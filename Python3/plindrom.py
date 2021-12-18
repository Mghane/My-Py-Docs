## Return  Yes if the string with alphabet items only, is a plindrom
def is_plindrom(a):
    a = "".join([x.lower() for x in a if x.isalpha()])
    flash = 'Yes'
    for i in range(len(a)//2):
        if a[i] != a[len(a)-1-i]:
            flash = 'No'
            break
    print(flash)
        
is_plindrom(a)

############################################
a = "r65A90./,c car 34 "

def is_plindrom2(a):
    import re
    a = "".join(re.findall('[a-z]+',a.lower()))
    print(a == a[::-1])

is_plindrom2(a)

