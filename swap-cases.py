def swap_case(s):
    y = []
    for i in range(len(s)):
        if s[i].isupper():
            y.append(s[i].lower())
        elif s[i].islower():
            y.append(s[i].upper())
        else:
            y.append(s[i])
    z = "".join(y)
    return z

if __name__ == '__main__':
    s = input()
    print(swap_case(s))