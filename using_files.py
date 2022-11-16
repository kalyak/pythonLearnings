poem = '''\
Roses are red,
violets are violet,
Python is a snake,
and what this poem is made (in).'''

# Open file for 'w'riting
f = open('poem.txt', 'w')
# Write text to file
f.write(poem)
# Close the file
f.close()

# If no mode is specified,
# 'r'ead mode is assumed by default
f = open('poem.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    print(line, end='')
f.close()
