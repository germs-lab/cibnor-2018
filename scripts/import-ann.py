import sys, screed

d = {}
for record in screed.open(sys.argv[1]):
    dat = record.name.split(' ', 1)
    id1 = dat[0]
    id2 = dat[1]
    d[id1] = id2

for n, line in enumerate(open(sys.argv[2])):
    dat = line.rstrip().split('\t')
    if n > 0:
        ann = d[dat[0]]
        dat.insert(1, ann)
    else:
        dat.insert(0, "Gene ID")
        dat.insert(1, "Gene Annotation")
    print '\t'.join(dat)
        
    
