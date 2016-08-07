import sys
if len(sys.argv) <= 2:
    print ('Usage: python3 [this] [input_file] [output_file]')
    sys.exit(0)
in_file = sys.argv[1]
out_file = sys.argv[2]
output = ''
with open(in_file, 'r', encoding='big5', errors='ignore') as f:
    for line in f:
        output += line
with open(out_file, 'w') as f:
    f.write(output)


