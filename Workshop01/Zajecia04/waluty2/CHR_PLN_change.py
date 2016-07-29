import pickle
import valuty

dicts = {
    "EUR": 3.99,
    "PLN": 1.00,
    "CHR": 5.16
}

valuty.zapis(dicts)

f = open("plik.txt", "rb")
dict2 = pickle.load(f)
print dict2

dict2["PLN"], dict2["CHR"] = dict2["CHR"], dict2["PLN"]

print dict2
