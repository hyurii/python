# slowniki
status = {0: 'Green', 1: 'Yellow', 2: 'Red'}

# wczytanie danych

totalTC = int(input("Podaj ilosc wszystkich TC w spotchecku: "))
failedTC = int(input("Podaj ilosc TC w spotchecku ze statusem Failed: "))
totalPRCR = int(input("Podaj ilosc wszystkich dostarczanych PR/CR: "))
notRun = int(input("Podaj ilosc PR/CR ze statusem Not Run: "))
failedS = int(input("Podaj ilosc PR/CR typu S ze statusem Failed: "))
failedA = int(input("Podaj ilosc PR/CR typu A ze statusem Failed: "))
failedB = int(input("Podaj ilosc PR/CR typu B ze statusem Failed: "))
newS = int(input("Podaj ilosc PR typu S zgloszonych podczas testow CR/FT: "))
newA = int(input("Podaj ilosc PR typu A zgloszonych podczas testow CR/FT: "))
newB = int(input("Podaj ilosc PR typu B zgloszonych podczas testow CR/FT: "))

# obliczenia
if newS > 0:
    statusSS = 2
else:
    statusSS = 0

procTC = float(failedTC) / totalTC * 100.0
if procTC < 10:
    statusTC = 0
elif procTC > 30:
    statusTC = 2
else:
    statusTC = 1

procFailSA = float(failedS + failedA) / totalPRCR * 100.0
procFailB = float(failedB) / totalPRCR * 100.0

if procFailSA > 20 or procFailB > 40:
    statusOldPR = 2
elif (procFailSA >= 10 and procFailSA <= 20) or (procFailB >= 20 and procFailB <= 40):
    statusOldPR = 1
else:
    statusOldPR = 0

newSA = newS + newA
if newSA >= 7 or newB >= 14:
    statusNew = 2
elif newSA in range(4, 7) or newB in range(7 - 13):
    statusNew = 1
else:
    statusNew = 0

percentage = (1.0 - float(notRun) / totalPRCR) * 100.0
if percentage < 70:
    statusProc = 2
elif percentage >= 70 and percentage <= 80:
    statusProc = 1
else:
    statusProc = 0

generalStatus = max(statusSS, statusTC, statusOldPR, statusNew, statusProc)

# drukowanie i zapis do pliku
print
print("Test Results:")
print "- Summany/Status:" + status[generalStatus]
print "- Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: {0}, {1}".format(
    status[statusSS], str(newS))
print '- Percentage (%) of \"failed\" (by S, A, B PRs) and \"not implemented\" statuses of TCs in Spotcheck: {0}, {1}'.format(
    status[statusTC], str(int(procTC)))
print '- Percentage (%) of failed delivered PRs (S, A, B): {0}, A+S: {1}, B: {2}'.format(status[statusOldPR], str(
    int(procFailSA)), str(int(procFailB)))
print '- Number of PRs (S, A, B) discovered during testing delivered CRs/FTs: {0}, {1}'.format(status[statusNew], str(
    int(newSA + newB)))
print '- Percentage (%) of tested delivery: {0}, {1}'.format(status[statusProc], str(int(percentage)))

f = open('delivery.txt', 'w')
f.write("Test Results:\n")
f.write("- Summany/Status:{0}\n".format(status[generalStatus]))
f.write(
    '- Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: {0}, {1}\n'.format(
        status[statusSS], str(newS)))
f.write(
    '- Percentage (%) of \"failed\" (by S, A, B PRs) and \"not implemented\" statuses of TCs in Spotcheck: {0}, {1}\n'.format(
        status[statusTC], str(int(procTC))))
f.write("- Percentage (%) of failed delivered PRs (S, A, B): {0}, A+S: {1}, B: {2}\n".format(status[statusOldPR], str(
    int(procFailSA)), str(int(procFailB))))
f.write(
    "- Number of PRs (S, A, B) discovered during testing delivered CRs/FTs: {0}, {1}\n".format(status[statusNew], str(
        int(newSA + newB))))
f.write("- Percentage (%) of tested delivery: {0}, {1}\n".format(status[statusProc], str(int(percentage))))
f.close()
