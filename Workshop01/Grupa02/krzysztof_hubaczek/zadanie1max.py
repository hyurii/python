import tkFileDialog
import tkMessageBox
from Tkinter import *
from datetime import *


def statusSS(newS):
    if newS > 0:
        return 2
    else:
        return 0


def statusTC(failedTC, totalTC):
    procTC = float(failedTC) / totalTC * 100.0
    if procTC < 10:
        return 0
    elif procTC > 30:
        return 2
    else:
        return 1


def statusOldPR(failedS, failedA, failedB, totalPRCR):
    procFailSA = float(failedS + failedA) / totalPRCR * 100.0
    procFailB = float(failedB) / totalPRCR * 100.0

    if procFailSA > 20 or procFailB > 40:
        return 2
    elif (procFailSA >= 10 and procFailSA <= 20) or (procFailB >= 20 and procFailB <= 40):
        return 1
    else:
        return 0


def statusNew(newS, newA, newB):
    newSA = newS + newA
    if newSA >= 7 or newB >= 14:
        return 2
    elif newSA in range(4, 7) or newB in range(7 - 13):
        return 1
    else:
        return 0


def statusProc(notRun, totalPRCR):
    percentage = (1.0 - float(notRun) / totalPRCR) * 100.0
    if percentage < 70:
        return 2
    elif percentage >= 70 and percentage <= 80:
        return 1
    else:
        return 0


def generalStatus(statusSS, statusTC, statusOldPR, statusNew, statusProc):
    return max(statusSS, statusTC, statusOldPR, statusNew, statusProc)


# slownik
status = {0: 'Green', 1: 'Yellow', 2: 'Red'}


def fileSave():
    text2save = str(textField.get(1.0, END))
    if not text2save.isspace():
        f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt", title='Save delivery raport',
                                       filetypes=[('all files', '.*'), ('text files', '.txt')],
                                       initialfile="deliveryStatusCW" + str(datetime.today().strftime("%y")) + str(
                                           datetime.today().isocalendar()[1]))  #
        if f is None:
            return
        f.write(text2save)
        f.close()
    else:
        tkMessageBox.showwarning("Alert", "Raport field is empty!!!")


def checkValues():
    totalTC = totalTCinput.get()
    failedTC = failedTCinput.get()
    totalPRCR = totalPRCRinput.get()
    notRun = notRunInput.get()
    failedS = failedSinput.get()
    failedA = failedAinput.get()
    failedB = failedBinput.get()
    newS = newSinput.get()
    newA = newAinput.get()
    newB = newBinput.get()
    if totalTC == "0" or totalTC.isspace() or not totalTC.isdigit():
        tkMessageBox.showwarning("Alert", "Wprowadz poprawna ilosc wszystich TC w spotchecku")
        totalTCinput.delete(0, END)
        return False
    elif totalPRCR == "0" or totalPRCR.isspace() or not totalPRCR.isdigit():
        tkMessageBox.showwarning("Alert", "Wprowadz poprawna ilosc wszystich PR/CR w deliverce")
        totalPRCRinput.delete(0, END)
        return False
    elif int(failedTC) > int(totalTC):
        tkMessageBox.showwarning("Alert", "Wprowadz poprawna ilosc TC i failedTC w spotchecku")
        return False
    elif int(totalPRCR) < int(notRun) + int(failedS) + int(failedB) + int(failedA):
        tkMessageBox.showwarning("Alert", "Wprowadz poprawna ilosc PR (NotRun/S/A/B) w spotchecku")
        return False
    elif not (
                                                totalTC.isdigit() and failedTC.isdigit() and totalPRCR.isdigit() and notRun.isdigit() and failedS.isdigit() and failedA.isdigit() and failedB.isdigit() and newS.isdigit() and newA.isdigit() and newB.isdigit()):
        tkMessageBox.showwarning("Alert", "Wprowadz poprawne dane!!!")
        return False
    else:
        return True


