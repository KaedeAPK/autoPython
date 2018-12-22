
sp = [2,5,3.14, 1, -7]
sp.sort()
print(sp)
sp.sort(reverse=True)
print(sp)

ani = ['ant','cat','dog','eleph', 'badger']
print(ani)
ani.sort(reverse=True)
print(ani)

ppl = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats','Z']
ppl.sort()
print(ppl)
ppl.sort(key=str.lower)
print(ppl)