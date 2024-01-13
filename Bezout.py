old_function = "x^4+2x^3-5x^2+2x-3"
index_insert = 0
def Bezout(old_function, x0):
    #analiza wzoru funkcji:
    index_insert = 0
    function = old_function[:index_insert] + " " + old_function[index_insert:]
    wspol = []
    h = []
    result = 0
    stopien = function[3]
    for i in range(len(function)):
        if function[i] != "x" and function[i] != "+":
            h.append(function[i])
        if function[i] == " " or (function[i] == "x" and (function[i - 1] == "+" or function[i - 1] == "-")):
            h.append("1")
    for j in range(len(h)):
        if h[j] == "^":
            h[j] = 0
            h[j + 1] = 0
        if h[j] == "-":
            h[j+1] = -int(h[j+1])
            h[j] = 0
    for x in h:
        if x == " " or x == 0:
            pass
        else:
            wspol.append(x)
    wspol = list(map(int, wspol))
    #obliczanie reszty
    n = len(wspol)-1
    print(wspol)
    for i in range(0, n+1):
        print(n-i)
        result += (x0**(n-i))*wspol[i]
    if result == 0:
        return "x0 jest pierwiastkiem funkcji f(x)"
    elif result != 0:
        return result

print(Bezout(old_function, 3))