def raport():
    if checkValues():
        resetRaport()
        totalTC = int(totalTCinput.get())
        failedTC = int(failedTCinput.get())
        totalPRCR = int(totalPRCRinput.get())
        notRun = int(notRunInput.get())
        failedS = int(failedSinput.get())
        failedA = int(failedAinput.get())
        failedB = int(failedBinput.get())
        newS = int(newSinput.get())
        newA = int(newAinput.get())
        newB = int(newBinput.get())
        procTC = int(float(failedTC) / totalTC * 100.0)
        procFailSA = int(float(failedS + failedA) / totalPRCR * 100.0)
        procFailB = int(float(failedB) / totalPRCR * 100.0)
        percentage = int((1.0 - float(notRun) / totalPRCR) * 100.0)
        statSS = statusSS(newS)
        statTC = statusTC(failedTC, totalTC)
        statOldPR = statusOldPR(failedS, failedA, failedB, totalPRCR)
        statNew = statusNew(newS, newA, newB)
        statProc = statusProc(notRun, totalPRCR)
        general = generalStatus(statSS, statTC, statOldPR, statNew, statProc)

        textField.insert("1.0", "Test Results:\n")
        textField.insert("2.0", "- Summary/Status: {0}\n".format(status[general]))
        textField.insert("3.0",
                         "- Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: {0:s} [{1:s}]\n".format(
                             status[statSS], str(newS)))
        textField.insert("4.0",
                         "- Percentage of FAILED (by S, A, B PRs) and NOT IMPLEMENTED statuses of TCs in Spotcheck: {0:s} [{1:d}%]\n".format(
                             status[statTC], procTC))
        textField.insert("5.0", "- Percentage of FAILED delivered PRs (S, A, B): {0} [A+S: {1}%, B: {2}%]\n".format(
            status[statOldPR], procFailSA, procFailB))
        textField.insert("6.0",
                         "- Number of PRs (old_S, A, B) discovered during testing delivered CRs, FTs: {0} [S:{1}, A:{2}, B:{3}]\n".format(
                             status[statNew], newS, newA, newB))
        textField.insert("7.0",
                         "- Percentage of tested delivery: {0:s} [{1:d}%]\n".format(status[statProc], percentage))


def reset():
    totalTCinput.delete(0, END)
    failedTCinput.delete(0, END)
    totalPRCRinput.delete(0, END)
    notRunInput.delete(0, END)
    failedSinput.delete(0, END)
    failedAinput.delete(0, END)
    failedBinput.delete(0, END)
    newSinput.delete(0, END)
    newAinput.delete(0, END)
    newBinput.delete(0, END)


def resetRaport():
    textField.delete(0.0, END)


# rysowanie okna

mainWindow = Tk()
mainWindow.title("Delivery status")
mainWindow.resizable(width=False, height=False)

inputFrame = Frame(mainWindow, padx=10, pady=10)
inputFrame.pack(fill="both")
resultFrame = LabelFrame(mainWindow, text="Raport", font=("Verdana", 15), padx=10, pady=10)
resultFrame.pack(pady=5)

label0 = Label(inputFrame, text="Wprowadz wartosci:", font=("Vileda", 15, "bold"))
label0.grid(row=1, column=0, sticky="W")

label1 = Label(inputFrame, text="Ilosc wszystkich TC w spotchecku: ").grid(row=3, column=0, sticky="W")
totalTCinput = Entry(inputFrame)
totalTCinput.grid(row=3, column=1)

label2 = Label(inputFrame, text="Ilosc TC w spotchecku ze statusem Failed:").grid(row=4, column=0, sticky="W")
failedTCinput = Entry(inputFrame)
failedTCinput.grid(row=4, column=1)

label3 = Label(inputFrame, text="Ilosc wszystkich PR/CR w deliverce:").grid(row=5, column=0, sticky="W")
totalPRCRinput = Entry(inputFrame)
totalPRCRinput.grid(row=5, column=1)

label4 = Label(inputFrame, text="Ilosc PR/CR ze statusem Not Run:").grid(row=6, column=0, sticky="W")
notRunInput = Entry(inputFrame)
notRunInput.grid(row=6, column=1)

label5 = Label(inputFrame, text="Ilosc PR/CR typu S ze statusem Failed:").grid(row=1, column=2, sticky="W")
failedSinput = Entry(inputFrame)
failedSinput.grid(row=1, column=3)

label6 = Label(inputFrame, text="Ilosc PR/CR typu A ze statusem Failed:").grid(row=2, column=2, sticky="W")
failedAinput = Entry(inputFrame)
failedAinput.grid(row=2, column=3)

label7 = Label(inputFrame, text="Ilosc PR/CR typu B ze statusem Failed:").grid(row=3, column=2, sticky="W")
failedBinput = Entry(inputFrame)
failedBinput.grid(row=3, column=3)

label8 = Label(inputFrame, text="Ilosc PR typu S zgloszonych podczas deliverki:").grid(row=4, column=2, sticky="W")
newSinput = Entry(inputFrame)
newSinput.grid(row=4, column=3)

label9 = Label(inputFrame, text="Ilosc PR typu A zgloszonych podczas deliverki:").grid(row=5, column=2, sticky="W")
newAinput = Entry(inputFrame)
newAinput.grid(row=5, column=3)

label10 = Label(inputFrame, text="Ilosc PR typu B zgloszonych podczas deliverki:").grid(row=6, column=2, sticky="W")
newBinput = Entry(inputFrame)
newBinput.grid(row=6, column=3)

raportButton = Button(inputFrame, text="Generuj raport", command=raport).grid(row=1, column=4)
resetButton = Button(inputFrame, text="Resetuj pola", command=reset).grid(row=2, column=4)

textField = Text(resultFrame, width=125, height=8)
textField.grid()

rapSave = Button(inputFrame, text="Zapisz raport", command=fileSave).grid(row=5, column=4)
rapReset = Button(inputFrame, text="Resetuj raport", command=resetRaport).grid(row=6, column=4)

mainWindow.mainloop()
