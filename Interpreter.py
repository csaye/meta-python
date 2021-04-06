# imports
import operator

# globals
vardict = {}
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '//': operator.floordiv,
    '**': operator.pow
}
# operator precedence
op_precedence = {
    '+': 0,
    '-': 0,
    '*': 1,
    '/': 1,
    '%': 1,
    '//': 1,
    '**': 2
}
# returns op precedence for given value
def oppre(val):
    if val not in op_precedence.keys(): return -1
    return op_precedence[val]
# double operator chars
dops = ['*', '/']

# formats and appends given line to lines
def format_line(raw_line):
    global lines
    line = raw_line.strip()
    # format line
    open_q = False; open_a = False
    line_len = len(line)
    for i in range(line_len):
        ch = line[i]
        # parse quotations
        if ch == "'" and not open_q: open_a = not open_a
        if ch == '"' and not open_a: open_q = not open_q
        # if no open string
        if not open_a and not open_q:
            # split by semicolon
            if ch == ';':
                lines.append(line[:i])
                format_line(line[(i + 1):])
                return
            # cut comment
            if ch == '#':
                lines.append(line[:i])
                return
    lines.append(line)

# whether string is int
def is_int(raw_s):
    s = str(raw_s).strip()
    try: int(s); return True
    except: return False

# whether string is float
def is_float(raw_s):
    s = str(raw_s).strip()
    try: float(s); return True
    except: return False

# whether string is string
def is_str(raw_s):
    s = str(raw_s).strip()
    open_a = False; open_q = False
    for i in range(len(s)):
        ch = s[i]
        # if apostrophe and not open quote
        if ch == "'" and not open_q: open_a = not open_a
        # if quote and not open apostrophe
        if ch == '"' and not open_a: open_q = not open_q
        # if end
        if i == len(s) - 1:
            # if string open, return false
            if open_a or open_q: return False
        # if not end
        else:
            # if string closed, return false
            if not open_a and not open_q: return False
    return True

# evaluates singular value
def eval_val(val):
    if is_int(val): return int(val)
    elif is_float(val): return float(val)
    elif val in vardict.keys(): return vardict[val]
    elif is_str(val): return val[1:(len(val) - 1)]
    else: return val

# splits a string, keeping quotes and parentheses together
def smart_split(string):
    words = []; word = ''
    open_par = 0
    open_a = False; open_q = False
    # for all chars in string
    for i in range(len(string)):
        ch = string[i]
        # parse quotations
        if ch == "'" and not open_q: open_a = not open_a
        if ch == '"' and not open_a: open_q = not open_q
        # if no open string
        if not open_a and not open_q:
            # parse parentheses
            if ch == '(': open_par += 1
            if ch == ')': open_par -= 1
            # if whitespace and no open parentheses
            if ch.isspace() and open_par <= 0:
                # close word and reset
                if len(word) > 0: words.append(word)
                word = ''
            # if not whitespace or parentheses, append char
            else: word += ch
        # if in string, append char
        else: word += ch
        # if end of string
        if i == len(string) - 1:
            # close word
            if len(word) > 0: words.append(word)
    return words

# evaluates expression value
def eval_exp(exp):
    # smart split elements
    elems = smart_split(exp)
    # while more than one element
    while len(elems) > 1:
        # for each element
        for i in range(len(elems)):
            elem = elems[i]
            # if operator
            if elem in ops:
                # enforce order of operations
                if any(oppre(elem) < oppre(e) for e in elems): continue
                # evaluate operation and break
                a = eval_exp(str(elems[i - 1]).strip('()'))
                b = eval_exp(str(elems[i + 1]).strip('()'))
                res = ops[elem](a, b)
                elems = elems[:(i - 1)] + [res] + elems[(i + 2):]
                break
    # return first element value
    return eval_val(elems[0])

# evaluates value
def evaluate(raw_val):
    # strip value
    val = raw_val.strip()
    # expression
    open_a = False; open_q = False
    is_exp = False
    i = 0; val_len = len(val)
    while i < val_len:
        ch = val[i]
        # parse open string status
        if ch == "'" and not open_q: open_a = not open_a
        if ch == '"' and not open_a: open_q = not open_q
        # if string not open and operator
        if not open_a and not open_q and ch in ops:
            is_exp = True
            # special case for multiple char operators
            if i < val_len - 1 and ch in dops and ch == val[i + 1]:
                val = val[:i] + ' ' + ch * 2 + ' ' + val[(i + 2):]
                i += 3
            # set expression to true and pad operator
            else:
                val = val[:i] + ' ' + ch + ' ' + val[(i + 1):]
                i += 2
            val_len += 2
        i += 1
    # if expression value
    if is_exp: return eval_exp(val)
    # if singular value
    else: return eval_val(val)

# processes given line
def process_line(line):
    # print
    if line.startswith('print'):
        # get stripped value inside parentheses
        val = line[5:].strip()
        val = val[1:(len(val) - 1)].strip()
        # print evaluated value
        print(evaluate(val))
    # variable
    if '=' in line:
        equal_index = line.find('=')
        # get variable and value
        var = line[:equal_index].strip()
        val = line[(equal_index + 1):].strip()
        # set result to evaluated value
        vardict[var] = evaluate(val)

# read input
fin = open('./Input.py', 'r')
raw_lines = fin.read().splitlines()
fin.close()

# format lines
lines = []
for line in raw_lines:
    format_line(line)

#print(lines)

# parse lines
index = 0; length = len(lines)
while index < length:
    # process line
    line = lines[index]
    process_line(line)
    index += 1
