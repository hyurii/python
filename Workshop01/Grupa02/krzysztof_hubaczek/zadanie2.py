def procent(dzielna, dzielnik):
    try:
        return (float(dzielna) / dzielnik * 100.0)
    except ZeroDivisionError:
        print('Ilosc wszystkich PRek nie moze wynosic zero!!!')
        return '-'


totalPRs = input("Podaj ilosc wszystkich PRek: ")
APR = input("Podaj ilosc PRek A: ")
BPR = input("Podaj ilosc PRek B: ")
SPR = input("Podaj ilosc PRek S: ")
print "Failed S: {0}%".format(procent(SPR, totalPRs))
print "Failed A: {0}%".format(procent(APR, totalPRs))
print "Failed B: {0}%".format(procent(BPR, totalPRs))
