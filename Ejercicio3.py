def sumarDigitos(n):
    
    resultado=0
    while n>0:
        resultado+=n%10
        n//=10
    return (resultado)


def cifrarNumero(num):
    claveCifrado=sumarDigitos(num)
    claveCifrado= claveCifrado%10

    cont=1
    res=claveCifrado
    while num>0:
        res= (10**cont)*(((num%10)+claveCifrado)%10)+res
        print (res)
        cont+=1
        num = num//10
    descifrarNumero(res,claveCifrado)
    res = res/(10**cont)
    

    return res

    

def descifrarNumero(num,claveCifrado):
    num=num//10
    res=0
    cont=0
    while num>0:
        res = (10**cont)*((((num%10)-claveCifrado))+10)+res
        cont+=1
        num = num//10
    return res



    

cifrarNumero(77635245)
