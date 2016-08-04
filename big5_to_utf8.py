import sys
filepath = sys.argv[1]
output = ''
with open(filepath, 'r', encoding='big5', errors='ignore') as f:
    for line in f:
        output += line
print (output)


