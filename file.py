f = open('test.txt','r')
print(f)


#lexojm sa linja ka file yne
count = 0
for line in f:
    count = count + 1
print('Line Count:', count)


inp = f.read()
print(len(inp))


for line in f:
    if line.startswith('a'):
        print(line)
