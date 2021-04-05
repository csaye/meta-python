# imports
import operator

# globals
vardict = {}
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

# whether string is int
def is_int(raw_s):
    s = raw_s.strip()
    try: int(s); return True
    except: return False

# whether string is float
def is_float(raw_s):
    s = raw_s.strip()
    try: float(s); return True
    except: return False

# whether string is string
def is_str(raw_s):
    s = raw_s.strip()
    open_a = False
    open_q = False
    for ch in s:
        # if apostrophe and not open quote
        if ch == "'" and not open_q: open_a = not open_a
        # if quote and not open apostrophe
        if ch == '"' and not open_a: open_q = not open_q
        # if no string open, return false
        if not open_a and not open_q: return False
    return True

# evaluates given value
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
            # set expression to true and pad operator
            is_exp = True
            val = val[:i] + ' ' + ch + ' ' + val[(i + 1):]
            i += 2
            val_len += 2
        i += 1
    # if expression
    if is_exp:
        # evaluate expression
    else:
        # evaluate singular term
        if is_int(val): return int(val)
        elif is_float(val): return float(val)
        elif val in vardict.keys(): return vardict[val]
        else: return val[1:(len(val) - 1)]

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
lines = fin.read().splitlines()
fin.close()

# go through lines
index = 0
while index < len(lines):
    line = lines[index].rstrip()
    # cut comment
    com_index = line.find('#')
    if com_index != -1: line = line[:com_index]
    process_line(line)
    index += 1
