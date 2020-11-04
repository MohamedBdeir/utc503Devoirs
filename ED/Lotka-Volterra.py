a = 0.09
b =0.00001
c = 0.25
d = 0.000005

uDepart = 53000
pDepart = 9000

def uv(n, a = 0.09,b =0.00001,c = 0.25,d = 0.000005):
    if n:
        u1 = uv(n-1)
        v1 = uv(n-1)
        return (u1 * (1+a-b*v1), v1*(1-c+d*u1))
    else:
        return(uDepart, pDepart)



def unImperatif(n, a = 0.09,b =0.00001,c = 0.25,d = 0.000005):
    proie = uDepart
    predateur = pDepart

    i = 0
    while i<n:
        proie = proie * (1+a-b*pDepart)
        predateur = predateur * (1-c+d*uDepart)
        i+=1
    return(proie, predateur)


