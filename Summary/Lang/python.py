l = [1,2,3,4,5]
for i in l:
    print(i)


for i in range(10):
    print(i)

d = ['a','b', 'c', 'd', 'e']
for i,j in zip(l,d):
    print(i, j)

print('-------------')

for i,j in enumerate(d):
    print(i,j)


dic = {'a': 'guauga', 'b': 'jaijia'}
for k,v in dic.iteritems():
    print(k,v)