def val_parentheses(s):
    t = list(s)
    l = len(t)
    new_li = []
    i=0
    while i!=l:
        if len(new_li)==0 and (t[i]==')' or t[i]==']' or t[i]=='}'):
            return False
        if t[i]=='(' or t[i]=='{' or t[i]=='[':
            new_li.append(t[i])
            i+=1
            continue
        if t[i]==')':
            if new_li[-1] == '(':
                new_li.pop()
                i+=1
                continue
            else:
                return False
        if t[i]=='}':
            if new_li[-1] == '{':
                new_li.pop()
                i+=1
                continue
            else:
                return False
        if t[i]==']':
            if new_li[-1] == '[':
                new_li.pop()
                i+=1
                continue
            else:
                return False

    if len(new_li)==0:
        return True
    else:
        return False

s = "({]})"
val_parentheses(s)

