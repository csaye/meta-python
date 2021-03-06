# imports
import operator

# variable dictionary
varlist = {}

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

# comparison operator dictionary
comparison_ops = {
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne
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

# returns number of preceding tabs in line
def count_tabs(line):
    spaces = 0
    for ch in line:
        if ord(ch) != 32: break
        spaces += 1
    tabs = spaces // 4
    return tabs

# gets end line of start line expression
def get_end_line(start_line):
    # get last line of while
    tabs = count_tabs(lines[start_line])
    end_index = start_line
    while (
        # end index before last line
        end_index < len(lines) - 1
        and (
        # line empty
        not lines[end_index + 1]
        # or line has enough tabs
        or count_tabs(lines[end_index + 1]) > tabs)
        ): end_index += 1
    return end_index

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
            # add parentheses if nothing inside
            if (i != len(string) - 1
            and ch == '(' and string[i + 1] == ')'):
                word += ch
            if (i != 0
            and ch == ')' and string[i - 1] == '('):
                word += ch
        else: word += ch
        # if last char, end word
        if i == len(string) - 1:
            if len(word) > 0: words.append(word)
    return words

# parses given boolean expression
def parse_boolean(expression):
    terms = smart_split(expression)
    # find comparison operator
    for i in range(len(terms)):
        term = terms[i]
        if term in comparison_ops:
            # parse expressions left and right of operator
            a = parse_expression(terms[:i])
            b = parse_expression(terms[(i + 1):])
            # return comparison
            return comparison_ops[term](a, b)

# parses given expression
def parse_expression(terms):
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
                a = parse_value(str(terms[i - 1]))
                b = parse_value(str(terms[i + 1]))
                result = operation(term)(a, b)
                # update terms list and break
                terms = terms[:(i - 1)] + [result] + terms[(i + 2):]
                break
    # return first term parsed
    return parse_term(terms[0])

# parses given term
def parse_term(term):
    if term == 'input()': return input() # input
    elif is_int(term): return int(term) # int
    elif is_float(term): return float(term) # float
    elif term in varlist.keys(): return varlist[term] # variable
    else: return term.strip("'") # string

# parses given value
def parse_value(value):
    terms = smart_split(value)
    # if no terms, return none
    if len(terms) == 0: return None
    # if one term, parse term
    elif len(terms) == 1: return parse_term(terms[0])
    # if multiple terms, parse expression
    else: return parse_expression(terms)

# parses given line
def parse_line(line):
    global line_index, lines, loop_lines
    # remove comment
    comment_index = raw_line.find('#')
    if comment_index != -1:
        line = line[:comment_index]
    # strip line
    line = line.strip()
    terms = smart_split(line)
    # print
    if line.startswith('print('):
        raw_value = line[6:(len(line) - 1)]
        value = parse_value(raw_value)
        print(value)
    # if
    elif line.startswith('if '):
        # get boolean value
        raw_value = line[3:(len(line) - 1)]
        value = parse_boolean(raw_value)
        # get last line of if
        end_index = get_end_line(line_index)
        # if if fails, skip to end of if
        if not value: line_index = end_index
        # if if passes and else statement
        elif lines[end_index + 1].strip().startswith('else:'):
            # append loop line to skip else
            end_end_index = get_end_line(end_index + 1)
            loop_lines.append((end_index, end_end_index + 1))
    # while
    elif line.startswith('while '):
        # get boolean value
        raw_value = line[6:(len(line) - 1)]
        value = parse_boolean(raw_value)
        # get last line of while
        end_index = get_end_line(line_index)
        # if while true, append loop line
        if value: loop_lines.append((end_index, line_index))
        # if while false, skip to end of while
        else: line_index = end_index
    # define method
    elif line.startswith('def '):
        # skip to end of method
        line_index = get_end_line(line_index)
    # call method
    elif len(terms) == 1 and line.endswith('()'):
        # get method name
        method = line[:(len(line) - 2)]
        # for each line
        for i in range(len(lines)):
            # if method def
            if lines[i].startswith('def ' + method):
                # create loop line
                end_index = get_end_line(i)
                loop_lines.append((end_index, line_index + 1))
                # set line index and break
                line_index = i
                break
    # variable
    elif len(terms) > 2 and terms[1].endswith('='):
        # get variable, operator, and value
        var = terms[0]
        op = terms[1]
        val = parse_expression(terms[2:])
        # assign variable
        if op == '=': varlist[var] = val
        # modify variable by self
        else:
            mod_op = op[:(len(op) - 1)]
            varlist[var] = operation(mod_op)(varlist[var], val)
    # if loop lines
    if len(loop_lines) > 0:
        # if line index matches top loop line
        last_index = len(loop_lines) - 1
        if line_index == loop_lines[last_index][0]:
            # go to line index of loop line
            line_index = loop_lines[last_index][1] - 1
            # pop loop line
            loop_lines.pop()

# read input
fin = open('./Input.py', 'r')
lines = fin.read().splitlines()
fin.close()

# parse lines
loop_lines = []
line_index = 0
while line_index < len(lines):
    line = lines[line_index]
    parse_line(line)
    line_index += 1
