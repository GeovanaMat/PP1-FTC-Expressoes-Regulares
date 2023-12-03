import re

def validarIndetifcadorCPF(ident,data):
    i = 0
    v1 = 0
    v2 = 0
    vetInvert = []
    for dig in data[ident.start(): ident.end()]:
        if(re.match(r"[0-9]",dig)):
            vetInvert.append(dig)
    vetInvert.reverse()
    for numbers in vetInvert[2:11]:

            v1 = v1 + int(numbers) * (9 - (i % 10))
            v2 = v2 + int(numbers) * (9 -(i + 1) % 10)
            i = i + 1

    v1 = (v1 % 11) % 10
    v2 = v2 + (v1 * 9)
    v2 = (v2 % 11) % 10
    if(v1 == int(vetInvert[1]) and v2 == int(vetInvert[0])):
        return True
    else:
        return False

def validarIdentificadorCNPJ(ident,data):
    
    return








dataA = input("Coloca ai: ")
findCPF = re.search(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}",dataA)
findCNPJ = re.search(r"[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}\-[0-9]{2}", dataA)
if(findCPF != None):
    print(validarIndetifcadorCPF(findCPF,dataA))
elif(findCNPJ != None):
    print(validarIdentificadorCNPJ(findCNPJ,dataA))
else:
    print(False)




findEmail = re.findall(r"^[a-zA-Z][\w\.-]+@[\w]+\.[\w]+",dataA)
findTelefone = re.findall(r"\+55\([0-9]{2}\)[0-9]{4}\-[0-9]{4}",dataA)
findChRapida = re.findall(r"[0-9A-Fa-f][0-9A-Fa-f]\.[0-9A-Fa-f][0-9A-Fa-f]\.[0-9A-Fa-f][0-9A-Fa-f]\.[0-9A-Fa-f][0-9A-Fa-f]",dataA)
ChavesA = []

