"""
A formatação de strings serve para inserirmos variaveis no meio de strings, 
de forma a não ser necessaria concatenação.
"""


"""
FORMATAÇÃO UTILIZANDO 'f'
"""
strNome = "Hadrian"
floatNumero = 2.12345

#Exemplo de string concatenada
strExemploConcatenado = "Me chamo "+strNome

#Exemplo de string formatada
strExemploFormatado = f"Me chamo {strNome}"

#Exemplo de casas decimais
strNumero2casas = f"O numero {floatNumero:.2f} tem 2 casas decimais"

print(strExemploConcatenado)
print(strExemploFormatado)
print(strNumero2casas)

"""
FORMATAÇÃO UTILIZANDO 'format'

Tudo em Python é um objeto, e um objeto tem metodos.
Um dos metodos da 'string' é o 'format'
"""
a = "A"
b = "B"
c = 1.1

#Format sendo utilizado na ordem dos parametros
formato = "a={} b={} c={:.2f}".format(a,b,c)

print(formato)

#Format sendo utilizado com os indices dos parametros
formato = "b={1} c={2:.2f} a={0}".format(a,b,c)

#Format sendo utilizado com os parametros sendo nomeados
formato = "c={nomeC:.2f} a={nomeA} b={nomeB}".format(nomeA=a,nomeB=b,nomeC=c)

print(formato)