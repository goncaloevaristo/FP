# Gonçalo Manuel Bolinhas Evaristo - ist187532
# Fundamentos de Programação - Projeto 1
################################
# 1) Correcção da documentação #
################################
# 1.2.1
def corrigir_palavra(cadeia):
    """
    Esta função recebe uma cadeia de caracteres que representa uma palavra e devolve
    a sequência de caracteres após a correcção ser feita. (Caso existam dois caracteres iguais
    seguidos, sendo um maiúsculo e outro minúsculo, apaga ambos).
    """
    cad = list(cadeia)  # transformar string numa lista para poder apagar os caracteres
    i = 1
    while i < len(cad):  # percorrer a lista
        if cad[i].upper() == cad[i - 1] or cad[i - 1].upper() == cad[i]:  # comparar caracter de indice i com o de i - 1
            if cad[i] != " " and cad[i - 1] != " ":  # se ambos não forem um espaço em branco
                del cad[i], cad[i - 1]  # apaga ambos
                i = 0
        i = i + 1
    return "".join(cad)  # junta todos os items da lista numa string


# 1.2.2
def eh_anagrama(palavra1, palavra2):
    """
    Esta função recebe duas cadeias de caracteres correspondentes a duas palavras e devolve
    um valor lógico (True or False) se uma palavra é anagrama da outra.
    """
    return sorted(palavra1.lower()) == sorted(palavra2.lower())  # transformar as maiúsculas e ordena as letras


# 1.2.3
def corrigir_doc(doc):
    """
    Esta função é a junção das últimas duas funções, isto é, recebe uma cadeia de caracteres
    correspondente a uma frase e devolve a frase após serem feitas duas correcções: uma para
    retirar os surtos de letras (1.2.1) e outra para retirar os anagramas(1.2.2), só ficando
    com a sua segunda ocorrência. Esta função também verifica a validade dos argumentos,
    devolvendo erro caso estes não sejam válidos.
    """
    if not isinstance(doc, str):
        raise ValueError("corrigir_doc: argumento invalido")
    lst1 = list(corrigir_palavra(doc))
    indice_car = 0
    while indice_car != len(lst1):
        if lst1[indice_car].isalpha() or lst1[indice_car] == " ":  # verifica se é letra ou espaço
            if lst1[indice_car] == " " and lst1[indice_car + 1] == " ":  # verifica se há dois espaços consecutivos
                raise ValueError("corrigir_doc: argumento invalido")
            indice_car = indice_car + 1
        else:
            raise ValueError("corrigir_doc: argumento invalido")
    lst_palavra = ''.join(lst1).split()  # junta as letras todas, formando palavras
    i, j = 0, 0
    if len(lst_palavra) < 1:
        raise ValueError("corrigir_doc: argumento invalido")
    while i < len(lst_palavra):  # fica na palavra de índice i
        while j < len(lst_palavra):  # percorre as palavras uma segunda vez para se poder comparar
            if eh_anagrama(lst_palavra[i], lst_palavra[j]) and (lst_palavra[i].lower()) != (lst_palavra[j].lower()):
                del lst_palavra[j]
            j = j + 1
        j = 0  # depois da palavra i ter sido comparada com todas, retorna-se ao início da lista de palavras
        i = i + 1  # troca-se de palavra
    return ' '.join(lst_palavra)  # junta todas as palavras todas da lista, formando uma string


########################
# 2) Descoberta do PIN #
########################
# 2.2.1
def obter_posicao(tecla, posicao):
    """
    Esta função recebe um caractere, que representa o movimento a ser feito (C,B,E,D), e um
    número, de 1 a 9, que representa a posição inicial no teclado. O retorno desta função é a
    posição após o movimento ser feito.
    """
    pos = 0
    if tecla == "C":
        if posicao <= 3:
            return posicao
        pos = posicao - 3
    if tecla == "B":
        if posicao >= 7:
            return posicao
        pos = posicao + 3
    if tecla == "E":
        if posicao == 1 or posicao == 4 or posicao == 7:
            return posicao
        pos = posicao - 1
    if tecla == "D":
        if posicao == 3 or posicao == 6 or posicao == 9:
            return posicao
        pos = posicao + 1
    return pos


