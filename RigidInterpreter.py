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
