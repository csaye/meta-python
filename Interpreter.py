# processes given line
def process_line(line):
    # print
    if line.startswith('print'):
        # get stripped content inside parentheses
        content = line[5:].strip()
        content = content[1:(len(content) - 1)].strip()
        # print content without quotations
        print(content[1:(len(content) - 1)])

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
