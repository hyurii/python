"""
Napisac skrypt ktory pyta nas o:
		1. ilosc wszystkich PRek:
		2. ilosc Fail A
		3. ilosc Fail B
		4. ilosc Fail S
		i drukuje % wszystkich prek i fail S/A/B
"""

Total_PRs = raw_input("What is the total number of PRs? -->")
Failed_S_PRs = raw_input("What is the number of failed S PRs? -->")
Failed_A_PRs = raw_input("What is the number of failed A PRs? -->")
Failed_B_PRs = raw_input("What is the number of failed B PRs? -->")

print
print "From the total of " + Total_PRs + " PRs:"
print  str((float(Failed_S_PRs) / float(Total_PRs))*100) + "% are Showstoppers" 
print  str((float(Failed_A_PRs) / float(Total_PRs))*100) + "% are A PRs"
print  str((float(Failed_B_PRs) / float(Total_PRs))*100) + "% are B PRs"
input ("Press ENTER to exit")
