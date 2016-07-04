'''
Created on 16 cze 2016

@author: Renata Cylejowska

Program oblicza status deliverki na podstawie zebranych danych wejœciowych.
'''
# from test.test_deque import fail

# WPROWADZANIE DANYCH POTRZEBNYCH DO OBLICZENIA STATUSOW
spot = float(raw_input("Ilosc wszystkich TC w spotchecku: "))
spotFailed = float(raw_input("Ilosc TC w spotchecku ze statusem Failed: "))

PRtotal = float(raw_input("Ilosc wszystkich PR/CR w deliverce: "))
PRnotrun = float(raw_input("Ilosc PR/CR ze statsuem Not Run: "))

PRfailedS = float(raw_input("Ilosc PR/CR typu S ze statusem Failed: "))
PRfailedA = float(raw_input("Ilosc PR/CR typu A ze statusem Failed: "))
PRfailedB = float(raw_input("Ilosc PR/CR typu B ze statusem Failed: "))
x = PRfailedA + PRfailedS

PRfoundS = int(raw_input("Ilosc PR typu S zgloszonych podczas deliverki: "))
PRfoundA = int(raw_input("Ilosc PR typu A zgloszonych podczas deliverki: "))
PRfoundB = int(raw_input("Ilosc PR typu B zgloszonych podczas deliverki: "))


# FUNKCJA OBLICZAJACA PROCENT
def percentage(total, fail):
    return int((fail / total) * 100)


# FUNKCJA OBLICZAJACA STATUS SPOTCHECKA
def statusSpotcheck(total, fail):
    if fail / total < 10.0 / 100:
        return "Green"
    elif fail / total > 30.0 / 100:
        return "Red"
    else:
        return "Yellow"


# FUNKCJA OBLICZAJACA STATUS PR-EK W DELIVERCE ZE STATUSEM "FAIL"
def statusFailedPR(s, a, b, total):
    if ((s + a) / total) < 10.0 / 100 and b / total < 20.0 / 100:
        return "Green"
    elif ((s + a) / total) > 20.0 / 100 or b / total > 40.0 / 100:
        return "Red"
    else:
        return "Yellow"


# FUNKCJA OBLICZAJACA STATUS WYKRYTYCH PR-EK W DELIVERCE
def statusNumberPR(s, a, b):
    if s + a <= 3 and b <= 6:
        return "Green"
    elif s + a >= 7 or b >= 14:
        return "Red"
    else:
        return "Yellow"


# FUNKCJA OBLICZAJACA ILOSC PRZETESTOWANEJ DELIVERKI
def statusDelivery(total, notrun):
    a = 100 - (notrun / total * 100)
    if a < 70:
        return "Red"
    elif a > 90:
        return "Green"
    else:
        return "Yellow"


# FUNKCJA OBLICZAJACA STATUS DELIVERKI Z WYKRYTMU PR-KAMI TYPU "S"
def statusShowstopper(s):
    if s == 0:
        return "Green"
    else:
        return "Red"


# FUNKCJA OBLICZAJACA OGOLNY STATUS DELIVERKI
def statusGlobal(n):
    for i in n:
        if i == "Red":
            return "Red"
            break
        elif i == "Green":
            return "Green"
            break
        else:
            return "Yellow"


lista = []
lista.append(statusShowstopper(PRfoundS))
lista.append(statusSpotcheck(spot, spotFailed))
lista.append(statusFailedPR(PRfailedS, PRfailedA, PRfailedB, PRtotal))
lista.append(statusNumberPR(PRfoundS, PRfoundA, PRfoundB))
lista.append(statusDelivery(PRtotal, PRnotrun))


# ZAPISANIE RAPORTU DO PLIKU
plik = open('deliverka.txt', 'w')
plik.write("Test Results:" + "\n"
"Summary/Status: " + str(statusGlobal(lista)) + "\n"
"Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: %s [%d]" % (statusShowstopper(PRfoundS), PRfoundS) + "\n"
"Percentage of FAILED (by S, A, B PRs) and NOT IMPLEMENTED statuses of TCs in Spotcheck: %s [%d%%]" % (statusSpotcheck(spot, spotFailed), percentage(spot, spotFailed)) + "\n"
"Percentage of FAILED delivered PRs (S, A, B): %s [A+S: %d%%, B: %d%%]" % (statusFailedPR(PRfailedS, PRfailedA, PRfailedB, PRtotal), percentage(PRtotal, x), percentage(PRtotal, PRfailedB)) + "\n"
"Number of PRs (old_S, A, B) discovered during testing delivered CRs, FTs: %s [S:%d, A:%d, B:%d]" % (statusNumberPR(PRfoundS, PRfoundA, PRfoundB), PRfoundS, PRfoundA, PRfoundB) + "\n"
"Percentage of tested delivery: %s [%d%%]" % (statusDelivery(PRtotal, PRnotrun), 100 - percentage(PRtotal, PRnotrun))
)
plik.close()


# WYDRUK RAPORTU NA KONSOLI
print "\n\nTest Results:"
print "Summary/Status: " + statusGlobal(lista)
print "Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: %s [%d]" % (statusShowstopper(PRfoundS), PRfoundS)
print "Percentage of FAILED (by S, A, B PRs) and NOT IMPLEMENTED statuses of TCs in Spotcheck: %s [%d%%]" % (statusSpotcheck(spot, spotFailed), percentage(spot, spotFailed))
print "Percentage of FAILED delivered PRs (S, A, B): %s [A+S: %d%%, B: %d%%]" % (statusFailedPR(PRfailedS, PRfailedA, PRfailedB, PRtotal), percentage(PRtotal, x), percentage(PRtotal, PRfailedB))
print "Number of PRs (old_S, A, B) discovered during testing delivered CRs, FTs: %s [S:%d, A:%d, B:%d]" % (statusNumberPR(PRfoundS, PRfoundA, PRfoundB), PRfoundS, PRfoundA, PRfoundB)
print "Percentage of tested delivery: %s [%d%%]" % (statusDelivery(PRtotal, PRnotrun), 100 - percentage(PRtotal, PRnotrun))
"\n"
"\n"
print "\n\nStatus deliverki zostal zapisany do pliku deliverka.txt"

input()
