""" 
  Napisac skrypt ktory pyta nas o:
  1. ilosc wszystkich PRek:
  2. ilosc Fail A
  3. ilosc Fail B
  4. ilosc Fail S
  i drukuje % wszystkich prek i fail S/A/B
"""

totalPRs = input("How many PRs: ")
failA = input("How many Fail A: ")
failB = input("How many Fail B: ")
failS = input("How many Fail S: ")

print "\nTotal PRs: " + str(totalPRs)
print "Fail A:", (float(failA) / totalPRs) * 100, "%"
print "Fail B:", (float(failB) / totalPRs) * 100, "%"
print "Fail B:", (float(failS) / totalPRs) * 100, "%"