# 2.2.2
def obter_digito(cadeia, posicao):
    """
    Esta função baseia-se em repetir a função anterior para a cadeia de caracteres apresentada
    pelo utilizador, isto é, vai-se fornecer uma cadeia de caracteres e uma posição inicial, e o
    retorno da função é a posição final após os movimentos representados na cadeia serem feitos.
    """
    i = 0
    while i != len(cadeia):
        posicao = obter_posicao(cadeia[i], posicao)
        i = i + 1
    return posicao


# 2.2.3
def obter_pin(t):
    """
    Esta função vai receber um tuplo constituído por várias cadeias de caracteres e vai
    devolver o pin, num tuplo (cada cadeia de caracteres, após ser processada, irá representar
    um número no pin). A posição inicial é 5 e após ser transformada a primeira cadeia de
    caracteres, a posição inicial para a cadeia a seguir é sempre igual à posição traduzida
    pela transformação da cadeia anterior (se a primeira cadeia,començando na posição 5, for
    transformada na posição 9, a segunda cadeia irá começar na posição 9). Esta função também
    verifica a validade dos argumentos, devolvendo erro caso estes não sejam válidos.
    """
    i, j = 0, 0
    cadeia = ()
    posicao = 5
    if not isinstance(t, tuple):
        raise ValueError("obter_pin: argumento invalido")
    if len(t) < 4 or len(t) > 10:
        raise ValueError("obter_pin: argumento invalido")
    while i != len(t):
        if len(t[i]) < 1:  # verificação dos argumentos
            raise ValueError("obter_pin: argumento invalido")
        while j != len(t[i]):
            if t[i][j] not in "CEDB":
                raise ValueError("obter_pin: argumento invalido")
            posicao = obter_digito(t[i][j], posicao)
            j = j + 1
        cadeia = cadeia + (posicao,)
        j = 0
        i = i + 1
    return cadeia


###########################
# 3) Verificação de dados #
###########################
# 3.2.1 e 4.2.1
"""
Esta função vai receber um argumento e vai retornar um valor lógico conforme se verifique ou não
a validade do mesmo (ser um tuplo de 3 entradas: uma cifra, uma sequência de controlo e uma
sequência de segurança).
"""


def eh_entrada(tuplo1):
    if isinstance(tuplo1, tuple) and len(tuplo1) == 3 and isinstance(tuplo1[0], str) and isinstance(tuplo1[1], str) \
            and isinstance(tuplo1[2], tuple):
        if len(tuplo1[1]) == 7 and len(tuplo1[2]) >= 2 and tuplo1[1][0] == "[" and tuplo1[1][6] == "]":
            k = 0
            while k != len(tuplo1[2]):
                if not isinstance(tuplo1[2][k], (float, int)) or tuplo1[2][k] < 0:
                    return False
                k = k + 1
            j = 1
            while j != 6:
                if "a" <= tuplo1[1][j] <= "z":  # verificação da validade dos argumentos
                    j = j + 1
                else:
                    return False
                i = 0
                while i != len(tuplo1[0]):
                    if "a" <= tuplo1[0][i] <= "z" or (tuplo1[0][i] == "-" and tuplo1[0][i + 1] != "-"):
                        i = i + 1
                    else:
                        return False
                return True
    return False


# 3.2.2
def validar_cifra(cifra, cad):
    """
    Esta função recebe duas cadeias de caracteres, uma cifra e uma cadeia de controlo. Vai
    devolver um valor lógico conforme se verifique ou não a coerência entre a cifra e a cadeia de
    controlo. (A cadeia de controlo deve ter os argumentos ordenados por ordem de ocorrência e depois
     por ordem alfabética).
    """
    lista = list(cifra)
    i = 0
    while i != len(lista):
        if lista[i] == "-":
            del lista[i]
        i = i + 1
    d = {x: lista.count(x) for x in lista}  # criar um dicionário
    x = sorted(d.items())  # ordenar por ordem alfabética
    i = 0
    while i != len(x):
        if x[i - 1][1] < x[i][1]:
            x[i], x[i - 1] = x[i - 1], x[i]  # trocar os elementos para ordenar por ordem de ocorrência decrescente
            i = 0
        elif x[i - 1][1] == x[i][1]:
            if ord(x[i - 1][0]) > ord(x[i][0]):
                x[i], x[i - 1] = x[i - 1], x[i]
                i = 0
        i = i + 1
    i, checksum = 0, ""
    while i != 5:
        checksum = checksum + x[i][0]
        i = i + 1
    return "[" + checksum + "]" == cad  # devolver o valor lógico


