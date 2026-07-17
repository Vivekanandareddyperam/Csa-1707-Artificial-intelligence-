from itertools import permutations
letters = "SENDMORY"
for p in permutations("0123456789", len(letters)):
    d = dict(zip(letters, map(int, p)))
    if d['S'] == 0 or d['M'] == 0:
        continue
    send = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
    more = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
    money = 10000*d['M'] + 1000*d['O'] + 100*d['N'] + 10*d['E'] + d['Y']
    if send + more == money:
        print("Solution Found:")
        print("SEND  =", send)
        print("MORE  =", more)
        print("MONEY =", money)
        print("\nLetter Values:")
        for ch in letters:
            print(ch, "=", d[ch])
        break