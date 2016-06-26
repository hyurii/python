from __future__ import division
from Tkinter import *
import tkMessageBox
import sys
import math

okno = Tk()
okno.title("Status deliverki")
okno.geometry("1050x500")   #rozmiar naszego okna

ramka1 = Frame(okno).grid() # ramka do wprowadzanie danych
ramka2 = Frame(okno).grid() # ramka do raportu

etykietaGlowna = Label(ramka1, text = "PODAJ WARTOSCI:", font = ("Vileda",15, "bold"), pady = "20")
etykietaGlowna.grid(row = 1, column = 0, sticky = "W")

e1 = Label(ramka1, text = "Ilosc wszystkich TC w spotchecku: ").grid(row = 2, column = 0, sticky = "W")
spot = Entry(ramka1)
spot.grid(row = 2, column = 1)

e2 = Label(ramka1, text = "Ilosc TC w spotchecku ze statusem Failed: ").grid(row = 3, column = 0, sticky = "W")
spotFailed = Entry(ramka1)
spotFailed.grid(row = 3, column = 1)

e3 = Label(ramka1, text = "Ilosc wszystkich PR/CR w deliverce: ").grid(row = 5, column = 0, sticky = "W")
PRtotal = Entry(ramka1)
PRtotal.grid(row = 5, column = 1)

e4 = Label(ramka1, text = "Ilosc PR/CR ze statsuem Not Run: ").grid(row = 6, column = 0, sticky = "W")
PRnotrun = Entry(ramka1)
PRnotrun.grid(row = 6, column= 1)

e5 = Label(ramka1, text = "Ilosc PR/CR typu S ze statusem Failed: ").grid(row = 8, column = 0,sticky = "W")
PRfailedS = Entry(ramka1)
PRfailedS.grid(row = 8, column = 1)

e6 = Label(ramka1, text = "Ilosc PR/CR typu A ze statusem Failed: ").grid(row = 9, column = 0,sticky = "W")
PRfailedA = Entry(ramka1)
PRfailedA.grid(row = 9, column = 1)

e7 = Label(ramka1, text = "Ilosc PR/CR typu B ze statusem Failed: ").grid(row = 10, column = 0,sticky = "W")
PRfailedB = Entry(ramka1)
PRfailedB.grid(row = 10, column = 1)

e8 = Label(ramka1, text = "Ilosc PR typu S zgloszonych podczas deliverki: ").grid(row = 12, column = 0,sticky = "W")
PRfoundS = Entry(ramka1)
PRfoundS.grid(row = 12, column = 1)

e9 = Label(ramka1, text = "Ilosc PR typu A zgloszonych podczas deliverki: ").grid(row = 13, column = 0,sticky = "W")
PRfoundA = Entry(ramka1)
PRfoundA.grid(row = 13, column = 1)

e10 = Label(ramka1, text = "Ilosc PR typu B zgloszonych podczas deliverki: "). grid(row = 14, column = 0,sticky = "W")
PRfoundB = Entry(ramka1)
PRfoundB.grid(row = 14, column = 1)


# FUNKCJA OBLICZAJACA STATUS SPOTCHECKA
def statusSpotcheck():
   total = float(spot.get())
   fail = float(spotFailed.get())
   if fail / total < 10.0 / 100:
       return "Green"
   elif fail / total > 30.0 / 100:
       return "Red"
   else:
       return "Yellow"


# FUNKCJA OBLICZAJACA STATUS PR-EK W DELIVERCE ZE STATUSEM "FAIL"
def statusFailedPR():
   s = float(PRfailedS.get())
   a = float(PRfailedA.get())
   b = float(PRfailedB.get())
   total = float(PRtotal.get())
   if ((s + a) / total) < 10.0 / 100 and b / total < 20.0 / 100:
       return "Green"
   elif ((s + a) / total) > 20.0 / 100 or b / total > 40.0 / 100:
       return "Red"
   else:
       return "Yellow"

      
# FUNKCJA OBLICZAJACA STATUS WYKRYTYCH PR-EK W DELIVERCE
def statusNumberPR():
   s = int(PRfoundS.get())
   a = int(PRfoundA.get())
   b = int(PRfoundB.get())
   if s + a <= 3 and b <= 6:
       return "Green"
   elif s + a >= 7 or b >= 14:
       return "Red"
   else:
       return "Yellow"


# FUNKCJA OBLICZAJACA ILOSC PRZETESTOWANEJ DELIVERKI
def statusDelivery():
   total = float(PRtotal.get())
   notrun = float(PRnotrun.get())
   a = 100 - (notrun / total * 100)
   if a < 70:
       return "Red"
   elif a > 90:
       return "Green"
   else:
       return "Yellow"


# FUNKCJA OBLICZAJACA STATUS DELIVERKI Z WYKRYTMI PR-KAMI TYPU "S"
def statusShowstopper():
   s = int(PRfoundS.get())
   if s == 0:
       return "Green"
   else:
       return "Red"


# FUNKCJA OBLICZAJACA OGOLNY STATUS DELIVERKI
def statusGlobal():
   lista = []
   lista.append(statusShowstopper())
   lista.append(statusSpotcheck())
   lista.append(statusFailedPR())
   lista.append(statusNumberPR())
   lista.append(statusDelivery())
   for i in lista:
       if i == "Red":
           return "Red"
           break
       elif i == "Green":
           return "Green"
           break
       else:
           return "Yellow"


# FUNKCJA OBLICZAJACA PROCENT
def percentage(total, fail):
   return int((fail / total) * 100)

