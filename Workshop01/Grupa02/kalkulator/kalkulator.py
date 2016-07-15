import kalk_funkcje


# def dodawanie():
#     pass
#
#
# def odejmowanie():
#     pass
#
#
# def mnozenie():
#     pass
#
#
# def dzielenie():
#     pass
#
#
# def potegowanie():
#     pass
#
#
# def pierwiastkowanie():
#     pass

while True:
    print """
    Wybierz operacje:
    [1] dodawanie
    [2] odejmowanie
    [3] mnozenie
    [4] dzielenie
    [5] potegowanie
    [5] pierwiastkowanie
    [0] wyjscie
    """
    ans = int(raw_input("Twoj wybor: "))

    if 1 == ans:
        print kalk_funkcje.dodawanie()
    elif 2 == ans:
        print kalk_funkcje.odejmowanie()
    elif 3 == ans:
        print kalk_funkcje.mnozenie()
    elif 4 == ans:
        print kalk_funkcje.dzielenie()
    elif 5 == ans:
        print kalk_funkcje.potegowanie()
    elif 6 == ans:
        print kalk_funkcje.pierwiastkowanie()
    elif 0 == ans:
        print "Konczymy"
        break
    else:
        continue
    next_operation = raw_input("Czy chcesz przerwac? (t / n)")
    if "t" == next_operation:
        break
