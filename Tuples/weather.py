weathr = (1, 0, 1, 0, 1, 1, 0)
sun = 0
rain = 0
for i in range(0, 7):
    if(weathr[i]==0):
        rain += 1
    else:
        sun += 1

if (sun<rain):
    print("It is going to rain today!")
else:
    print("It is going to be sunny today!")