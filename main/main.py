import re

findEmail = None
findCNPJ = None
findChRapid = None
findTelefone = None
findCPF = None


def verificarformato(vetData):
    if not vetData:
        return False
    if re.match(r"[R$]", vetData[2]) is None:
        return False

    if re.match(r"^[1-9]\d{0,2}(\.\d{3})*,\d{2}$", vetData[3]) is None:
        return False

    if re.match(r"[0-9]{2}/[0-9]{2}/[0-9]{4}", vetData[4]) is None:
        return False
    else:
        dia, me, ano = vetData[4].split("/")
        if dia > "31":
            return False
        if me > "12":
            return False
        if ano < "0001":
            return False
    if re.match(r"[0-9]{2}:[0-9]{2}", vetData[5]) is None:
        return False

    else:
        horavet = vetData[5].split(":")
        if int(horavet[0]) > 23 or int(horavet[1]) > 59:
            return False
    if len(vetData[6]) != 12:
        return False
    elif len(re.findall(r"[A-Z]", vetData[6])) != 3:
        return False
    elif len(re.findall(r"[a-z]", vetData[6])) != 3:
        return False

    elif len(re.findall(r"[0-9]", vetData[6])) != 4:
        return False

    elif len(re.findall(r"[$@%()*]", vetData[6])) != 2:

        return False
    return True


def verificarChaves(vetData, lista_pix):
    v1 = None
    v2 = None

    for item in lista_pix:
        for chave in item:
            if chave == vetData[0]:
                v1 = lista_pix.index(item)
            if chave == vetData[1]:
                v2 = lista_pix.index(item)
    if v1 == v2:
        return False
    elif v1 is None:
        return False
    elif v2 is None:
        return False
    return True


def validarindetifcadorcpf(ident, data):
    if ident is None:
        return False
    if re.match(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}", ident.string) is None:
        return False
    i1 = 0
    v1 = 0
    v2 = 0
    vetInvert = []
    for dig in data[ident.start(): ident.end()]:
        if re.match(r"[0-9]", dig):
            vetInvert.append(dig)
    vetInvert.reverse()
    for numbers in vetInvert[2:11]:
        v1 = v1 + int(numbers) * (9 - (i1 % 10))
        v2 = v2 + int(numbers) * (9 - (i1 + 1) % 10)
        i1 = i1 + 1

    v1 = (v1 % 11) % 10
    v2 = v2 + (v1 * 9)
    v2 = (v2 % 11) % 10
    if v1 == int(vetInvert[1]) and v2 == int(vetInvert[0]):
        return True
    else:
        return False


def validaridentcnpj(ident, data):
    if ident is None:
        return False
    if re.match(r"[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}", ident.string) is None:
        return False
    numberVerif = []

    for number in data[ident.start():ident.end()]:
        if re.match(r"[0-9]", number):
            numberVerif.append(int(number))
    v1 = 5 * numberVerif[0] + 4 * numberVerif[1] + 3 * numberVerif[2] + 2 * numberVerif[3]
    v1 += 9 * numberVerif[4] + 8 * numberVerif[5] + 7 * numberVerif[6] + 6 * numberVerif[7]
    v1 += 5 * numberVerif[8] + 4 * numberVerif[9] + 3 * numberVerif[10] + 2 * numberVerif[11]
    v1 = 11 - v1 % 11
    if v1 >= 10:
        v1 = 0
    v2 = 6 * numberVerif[0] + 5 * numberVerif[1] + 4 * numberVerif[2] + 3 * numberVerif[3]
    v2 += 2 * numberVerif[4] + 9 * numberVerif[5] + 8 * numberVerif[6] + 7 * numberVerif[7]
    v2 += 6 * numberVerif[8] + 5 * numberVerif[9] + 4 * numberVerif[10] + 3 * numberVerif[11]
    v2 += 2 * numberVerif[12]
    v2 = 11 - v2 % 11
    if v2 >= 10:
        v2 = 0
    if v1 == numberVerif[12] and v2 == numberVerif[13]:
        return True
    else:
        return False


def validaremail(emails):
    if emails is None:
        return True
    for item in emails:
        if re.match(r"^[a-zA-Z][a-zA-Z0-9]*@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+", item) is None:
            return False
    return True


def validartelefone(list_telefones):
    if list_telefones is None:
        return True
    for telefones in list_telefones:
        if re.match(r"\+55\([0-9]{2}\)[0-9]{4}-[0-9]{4}", telefones) is None:
            return False
    return True


def validadarchrapida(lista_ch):
    if not lista_ch:
        return True
    for item in lista_ch:
        if re.match(r"[A-Fa-f0-9]{2}.[A-Fa-f0-9]{2}.[A-Fa-f0-9]{2}.[A-Fa-f0-9]{2}", item) is None:
            return False
    for item in lista_ch:
        for i2 in range(0, 10, 3):
            if re.match(r"[A-Fa-f]", item[i2]):
                if re.match(r"[A-Fa-f]", item[i2 + 1]):
                    return False
            if re.match(r"[0-9]", item[i2]):
                if item[i2 + 1] == item[i2]:
                    return False
    return True


dataA = ""
lista_chpix = []
digverf = True

while dataA != "==========":
    dataA = input()
    if dataA != "==========":

        findCPF = re.search(r"\d{3}\.\d{3}\.\d{3}-\d{2}", dataA)

        findCNPJ = re.search(r"[\w.*}{,^?~=+\-_/|]{2}\.[\w.*}{,^?~=+\-_/|]{3}\.[\w.*}{,^?~=+\-_/|]{3}"
                             r"/[\w.*}{,^?~=+\-_/|]{4}-[\w.*}{,^?~=+\-_/|]{2}", dataA)
        findEmail = re.findall(r"\S+@[\w.*}{,^?~=+\-_/|]+", dataA)

        findTelefone = re.findall(r"\+55\([\w.*}{,^?~=+\-_/|]{2}\)[\w.*}{,^?~=+\-_/|]{4}-[\w.*}{,^?~=+\-_/|]{4}",
                                  dataA)
        findChRapid = re.findall(r"[\w.*}{,^?~=+\-_/|]{2}\.[\w.*}{,^?~=+\-_/|]{2}\."
                                 r"[\w.*}{,^?~=+\-_/|]{2}\.[\w.*}{,^?~=+\-_/|]{2}", dataA)

        print(validaridentcnpj(findCNPJ, dataA))
        print(validarindetifcadorcpf(findCPF, dataA))
        print(validaremail(findEmail))
        print(validartelefone(findTelefone))
        print(validadarchrapida(findChRapid))

        if validaridentcnpj(findCNPJ, dataA) is True:
            if validaremail(findEmail) is False:
                digverf = False
            if validartelefone(findTelefone) is False:
                digverf = False
            if validadarchrapida(findChRapid) is False:
                digverf = False
        elif validarindetifcadorcpf(findCPF, dataA) is True:
            if validaremail(findEmail) is False:
                digverf = False
            if validadarchrapida(findChRapid) is False:
                digverf = False
            if validartelefone(findTelefone) is False:
                digverf = False
        else:
            digverf = False

        vetDataA = dataA.split(" ")
        lista_chpix.append(vetDataA)
        print("digverf" + str(digverf))

dig_final = True

try:
    while True:

        dataB = input()
        vetDataB = dataB.split(" ")
        if verificarChaves(vetDataB, lista_chpix) is False:
            dig_final = False
        if verificarformato(vetDataB) is False:
            dig_final = False
        if digverf is False:
            dig_final = False

except EOFError:
    print(dig_final)
