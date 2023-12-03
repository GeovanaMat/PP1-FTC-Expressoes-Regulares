import re


def validarIndetifcadorCPF(ident, data):
    if ident is None:
        return True
    if re.match(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}", ident.string) is None:
        return False
    i = 0
    v1 = 0
    v2 = 0
    vetInvert = []
    for dig in data[ident.start(): ident.end()]:
        if re.match(r"[0-9]", dig):
            vetInvert.append(dig)
    vetInvert.reverse()
    for numbers in vetInvert[2:11]:
        v1 = v1 + int(numbers) * (9 - (i % 10))
        v2 = v2 + int(numbers) * (9 - (i + 1) % 10)
        i = i + 1

    v1 = (v1 % 11) % 10
    v2 = v2 + (v1 * 9)
    v2 = (v2 % 11) % 10
    if (v1 == int(vetInvert[1]) and v2 == int(vetInvert[0])):
        return True
    else:
        return False


def validaridentcnpj(ident, data):
    if ident is None:
        return True
    if re.match(r"[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}", ident.string) is None:
        return False
    numberVerif = []
    v1 = 0
    v2 = 0
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
        if re.match(r"^[a-zA-Z][\w._]*@[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+", item) is None:
            return False
        return True


def validartelefone(list_telefones):
    for telefones in list_telefones:
        if re.match(r"\+55\([0-9]{2}\)[0-9]{4}-[0-9]{4}", telefones) is None:
            return False
    return True


def validadarchrapida(lista_ch):
    i = 0
    for item in lista_ch:
        if re.match(r"[A-Fa-f0-9]{2}.[A-Fa-f0-9]{2}.[A-Fa-f0-9]{2}.[A-Fa-f0-9]{2}", item) is None:
            print("nao deu")
            return False
    for item in lista_ch:
        for i in range(0, 10, 3):
            if re.match(r"[A-Fa-f]", item[i]):
                if re.match(r"[A-Fa-f]", item[i + 1]):
                    return False
            if re.match(r"[0-9]", item[i]):
                if item[i + 1] == item[i]:
                    return False
    return True


dataA = "0"

while dataA != "==========":

    dataA = input("Coloca ai: ")
    findCPF = re.search(
        r"[\w.*}{,^?~=+\-_/|]{3}\.[\w.*}{,^?~=+\-_/|]{3}\.[\w.*}{,^?~=+\-_/|]{3}-[\w.*}{,^?~=+\-_/|]{2}",
        dataA)
    findCNPJ = re.search(r"[\w.*}{,^?~=+\-_/|]{2}\.[\w.*}{,^?~=+\-_/|]{3}\.[\w.*}{,^?~=+\-_/|]{3}"
                         r"/[\w.*}{,^?~=+\-_/|]{4}-[\w.*}{,^?~=+\-_/|]{2}", dataA)
    findEmail = re.findall(r"[\w.*}{,^?~=+\-_/|]+@[\w.*}{,^?~=+\-_/|]+", dataA)
    findTelefone = re.findall(r"\+55\([\w.*}{,^?~=+\-_/|]{2}\)[\w.*}{,^?~=+\-_/|]{4}-[\w.*}{,^?~=+\-_/|]{4}", dataA)
    findChRapid = re.findall(r"[\w.*}{,^?~=+\-_/|]{2}\.[\w.*}{,^?~=+\-_/|]{2}\."
                             r"[\w.*}{,^?~=+\-_/|]{2}\.[\w.*}{,^?~=+\-_/|]{2}", dataA)

    if (validaremail(findEmail) and validadarchrapida(findChRapid) and validarIndetifcadorCPF(findCPF,dataA)
            and validartelefone(findTelefone) and validaridentcnpj(findCNPJ,dataA) is True):

        print(validaremail(findEmail))
        print(validartelefone(findTelefone))
        print(validarIndetifcadorCPF(findCPF, dataA))
        print(validaridentcnpj(findCNPJ, dataA))
        print(validadarchrapida(findChRapid))
        print(True)
    else:
        print(False)