'''
def drukuj():
   x = float(PRfailedA.get()) + float(PRfailedS.get())
   print "\n\nTest Results:"
   print "Summary/Status: " + statusGlobal()
   print "Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: %s [%s]" % (statusShowstopper(), PRfoundS.get())
   print "Percentage of FAILED (by S, A, B PRs) and NOT IMPLEMENTED statuses of TCs in Spotcheck: %s [%d%%]" % (statusSpotcheck(), percentage(float(spot.get()), float(spotFailed.get())))
   print "Percentage of FAILED delivered PRs (S, A, B): %s [A+S: %d%%, B: %d%%]" % (statusFailedPR(), percentage(float(PRtotal.get()), x), percentage(float(PRtotal.get()), float(PRfailedB.get())))
   print "Number of PRs (old_S, A, B) discovered during testing delivered CRs, FTs: %s [S:%s, A:%s, B:%s]" % (statusNumberPR(), PRfoundS.get(), PRfoundA.get(), PRfoundB.get())
   print "Percentage of tested delivery: %s [%d%%]" % (statusDelivery(), 100 - percentage(float(PRtotal.get()), float(PRnotrun.get())))
'''
'''
def pokaz_jako_label():
   x = float(PRfailedA.get()) + float(PRfailedS.get())
   Label(ramka2, text = "Test Results:").grid(columnspan = 4, sticky = "W")
   Label(ramka2, text = "Summary/Status: " + statusGlobal()).grid(columnspan = 4, sticky = "W")
   Label(ramka2, text = "Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: %s [%s]" % (statusShowstopper(), PRfoundS.get())).grid(columnspan = 4, sticky = "W")
   Label(ramka2, text = "Percentage of FAILED (by S, A, B PRs) and NOT IMPLEMENTED statuses of TCs in Spotcheck: %s [%d%%]" % (statusSpotcheck(), percentage(float(spot.get()), float(spotFailed.get())))).grid(columnspan = 4, sticky = "W")
   Label(ramka2, text = "Percentage of FAILED delivered PRs (S, A, B): %s [A+S: %d%%, B: %d%%]" % (statusFailedPR(), percentage(float(PRtotal.get()), x), percentage(float(PRtotal.get()), float(PRfailedB.get())))).grid(columnspan = 4, sticky = "W")
   Label(ramka2, text = "Number of PRs (old_S, A, B) discovered during testing delivered CRs, FTs: %s [S:%s, A:%s, B:%s]" % (statusNumberPR(), PRfoundS.get(), PRfoundA.get(), PRfoundB.get())).grid(columnspan = 4, sticky = "W")
   Label(ramka2, text = "Percentage of tested delivery: %s [%d%%]" % (statusDelivery(), 100 - percentage(float(PRtotal.get()), float(PRnotrun.get())))).grid(columnspan = 4, sticky = "W")
'''

def pokaz_txt():
   if spot.get() == "0" or spot.get() == "":
      tkMessageBox.showinfo("Alert", "Ilosc wszystich TC w spotchecku nie moze wynosic zero")
   elif PRtotal.get() == "0" or PRtotal.get() == "":
      tkMessageBox.showinfo("Alert2", "Ilosc wszystich PR/CR w deliverce nie moze wynosic zero")
   else:   
      x = float(PRfailedA.get()) + float(PRfailedS.get())
      pole_txt.insert("1.0", "Test Results:\n")
      pole_txt.insert("2.0", "Summary/Status: " + statusGlobal() + "\n")
      pole_txt.insert("3.0", "Occurrence of minimum 1 Showstopper introduced by current delivery tasks, which NOT exist on earlier SI baseline: %s [%s]" % (statusShowstopper(), PRfoundS.get()) + "\n")
      pole_txt.insert("4.0", "Percentage of FAILED (by S, A, B PRs) and NOT IMPLEMENTED statuses of TCs in Spotcheck: %s [%d%%]" % (statusSpotcheck(), percentage(float(spot.get()), float(spotFailed.get()))) + "\n")
      pole_txt.insert("5.0", "Percentage of FAILED delivered PRs (S, A, B): %s [A+S: %d%%, B: %d%%]" % (statusFailedPR(), percentage(float(PRtotal.get()), x), percentage(float(PRtotal.get()), float(PRfailedB.get()))) + "\n")
      pole_txt.insert("6.0", "Number of PRs (old_S, A, B) discovered during testing delivered CRs, FTs: %s [S:%s, A:%s, B:%s]" % (statusNumberPR(), PRfoundS.get(), PRfoundA.get(), PRfoundB.get()) + "\n")
      pole_txt.insert("7.0", "Percentage of tested delivery: %s [%d%%]" % (statusDelivery(), 100 - percentage(float(PRtotal.get()), float(PRnotrun.get()))) + "\n")


def usun_wpisy():
   spot.delete(0, END)
   spotFailed.delete(0, END)
   PRtotal.delete(0, END)
   PRnotrun.delete(0, END)
   PRfailedS.delete(0, END)
   PRfailedA.delete(0, END)
   PRfailedB.delete(0, END)
   PRfoundS.delete(0, END)
   PRfoundA.delete(0, END)
   PRfoundB.delete(0, END)
   

#przycisk = Button(ramka1, text = "Oblicz status deliverki", command = drukuj).grid()
przycisk2 = Button(ramka1, text = "Wyswietl raport", command = pokaz_txt).grid(column = 1)
przycisk3 = Button(ramka1, text = "Wyczysc pola", command = usun_wpisy).grid(row = 15, column = 2)

etykietaDruga = Label(ramka2, text = "Raport koncowy: ", font = ("Vileda",15, "bold"))
etykietaDruga.grid(sticky = "W")

pole_txt = Text(ramka2, width = 125, height = 8)
pole_txt.grid(row = 20, column = 0, columnspan = 10)

przycisk4 = Button(ramka1, text = "Wyczysc raport", command = lambda: pole_txt.delete(0.0, END)).grid(column = 0)



 
okno.mainloop()
