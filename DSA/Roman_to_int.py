s = "MCMXCIV"
d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
num = 0
i = 0
if len(s) == 1:
    print(d[s[0]])
else:
    while i < len(s)-1:
        if i > len(s)-1:
            break
        if d[s[i]]>=d[s[i+1]]:
            num = num+d[s[i]]
            i = i+1
        else:
            x = d[s[i+1]]-d[s[i]]
            num = num+x
            i = i+2

    if d[s[-2]] >= d[s[-1]]:
        num = num+d[s[-1]]

    print(num)
