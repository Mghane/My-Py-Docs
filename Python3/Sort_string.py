a = "hello world who are You Today"
def sort_string(a):
    lis = a.split()
    mydict = dict(zip(lis,[ord(x[0].lower()) for x in lis]))
    print(" ".join(sorted(mydict, key=mydict.__getitem__)))


sort_string(a)