# globals
vardict = {}

# whether string is int
def is_int(string):
    try: int(string); return True
    except: return False

# whether string is float
def is_float(string):
    try: float(string); return True
    except: return False

# evaluates given value
def evaluate(val):
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
    process_line(line)
    index += 1