# 3.2.3
def filtrar_bdb(lista):
    """
    Esta função vai receber uma lista de entradas BDB e irá verificar numa primeira fase se as
    entradas estão de acordo com os argumentos pedidos (3.2.1). Em última instância irá verificar
    se a cifra e a cadeia de controlo estão coerentes entre si (3.2.2) e o programa irá retornar
     as entradas que falhem nesta última verificação.
    """
    if not isinstance(lista, list):
        raise ValueError("filtrar_bdb: argumento invalido")
    elif len(lista) < 1:
        raise ValueError("filtrar_bdb: argumento invalido")  # verificação da validade dos argumentos da lista
    j, i = 0, 0
    while j != len(lista):
        if not isinstance(lista[j], tuple) or len(lista[j]) < 1:
            raise ValueError("filtrar_bdb: argumento invalido")
        j = j + 1
    while i != len(lista):
        if validar_cifra(lista[i][0], lista[i][1]):  # chamar a função para verificar a validade dos argumentos da cifra
            del lista[i]  # e da cadeia de controlo
        else:
            i = i + 1
    return lista


##############################
# 4) Desencriptação de dados #
##############################
# 4.2.2
def obter_num_seguranca(tpl):
    """
    Esta função irá receber um tuplo constituído por números e irá retornar a menor diferença entre
    qualquer par de números.
    """
    i, j = 0, 0
    sub = ()
    while i != len(tpl):  # percorrer o tuplo de números, escolhendo o primeiro
        while j != len(tpl):  # voltar a percorrer o tuplo para poder fazer as subtrações
            subtracao = tpl[i] - tpl[j]
            if subtracao > 0:
                sub = sub + (subtracao,)  # acrescentar o valor da subtração a um novo tuplo
            j = j + 1
        j = 0  # após fazer a subtração para a primeira iteração, voltar ao início da lista
        i = i + 1  # passar para o próximo número
    return sorted(sub)[0]  # devolver o número mais pequeno, que deverá ser o primeiro numa lista com ordem crescente


# 4.2.3
def decifrar_texto(str1, tpl):
    """
    Esta função irá receber uma cadeia de caracteres e um número de segurança e irá devolver a
    respetiva cadeia de caracteres, já descodificada. A descodificação ocorre ao percorrer cada letra
    da cadeia n vezes, sendo n igual ao número de segurança. De salientar que, caso a letra esteja
    numa posição par, avança uma posição, e caso seja impar recua uma. (Por exemplo  se "t" estiver
    na posição 7, irá passar a "s".
    """
    i = 0
    lst1 = list(str1)
    while i != len(lst1):
        passo = tpl % 26  # há 26 letras no alfabeto, se usarmos o resto da divisão escusamos de percorrer o
        if lst1[i] == "-":  # alfabeto tantas vezes caso o número seja grande
            lst1[i] = " "
        else:
            if i % 2 == 0:
                lst1[i] = chr(ord(lst1[i]) + 1)  # se for par passa para a letra seguinte
            else:
                lst1[i] = chr(ord(lst1[i]) - 1)  # se for impar vai para a letra anterior

            if passo + ord(lst1[i]) <= 122:
                lst1[i] = chr(passo + ord(lst1[i]))  # caso a soma do passo com a letra seja menor ou igual a 122 (valor
            else:  # da última letra no alfabeto), troca-se a letra na lista
                lst1[i] = chr(passo + ord(lst1[i]) - 26)  # caso seja maior, tem de se voltar ao príncipio do alfabeto
        i = i + 1
    return ''.join(lst1)


# 4.2.4
def decifrar_bdb(lista):
    """
    Esta função é um agregado das últimas funções (4.2.1, 4.2.2 e 4.2.3). O programa vai uma lista de
    um ou mais tuplos e vai correr as três funções: verificar se são entradas válidas, calcular o
    número de segurança e proceder à descodificação utilizando o mesmo. O retorno da função será uma
    lista das cadeias de caracteres já descodificadas.
    """
    lst1 = []
    i = 0
    if not isinstance(lista, list):
        raise ValueError("decifrar_bdb: argumento invalido")  # verificação de argumentos
    while i != len(lista):
        if eh_entrada(lista[i]):  # chama a função 4.2.1 para verificar a validade da entrada
            lst1 = lst1 + [decifrar_texto(lista[i][0], obter_num_seguranca(lista[i][2])), ]
        else:  # chama 4.2.2 e 4.2.3 para
            raise ValueError("decifrar_bdb: argumento invalido")  # fazer a descodificação do
        i = i + 1  # texto
    return lst1


