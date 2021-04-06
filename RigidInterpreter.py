# globals
var_dict = {}

# returns whether string is int
def is_int(string):
    try: int(string); return True
    except: return False

# returns whether string is float
def is_float(string):
    try: float(string); return True
    except: return False

# parses given expression
def parse_expression(terms):
    return terms

# parses given term
def parse_term(term):
    if is_int(term): return int(term)
    elif is_float(term): return float(term)
    elif term in var_dict.keys(): return var_dict[term]
    else: return term[1:(len(term) - 1)]

# parses given value
def parse_value(value):
    terms = value.split()
    # if no terms, return none
    if len(terms) == 0: return None
    # if one term, parse term
    elif len(terms) == 1: return parse_term(terms[0])
    # if multiple terms, parse expression
    else: return parse_expression(terms)

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
