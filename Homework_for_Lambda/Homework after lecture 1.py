def minimum(a,b,c):
    if a < b and b < c:
        return a
    elif a > b and b > c:
        return c
    else:
        return b
'''Или можно просто сделать 
return min(a,b,c)
Но так как у нас курс с самого начала, то и оперируем знаниями которые 
были даны на первой лекции'''

def comp(a,b,c):
    if a == b and b == c:
        return 3
    elif (a == b and b != c) or (a != b and b == c) or (a == c and b != c):
        return 2
    else:
        return 0


def summ(lst):
    s = 0
    for i in lst:
        s += i
    return s
'''Или return sum(lst)'''


def zero_lst(lst):
    count = 0
    for i in lst:
        if i == 0:
            count += 1 
    return count             

a = 5
b = 5
c = 3
lst = [0, 10, 11, 12, 13, 0, 8, 5, 9, 0]
print(minimum(a,b,c))
print(comp(a,b,c))
print(summ(lst))
print(zero_lst(lst))