##########################
# 5) Depuração de senhas #
##########################
# 5.2.1
def eh_utilizador(dicionario):
    """
    Esta função recebe um dicionário constituído por 3 elementos: nome, senha e regra individual.
    A função irá verificar se os argumentos de cada um destes elementos está de acordo com o estipulado
    e irá devolver um resultado lógico.
    O nome e a senha devem ser do tipo string, devem ter pelo menos um caractere.
    A regra individual deve ser do tipo dictionary e uma das chaves, "vals", deve ser um tuplo de
    dimensão 2 e esse tuplo deve estar ordenado de forma crescente. A outra chave, "char", deve ser
    uma string e deve apenas conter uma letra como elemento.
    """
    if isinstance(dicionario, dict) and len(dicionario) == 3 and type(dicionario["name"]) == str and \
            len(dicionario["name"]) > 1 and type(dicionario["pass"]) == str and isinstance(dicionario["rule"], dict) \
            and len(dicionario["rule"]) == 2 and isinstance(dicionario["rule"]["char"], str) and \
            type(dicionario["rule"]["vals"]) == tuple and \
            0 < dicionario["rule"]["vals"][0] < dicionario["rule"]["vals"][1] and dicionario["rule"]["vals"][1] > 0 \
            and len(dicionario["rule"]["char"]) == 1:  # verificação de argumentos
        return True
    return False


# 5.2.2
def eh_senha_valida(cadeia, regra):
    """
    Esta função recebe uma cadeia de caracteres e um dicionário. A função irá avaliar a coerência
    entre a cadeia e as regras pertencentes ao dicionário e irá retornar o valor lógico.
    As regras que se têm de verificar para além das impostas no dicionário são a presença de  pelo
    menos três vogais minúsculas e a aparição de um caractere repetido seguido pelo menos uma vez.
    As regras impostas no dicionário são que o caractere presente em "char" tem de aparecer pelo menos n
    vezes e no máximo m vezes, sendo (n,m) discriminados no tuplo presente em "vals".
    """
    i, contador_letra, contador_vogais, repeticoes = 0, 0, 0, 0
    while i != len(cadeia):
        if (cadeia[i] == cadeia[i - 1]) and i >= 1:
            repeticoes = 1
        if cadeia[i] == "a" or cadeia[i] == "e" or cadeia[i] == "i" or cadeia[i] == "o" or cadeia[i] == "u":
            contador_vogais = contador_vogais + 1
        if regra["char"] == cadeia[i]:  # verificação da validade dos argumentos
            contador_letra = contador_letra + 1
        i = i + 1
    return (regra["vals"][0] <= contador_letra <= regra["vals"][1]) and (contador_vogais >= 3) and repeticoes == 1


# 5.2.3
def filtrar_senhas(lista):
    """
    Esta função é um conjunto das últimas duas: vai receber uma lista de dicionário e, em primeira
    instância, irá avaliar se os dicionários são entradas válidas quanto aos tipo de argumentos. Em
    último lugar irá verificar se as regras impostas são cumpridas. Por fim, serão apresentados sob a
    forma de lista por ordem alfabética os nomes dos utilizadores (presente nos dicionários na chave
    "name") que não cumpriram com as regras.
    """
    if type(lista) != list or len(lista) < 1:
        raise ValueError("filtrar_senhas: argumento invalido")
    listaf = []
    j = 0
    while j != len(lista):
        if type(lista[j]) != dict:
            raise ValueError("filtrar_senhas: argumento invalido")
        elif eh_utilizador(lista[j]):
            if eh_senha_valida(lista[j]["pass"], lista[j]["rule"]):
                del lista[j]
                j = 0
            else:
                j = j + 1
    for x in range(len(lista)):
        listaf = listaf + [lista[x]["name"], ]
    return sorted(listaf)
