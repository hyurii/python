'''
Created on 16 cze 2016

@author: zablodan
'''
allPrs = input("Enter number of all PRs in delivery: ")
failedPrS = input("Enter number of failed PR with severity S: ")
failedPrA = input("Enter number of failed PR with severity A: ")
failedPrB = input("Enter number of failed PR with severity B: ")

percentPrS = failedPrS / float(allPrs) * 100
percentPrA = failedPrA / float(allPrs) * 100
percentPrB = failedPrB / float(allPrs) * 100

print "Percent o failed PR with severity S = " + str(round(percentPrS, 1)) + "%"
print "Percent o failed PR with severity A = " + str(round(percentPrA, 1)) + "%"
print "Percent o failed PR with severity B = " + str(round(percentPrB, 1)) + "%"

if __name__ == '__main__':
    pass
