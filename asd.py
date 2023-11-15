# class Solution:
def romanToInt(s: str) -> int:
    sym = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        "M":1000
    }

    c = 0
    ls = []
    for i in range(len(s)):
        if s[i] in sym.keys():
            for k, v in sym.items():
                if s[i] == k:
                    ls.append(v)
                    # c += v

                    # try:
                    #     if s[i] < s[i+1]:
                    #         ls.append(k)
                    #         c += v
                    #     else:
                    #         ls.append('-'+k)
                    #         c += -v
                    # except:
                    #     print('propusk', s[i])
    b = []
    print(ls)
    ls = ls[::-1]
    print(ls)
    for a in range(len(ls)):
        try:
            if ls[a] > ls[a+1]:
                p = ls[a+1] * (-1)
                ls[a+1] = p
                b.append(ls[a])
            else:
                b.append(ls[a])
        except:
            print('s')
            b.append(ls[-1])
    print(sum(b))
    return ls, c, #sum(ls)

print(romanToInt('III'))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))




#fnasjnfajsnfjasnfjnasjfnajsnfjansjnf GIT