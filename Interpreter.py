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

# processes given line
def process_line(line):
    # print
    if line.startswith('print'):
        # get stripped content inside parentheses
        content = line[5:].strip()
        content = content[1:(len(content) - 1)].strip()
        # print content without quotations
        print(content[1:(len(content) - 1)])
    # variable
    if '=' in line:
        equal_index = line.find('=')
        # get variable and value
        var = line[:equal_index].strip()
        val = line[(equal_index + 1):].strip()
        # get result
        if is_int(val): res = int(val)
        elif is_float(val): res = float(val)
        elif val in vardict.keys(): res = vardict[val]
        else: res = val[1:(len(val) - 1)]
        # set result
        vardict[var] = res
        print(vardict)

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
