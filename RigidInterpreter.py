# imports
import operator

# variable dictionary
variables = {}

# operator dictionary
operators = {
    '+': (operator.add, 0),
    '-': (operator.sub, 0),
    '*': (operator.mul, 1),
    '/': (operator.truediv, 1),
    '%': (operator.mod, 1),
    '//': (operator.floordiv, 1),
    '**': (operator.pow, 2)
}

# returns operator operation
def operation(operator):
    return operators[operator][0]

# returns operator precedence
def precendence(operator):
    return operators[operator][1]

# returns whether string is int
def is_int(string):
    try: int(string); return True
    except: return False

# returns whether string is float
def is_float(string):
    try: float(string); return True
    except: return False

# splits given string, keeping quotes and parentheses together
def smart_split(string):
    words = []; word = ''
    open_par = 0; open_quo = False
    # for each char in string
    for i in range(len(string)):
        ch = string[i]
        # parse quotations
        if ch == "'": open_quo = not open_quo
        # if no open quotations
        if not open_quo:
            # parse parentheses
            if ch == '(': open_par += 1
            elif ch == ')': open_par -= 1
            # if space and no open parentheses, end word
            elif ch.isspace() and open_par <= 0:
                if len(word) > 0: words.append(word)
                word = ''
            else: word += ch
        else: word += ch
        # if last char, end word
        if i == len(string) - 1:
            if len(word) > 0: words.append(word)
    return words

# parses given expression
def parse_expression(expression):
    terms = smart_split(expression)
    # while multiple terms
    while len(terms) > 1:
        for i in range(len(terms)):
            term = terms[i]
            if term in operators:
                # enforce order of operations
                if any(
                    t in operators
                    and precendence(term) < precendence(t)
                    for t in terms
                ): continue
                # evaluate operation
                a = parse_expression(str(terms[i - 1]))
                b = parse_expression(str(terms[i + 1]))
                result = operation(term)(a, b)
                # update terms list and break
                terms = terms[:(i - 1)] + [result] + terms[(i + 2):]
                break
    # return first term parsed
    return parse_term(terms[0])

# parses given term
def parse_term(term):
    if is_int(term): return int(term) # int
    elif is_float(term): return float(term) # float
    elif term in var_dict.keys(): return var_dict[term] # variable
    else: return term.strip("'") # string

# parses given value
def parse_value(value):
    terms = smart_split(value)
    # if no terms, return none
    if len(terms) == 0: return None
    # if one term, parse term
    elif len(terms) == 1: return parse_term(value)
    # if multiple terms, parse expression
    else: return parse_expression(value)

# parses given line
def parse_line(raw_line):
    # strip line
    line = raw_line.strip()
    # print
    if line.startswith('print'):
        raw_value = line[6:(len(line) - 1)]
        value = parse_value(raw_value)
        print(value)

# read input
fin = open('./Input.py', 'r');
lines = fin.read().splitlines()
fin.close()

# parse lines
line_index = 0;
while line_index < len(lines):
    line = lines[line_index];
    parse_line(line)
    line_index += 1
