import time

a = [1,2,3,4,5]

def calc(lst):
    res = {}
    for item in lst:
        res.update({str(item): item*item})
    return res


lst = range(30)

result = calc(lst)


print(result)
