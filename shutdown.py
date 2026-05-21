def shutdown(y):
    print("shutting down")
def ashutdown(a):
    print("abort shutdown")
def smt(c):
    print("Sorry. Unvalid answer")
txt = str(input(" Is Shut down possible? Enter in lowercaps: "))
if txt == "yes":
    print(shutdown(txt))
elif txt == "no":
    print(ashutdown(txt))
else:
    print(smt(txt))