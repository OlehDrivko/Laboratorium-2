# Napisz skrypt działający jak prosty kalkulator, który potrafi dodawać, odejmować, mnożyć,
# dzielić oraz obliczać potęgę.
# Przykład: Jaką operację chcesz wykonać?
# 1) dodawanie
# 2) odejmowanie
# 3) mnożenie
# 4) dzielenie
# 5) potęgowanie
# Wpisz numer operacji: 2
# Podaj argument 1: 34
# Podaj argument 2: 5
# Wynik: 29

print('''
1) dodawanie
2) odejmowanie
3) mnożenie
4) dzielenie
5) potęgowanie
''')
X = int(input('what operation do you want to perform?'))
a = int(input("podaj a:"))
b = int(input("podaj b:"))
if X == 1:
    print (a+b)
elif X == 2:
        print(a - b)
elif X == 3:
        print(a * b)
elif X == 4:
        print(a / b)
elif X == 5:
        print(a ** b)
else:
    print('not a valid number')






