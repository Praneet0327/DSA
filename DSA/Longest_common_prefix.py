strs = ["flower","flow","flight"]
strs.sort()
l = min(len(strs[0]), len(strs[-1]))
s = ""
count=0

for i in range(0,l):
    if strs[0][i] != strs[-1][i]:
        break
    count+=1

print(strs[0][:count])
    