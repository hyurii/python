
'''     
Napisac skrypt ktory pyta nas o:
  1. ilosc wszystkich PRek:
  2. ilosc Fail A
  3. ilosc Fail B
  4. ilosc Fail S
  i drukuje % wszystkich prek i fail S/A/B '''


pr = input ("Enter the number of total PR: ")
fa = input ("Enter the number of Fail A: ")
fb = input ("Enter the number of Fail B: ")
fs = input ("Enter the number of Fail S: ")

print " "
print "Total PRs = ", pr , "(",int((pr*100)/pr), "%", ")"
print "Fail A = ", fa , "(", int((fa*100)/pr), "%", ")"
print "Fail B = ", fb , "(", int((fb*100)/pr), "%", ")"
print "Fail S = ", fs , "(", int((fs*100)/pr), "%", ")"
