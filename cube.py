def cube(num):
    return num*num*num
def div_3(num):
    if num %3 == 0:
        return cube(num)
    else:
        return False
print(div_3(12))
print(div_3(7))