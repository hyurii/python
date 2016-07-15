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
    print "text:", ans
    if 1 == ans:
        print dodawanie()
    elif 2 == ans:
        print odejmowanie()
    elif 3 == ans:
        print mnozenie()
    elif 4 == ans:
        print dzielenie()
    elif 5 == ans:
        print potegowanie()
    elif 6 == ans:
        print pierwiastkowanie()
    elif 0 == ans:
        print "Konczymy"
        break
    else:
        continue
    ans = raw_input("Czy chcesz wykonac kolejna operacje? (t / n)")
    if "t" == ans:
        break
