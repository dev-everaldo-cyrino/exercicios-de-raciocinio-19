n = input('digite um DNA usando (G,T,C,A) : ')
n = n.upper()
rna = ''
for x in range(len(n)):
    if n[x] == 'T':
        rna += "t"
    elif n[x] == 'A':
        rna += "u"
    elif n[x] == 'C':
        rna += "g"
    elif n[x] == 'G':
        rna += "c"
    
print('o DNA {} , transcrito em RNA fica {}'.format(n,rna.upper()))