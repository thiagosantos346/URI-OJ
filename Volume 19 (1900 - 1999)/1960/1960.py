n = int(input())
s = ""
if n >= 1000:
    s += 'M'*int(n/1000)
    n %= 1000
if n >= 900:
    s += 'CM'*int(n/900)
    n %= 900
if n >= 500:
    s += 'D'*int(n/500)
    n %= 500
if n >= 400:
    s += 'CD'*int(n/400)
    n %= 400
if n >= 100:
    s += 'C'*int(n/100)
    n %= 100
if n >= 90:
    s += 'XC'*int(n/90)
    n %= 90
if n >= 50:
    s += 'L'*int(n/50)
    n %= 50
if n >= 40:
    s += 'XL'*int(n/40)
    n %= 40
if n >= 10:
    s += 'X'*int(n/10)
    n %= 10
if n >= 9:
    s += 'IX'*int(n/9)
    n %= 9
if n >= 5:
    s += 'V'*int(n/5)
    n %= 5
if n >= 4:
    s += 'IV'*int(n/4)
    n %= 4
if n >= 1:
    s += 'I'*int(n/1)
    n %= 1
print(s)