"""
Napisac skrypt ktory pyta nas o:
		1. ilosc wszystkich PRek:
		2. ilosc Fail A
		3. ilosc Fail B
		4. ilosc Fail S
		i drukuje % wszystkich prek i fail S/A/B
"""
while True:
    while True:
        Fail_A=1
        Fail_B=1
        Fail_S=1
        Fail_all=1
        print "podaj liczbe  PR klasy A wprowadzonych do systemu"
        Fail_A = input()
        print "podaj liczbe PR klasy B w systemie"
        Fail_B = input()
        print "podaj liczbe PR klasy S w systemie"
        Fail_S = input()
        #Fail_all=Fail_A+Fail_B+Fail_S
        #print "Wszystkich PR jest ", Fail_all
        print "Podaj liczbe wsztskich PR w stystemie"
        temp=Fail_S+Fail_B+Fail_A
        Fail_all=input()
        if Fail_all>=temp:
            print "Dane poprawne"
            break
        else:
            print "Ogolna liczba PR jest mniejsza niz suma PR A, B i S. " \
                  "sprawdz dane i podaj je jeszcze raz"
    print "Procentowy udzal PR klas A B i S we wszystkich PR w systemie"
    print  str((float(Fail_S) / float(Fail_all))*100) + "% klasy S "
    print  str((float(Fail_A) / float(Fail_all))*100) + "% klasy A"
    print  str((float(Fail_B) / float(Fail_all))*100) + "% klasy B"

    print "Konczymy zabawe T czy N"
    konic=raw_input()
    if konic=='T':
        print "Pa pa"
        break

