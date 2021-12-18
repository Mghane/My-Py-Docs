num = []
for x in range(2,800):
    d = list(range(2,x))
    if 0 not in [x%y for y in d]:
        num.append(x)


def get_prime_factor(a):
    factor = []
    while a >1:
        b = num[[a%x for x in num].index(0)]
        factor.append(b)
        a = a//b
    print(factor)

get_prime_factor(723)


###########################################
def get_prime_number2(a):
    factor = []
    devisor = 2
    while devisor<=a:
        if a%devisor ==0:
            factor.append(devisor)
            a = a//devisor
        else:
            devisor +=1
    print(factor)

get_prime_factor(723)
get_prime_number2(723)