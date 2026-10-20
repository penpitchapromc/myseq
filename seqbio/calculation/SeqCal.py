def countBase(seq, base):
    return seq.count(base)


def gcContent(seq):
    return (countBase(seq, 'G') + countBase(seq, 'C')) / len(seq)


def atContent(seq):
    return (countBase(seq, 'A') + countBase(seq, 'T')) / len(seq)


def countBasesDict(seq):
    basesM = {}
    for base in seq:
        basesM.setdefault(base, 0)
        basesM[base] = basesM[base] +1
    return basesM



