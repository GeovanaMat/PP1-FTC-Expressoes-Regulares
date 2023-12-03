dataA = input("Coloca ai: ")
findCPF = re.findall(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}",dataA)
findCNPJ = re.findall(r"[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}\-[0-9]{2}", dataA)
findEmail = re.findall(r"^[a-zA-Z][\w\.-]+@[\w]+\.[\w]+",dataA)
findTelefone = re.findall(r"\+55\([0-9]{2}\)[0-9]{4}\-[0-9]{4}",dataA)
dataA = input("Coloca ai: ")
dataA = input()
dataA = input("Coloca ai: ")

numbersCPF = re.split(r"[0-9]", ident[0])
vetorCFP = numbersCPF[0:8]
for numbers in range(8):
    v1 = v1 + int(vetorCFP[numbers]) * (9 - (numbers % 10))
    v2 = v2 + int(vetorCFP[numbers]) * (9 - ((numbers + 1) % 10))

v1 = (v1 % 11) % 10
v2 = v2 + v1 * 9
v2 = (v2 % 11) % 10
if (v1 < v2):
    numbersCPF[9] == v1
    return print(True)
elif (v2 < v1):
    numbersCPF[9] == v2
    return print(True)
else:


    ;;;

    for dig in data:
        if(re.match(r"[0-9]",dig) != None and i < 9):
            print(dig)
            v1 = v1 + int(dig) * (9 - (i % 10))
            v2 = v2 + int(dig) * ((i+1) % 10)
            print("Valor v1", v1)
            i = i + 1
            print("Valor i : ", i)
    v1 = (v1 % 11) % 10
    v2 = v2 + v1*9
    v2 = (v2 %  11) % 10
    print(v1,v2)
