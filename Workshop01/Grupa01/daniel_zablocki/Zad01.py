'''
Created on 16 cze 2016

@author: zablodan
'''


def inputInt(Text):
    while True:
        try:
            In = int(raw_input(Text))
            if In < 0:
                print 'Number can not be negative!'
                continue
            break
        except ValueError:
            print("It's not number!")
            continue
    return In

while True:
    allPrs = inputInt("Enter number of all PRs in delivery: ")
    if allPrs == 0:
        print "Number must be grater than 0!"
        continue

    failedPrS = inputInt("Enter number of failed PR with severity S: ")
    failedPrA = inputInt("Enter number of failed PR with severity A: ")
    failedPrB = inputInt("Enter number of failed PR with severity B: ")
    if ((failedPrS + failedPrA + failedPrB) > allPrs):
        print "Number of PRs disagree!"
        continue
    break

percentPrS = failedPrS / float(allPrs) * 100
percentPrA = failedPrA / float(allPrs) * 100
percentPrB = failedPrB / float(allPrs) * 100

print "Percent o failed PR with severity S = " + str(round(percentPrS, 1)) + "%"
print "Percent o failed PR with severity A = " + str(round(percentPrA, 1)) + "%"
print "Percent o failed PR with severity B = " + str(round(percentPrB, 1)) + "%"
