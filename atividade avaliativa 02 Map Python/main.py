# Exemplo : Multiplicar por dois cada valor de uma lista


numeros1 = [ 10 , 20, 30]

def dobro( p ):
    return p * 2

novosNumeors = map( dobro, numeros1 )
print( list(novosNumeors) )

