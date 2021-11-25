chisla = []
for q in range(60):
    chisla.append(q)

chisla.reverse()
i1, i2, i3 = 0, 0, 0

def ner(i1, i2, i3):
    if (i1 + i2 > i3) and (i1 + i3 > i2) and (i2 + i3 > i1):
        s = (i1 + i2 + i3) / 2
        return (s * (s - i1) * (s - i2) * (s - i3)) ** (1 / 2)
    return 0


for i in range(len(chisla)):

    i1 = chisla[i]
    i2 = chisla[i + 1]
    i3 = chisla[i + 2]
    if ner(i1, i2, i3) != 0:
        print(ner(i1, i2, i3))
        print(i1, i2, i3)
        break
