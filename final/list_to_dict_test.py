psets = [(1, 100), (2, 100), (2, 90)]
psets_new = {}
for p in psets:
    psets_new[p[0]] = p[1]
print psets_new

psets = psets_new.copy()

print 'psets',psets