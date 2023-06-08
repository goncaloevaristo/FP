# Gonçalo Manuel Bolinhas Evaristo - ist187532
# Fundamentos de Programação - Projeto 2

#######################
# 2.1.1) TAD Posição  #
#######################

# Construtores
def cria_posicao(x, y):
    """
    cria posicao(x,y) recebe os valores correspondentes às coordenadas de uma
    posição e devolve a posiçãa correspondente. O construtor verifica a validade
    dos seus argumentos, gerando um ValueError com a mensagem ‘cria posicao:
    argumentos invalidos’ caso os seus argumentos não sejam válidos.
    """
    if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
        raise ValueError("cria_posicao: argumentos invalidos")
    return x, y


def cria_copia_posicao(p):
    return p[0], p[1]


# Seletores
def obter_pos_x(p):
    """
    obter_pos_x(p) devolve a componente x da posição p.
    """
    return p[0]


def obter_pos_y(p):
    """
    obter_pos_y(p) devolve a componente y da posição p.
    """
    return p[1]


# Reconhecedores
def eh_posicao(arg):
    """
    eh posicao(arg) devolve True caso o seu argumento seja um TAD posicao e False caso contrário.
    """
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int) and \
        isinstance(arg[1], int) and arg[0] >= 0 and arg[1] >= 0


# Testes
def posicoes_iguais(v1, v2):
    """
    posicoes iguais(p1, p2) devolve True apenas se p1 e p2 são posições e são iguais.
    """
    return eh_posicao(v1) and eh_posicao(v2) and obter_pos_x(v1) == obter_pos_x(v2) \
        and obter_pos_y(v1) == obter_pos_y(v2)


# Transformadores
def posicao_para_str(p):
    """
    posicao para str(p) devolve a cadeia de caracteres ‘(x, y)’ que representa o
    seu argumento, sendo os valores x e y as coordenadas de p.
    """
    return "(" + str(obter_pos_x(p)) + ", " + str(obter_pos_y(p)) + ")"


# Funções de alto nível
def obter_posicoes_adjacentes(p):
    """
    obter posicoes adjacentes(p) devolve um tuplo com as posições adjacentes à posição p,
    começando pela posição acima de p e seguindo no sentido horário.
    """
    t = ()
    p1 = cria_posicao(0, 1)
    p2 = cria_posicao(1, 0)
    if eh_posicao(p1) and eh_posicao(p2) and eh_posicao(p):
        if obter_pos_y(p) > obter_pos_y(p1):
            t = t + (cria_posicao(obter_pos_x(p), obter_pos_y(p) - obter_pos_y(p1)),)
        if eh_posicao(cria_posicao(obter_pos_x(p) + obter_pos_x(p2), obter_pos_y(p))):
            t = t + (cria_posicao(obter_pos_x(p) + obter_pos_x(p2), obter_pos_y(p)),)
        if eh_posicao(cria_posicao(obter_pos_x(p), obter_pos_y(p) + obter_pos_y(p1))):
            t = t + (cria_posicao(obter_pos_x(p), obter_pos_y(p) + obter_pos_y(p1)),)
        if obter_pos_x(p) > obter_pos_x(p2):
            t = t + (cria_posicao(obter_pos_x(p) - obter_pos_x(p2), obter_pos_y(p)),)
    return t


def ordenar_posicoes(t):
    """
    ordenar posicoes(t) devolve um tuplo contendo as mesmas posições do tuplo fornecido
    como argumento, ordenadas de acordo com a ordem de leitura do prado.
    """
    return sorted(t, key=lambda x: [obter_pos_y(x), obter_pos_x(x)])


######################
# 2.1.2) TAD Animal  #
######################

# Construtores
def cria_animal(s, r, a):
    """
    cria animal(s, r, a) recebe uma cadeia de caracteres s não vazia correspondente
    à espécie do animal e dois valores inteiros correspondentes à frequência
    de reprodução r (maior do que 0) e à frequência de alimentação a (maior
    ou igual que 0); e devolve o animal. Animais com frequência de alimentação
    maior que 0 são considerados predadores, caso contrário são considerados
    presas. O construtor verifica a validade dos seus argumentos, gerando um
    ValueError com a mensagem ‘cria animal: argumentos invalidos’ caso
    os seus argumentos não sejam válidos.
    """
    if not (isinstance(s, str) and len(s) > 0 and isinstance(r, int) and isinstance(a, int) and r > 0 and a >= 0):
        raise ValueError("cria_animal: argumentos invalidos")
    return [s, r, a, 0, 0]


def cria_copia_animal(a):
    """
    cria copia animal(a) recebe um animal a (predador ou presa) e devolve uma
    nova cópia do animal.
    """
    return a[0], a[1], a[2], a[3], a[4]


def obter_especie(a):
    """
    obter especie(a) devolve a cadeia de caracteres correspondente à espécie do
    animal.
    """
    return a[0]


def obter_freq_reproducao(a):
    """
    obter freq reproducao(a) devolve a frequência de reprodução do animal a.
    """
    return a[1]


def obter_freq_alimentacao(a):
    """
    obter freq alimentacao(a) devolve a frequência de alimentação do animal a
    (as presas devolvem sempre 0).
    """
    return a[2]


def obter_idade(a):
    """
    obter idade(a) devolve a idade do animal a.
    """
    return a[3]


def obter_fome(a):
    """
    obter fome(a) devolve a fome do animal a (as presas devolvem sempre 0).
    """
    return a[4]


# Modificadores
def aumenta_idade(a):
    """
    aumenta idade(a) modifica destrutivamente o animal a, incrementando o valor
    da sua idade em uma unidade, e devolve o próprio animal.
    """
    a[3] = obter_idade(a) + 1
    return a


def reset_idade(a):
    """
    reset idade(a) modifica destrutivamente o animal a, definindo o valor da sua
    idade igual a 0, e devolve o próprio animal.
    """
    a[3] = 0
    return a


def aumenta_fome(a):
    """
    aumenta fome(a) modifica destrutivamente o animal predador a incrementando o valor
    da sua fome em uma unidade, e devolve o pr´oprio animal. Esta operação não modifica
    os animais presa.
    """
    if obter_freq_alimentacao(a) > 0:
        a[4] = obter_fome(a) + 1
    return a


def reset_fome(a):
    """
    reset fome(a) modifica destrutivamente o animal predador a definindo o valor
    da sua fome igual a 0, e devolve o próprio animal. Esta operação não modifica
    os animais presa.
    """
    a[4] = 0
    return a


# Reconhecedores
def eh_animal(arg):
    """
    eh animal(arg) devolve True caso o seu argumento seja um TAD animal e
    False caso contrário.
    """
    return len(arg) == 5 and isinstance(obter_especie(arg), str) and len(obter_especie(arg)) > 0 and \
        isinstance(obter_freq_reproducao(arg), int) and \
        isinstance(obter_freq_alimentacao(arg), int) and obter_freq_reproducao(arg) > 0 and \
        obter_freq_alimentacao(arg) >= 0 and obter_fome(arg) >= 0 and obter_idade(arg) >= 0


def eh_predador(arg):
    """
    eh predador(arg) devolve True caso o seu argumento seja um TAD animal do
    tipo predador e False caso contrário.
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    """
    eh presa(arg) devolve True caso o seu argumento seja um TAD animal do
    tipo presa e False caso contrário.
    """
    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


# Testes
def animais_iguais(a1, a2):
    """
    animais iguais(a1, a2) devolve True apenas se a1 e a2 são animais e são iguais.
    """
    return eh_animal(a1) and eh_animal(a2) and obter_especie(a1) == obter_especie(a2) and \
        obter_freq_reproducao(a1) == obter_freq_reproducao(a2) and \
        obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2) and obter_fome(a1) == obter_fome(a2) and \
        obter_idade(a1) == obter_idade(a2)


# Transformadores
def animal_para_char(arg):
    """
    animal para char(a) devolve a cadeia de caracteres dum único elemento
    correspondente ao primeiro caractere da espécie do animal passada por
    argumento, em maiúscula para animais predadores e em minúscula para animais
    presa.
    """
    if eh_predador(arg):
        return obter_especie(arg)[0].upper()
    else:
        return obter_especie(arg)[0].lower()


def animal_para_str(arg):
    """
    animal para str(a) devolve a cadeia de caracteres que representa o animal
    como mostrado nos exemplos a seguir.
    """
    if eh_predador(arg):
        return str(obter_especie(arg)) + " [" + str(obter_idade(arg)) + "/" + str(obter_freq_reproducao(arg)) + ";" + \
               str(obter_fome(arg)) + "/" + str(obter_freq_alimentacao(arg)) + "]"
    else:
        return str(obter_especie(arg)) + " [" + str(obter_idade(arg)) + "/" + str(obter_freq_reproducao(arg)) + "]"


# Funções de alto nível
def eh_animal_fertil(arg):
    """
    eh animal fertil(a) devolve True caso o animal a tenha atingido a idade de
     reprodução e False caso contrário.
    """
    return obter_freq_reproducao(arg) == obter_idade(arg)


def eh_animal_faminto(arg):
    """
    eh animal faminto(a) devolve True caso o animal a tenha atingindo um valor de
    fome igual ou superior à sua frequência de alimentação e False caso contrário. As
    presas devolvem sempre False.
    """
    if eh_predador(arg):
        return obter_freq_alimentacao(arg) <= obter_fome(arg)
    else:
        return False


def reproduz_animal(a):
    """
    reproduz animal(a) recebe um animal a devolvendo um novo animal da mesma
    espécie com idade e fome igual a 0, e modificando destrutivamente o animal passado
    como argumento a alterando a sua idade para 0.
    """
    a = reset_idade(a)
    return cria_animal(obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a))


#####################
# 2.1.3) TAD Prado  #
#####################

# Construtores
def cria_prado(d, r, a, p):
    """
    cria prado(d, r, a, p) recebe uma posição d correspondente à posição que
    ocupa a montanha do canto inferior direito do prado, um tuplo r de 0 ou
    mais posições correspondentes aos rochedos que não são as montanhas dos
    limites exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p da
    mesma dimensão do tuplo a com as posições correspondentes ocupadas pelos
    animais; e devolve o prado que representa internamente o mapa e os animais
    presentes. O construtor verifica a validade dos seus argumentos, gerando um
    ValueError com a mensagem ‘cria prado: argumentos invalidos’ caso
    os seus argumentos não sejam válidos.

    """
    if not (eh_posicao(d) and isinstance(r, tuple) and 0 <= len(r) == len(
            list(filter(lambda z: z == True, map(lambda z: eh_posicao(z), r))))
            and isinstance(a, tuple) and len(a) >= 1 and isinstance(p, tuple) and len(p) == len(a) and
            len(list(filter(lambda x: x == True,
                            map(lambda x: obter_pos_x(cria_copia_posicao(d)) > obter_pos_x(cria_copia_posicao(x)) > 0,
                                r)))) == len(r) and
            len(list(filter(lambda x: x == True,
                            map(lambda x: obter_pos_y(cria_copia_posicao(d)) > obter_pos_y(cria_copia_posicao(x)) > 0,
                                r)))) == len(r) and  # verifica se as posições dos rochedos e dos animais estão dentro
            len(list(filter(lambda x: x == True,     # dos limites
                            map(lambda x: obter_pos_x(cria_copia_posicao(d)) > obter_pos_x(cria_copia_posicao(x)) > 0,
                                p)))) == len(p) and
            len(list(filter(lambda x: x == True,
                            map(lambda x: obter_pos_y(cria_copia_posicao(d)) > obter_pos_y(cria_copia_posicao(x)) > 0,
                                p)))) == len(p)):
        raise ValueError("cria_prado: argumentos invalidos")
    return [list(d), list(r), list(a), list(p)]


def cria_copia_prado(m):
    """
    cria copia prado(m) recebe um prado e devolve uma nova cópia do prado.
    """
    copia = m.copy
    return copia


# Seletores
def obter_tamanho_x(m):
    """
    obter tamanho x(m) devolve o valor inteiro que corresponde à dimensão Nx
    do prado.
    """
    return obter_pos_x(m[0]) + 1


def obter_tamanho_y(m):
    """
    obter tamanho y(m) devolve o valor inteiro que corresponde à dimensão Ny
    do prado.
    """
    return obter_pos_y(m[0]) + 1


def obter_numero_predadores(m):
    """
    obter numero predadores(m) devolve o número de predadores no prado.
    """
    return len(list(filter(lambda a: eh_predador(a), m[2])))


def obter_numero_presas(m):
    """
    obter numero presas(m) devolve o número de presas no prado.
    """
    return len(list(filter(lambda a: eh_presa(a), m[2])))


def obter_posicao_animais(m):
    """
    obter posicao animais(m) devolve um tuplo contendo as posições do prado
    ocupadas por animais, ordenadas em ordem de leitura do prado.
    """
    i = 0
    soma = []
    while i != len(m[3]):
        if eh_posicao(m[3][i]):
            soma = soma + [cria_copia_posicao(m[3][i]), ]
        i = i + 1
    return ordenar_posicoes(soma)


def obter_posicao_animais_aux(m):
    """
    obter posicao animais aux(m) devolve um tuplo contendo as posições do prado
    ocupadas por animais.
    """
    i = 0
    soma = []
    while i != len(m[3]):
        if eh_posicao(m[3][i]):
            soma = soma + [cria_copia_posicao(m[3][i]), ]  # posição dos animais, mas com a ordem de acordo com o imput
        i = i + 1
    return soma


def obter_animal(m, p):
    """
    obter animal(m, p) devolve o animal do prado que se encontra na posição p.
    """
    pos = obter_posicao_animais_aux(m)
    i = 0
    while i != obter_numero_predadores(m) + obter_numero_presas(m):
        if posicoes_iguais(pos[i], p):
            return m[2][i]
        i = i + 1


# Modificadores
def eliminar_animal(m, p):
    """
    eliminar animal(m, p) modifica destrutivamente o prado m eliminando o animal da
    posição p deixando-a livre. Devolve o próprio prado.
    """
    i = 0
    while i != obter_numero_predadores(m) + obter_numero_presas(m):
        if posicoes_iguais(obter_posicao_animais_aux(m)[i], p):
            del m[2][i]  # apaga o animal
            del m[3][i]  # apaga a posição do animal no prado
            return m
        i = i + 1


def mover_animal(m, p1, p2):
    """
    mover animal(m, p1, p2) modifica destrutivamente o prado m movimentando
    o animal da posição p1 para a nova posição p2, deixando livre a posição onde
    se encontrava. Devolve o próprio prado.
    """
    animal = obter_animal(m, p1)
    eliminar_animal(m, p1)
    m[3] = m[3] + [cria_posicao(obter_pos_x(p2), obter_pos_y(p2)), ]
    m[2] = m[2] + [cria_copia_animal(animal), ]
    return m


def inserir_animal(m, a, p):
    """
    inserir animal(m, a, p) modifica destrutivamente o prado m acrescentando
    na posição p do prado o animal a passado com argumento. Devolve o próprio
    prado.
    """
    m[3] = m[3] + [cria_posicao(obter_pos_x(p), obter_pos_y(p)), ]
    m[2] = m[2] + [cria_copia_animal(a), ]
    return m


# Reconhecedores
def eh_prado(arg):
    """
    eh prado(arg) devolve True caso o seu argumento seja um TAD prado e False
    caso contrário.
    """
    n_posicoes = 0
    n_animais = 0
    n_posicoes_a = 0
    for i in range(len(arg[1])):
        if eh_posicao(arg[1][i]):
            n_posicoes = n_posicoes + 1
    for i in range(len(arg[2])):
        if eh_animal(arg[2][i]):
            n_animais = n_animais + 1
    for i in range(len(arg[3])):
        if eh_posicao(arg[3][i]):
            n_posicoes_a = n_posicoes_a + 1
    return eh_posicao((obter_tamanho_x(arg) - 1, obter_tamanho_y(arg) - 1)) and n_posicoes == len(arg[1]) and \
        n_animais == len(arg[2]) and len(arg[2]) == len(arg[3]) and len(arg[3]) == n_posicoes_a


def eh_posicao_animal(m, p):
    """
    eh posicao animal(m, p) devolve True apenas no caso da posição p do prado
    estar ocupada por um animal.
    """
    return len(list(filter(lambda x: posicoes_iguais(x, cria_copia_posicao(p)), obter_posicao_animais(m)))) == 1


def obter_posicao_obstaculo_aux(m):
    """
    obter posicao obstaculo aux devolve todas as posições ocupadas por montanhas e rochedos,
    ordenadas por ordem de leitura do prado,
    ocupadas por montanhas e rochedos.
    """
    return ordenar_posicoes(list(m[1]) +
                            [cria_posicao(i, 0) for i in range(obter_tamanho_x(m))] +
                            [cria_posicao(0, i) for i in range(1, obter_tamanho_y(m))] +    # posições das montanhas
                            [cria_posicao(obter_tamanho_x(m) - 1, i) for i in range(1, obter_tamanho_y(m))] +
                            [cria_posicao(i, obter_tamanho_y(m) - 1) for i in range(1, obter_tamanho_x(m) - 1)])


def eh_posicao_obstaculo(m, p):
    """
    eh posicao obstaculo(m, p) devolve True apenas no caso da posição p do prado
    corresponder a uma montanha ou rochedo.
    """
    return len(list(filter(lambda x: posicoes_iguais(x, cria_copia_posicao(p)), obter_posicao_obstaculo_aux(m)))) == 1


def eh_posicao_livre(m, p):
    """
    eh posicao livre(m, p) devolve True apenas no caso da posição p do prado
    corresponder a um espaço livre (sem animais, nem obstáculos).
    """
    return not (eh_posicao_animal(m, p) and eh_posicao_obstaculo(m, p))


# Testes
def prados_iguais(p1, p2):
    """
    prados iguais(p1, p2) devolve True apenas se p1 e p2 forem prados e forem
    iguais.
    """
    a_iguais = 0
    pr1 = sorted(p1[2])
    pr2 = sorted(p2[2])
    if len(pr1) == len(pr2):
        for i in range(len(pr1)):
            if animais_iguais(pr1[i], pr2[i]):
                a_iguais = a_iguais + 1

    return eh_prado(p1) and eh_prado(p2) and \
        cria_copia_posicao((obter_tamanho_x(p1), obter_pos_y(p1))) ==\
        cria_copia_posicao((obter_tamanho_x(p1), obter_pos_y(p1))) and \
        obter_posicao_obstaculo_aux(p1) == obter_posicao_obstaculo_aux(p2) and \
        obter_posicao_animais(p1) == obter_posicao_animais(p2) and \
        obter_numero_presas(p1) == obter_numero_presas(p2) and \
        obter_numero_predadores(p1) == obter_numero_predadores(p2) and \
        a_iguais == len(p1[2])


def prado_para_str(m):
    """
    prado para str(m) devolve uma cadeia de caracteres que representa o prado.
    """
    rocha = ordenar_posicoes(list(m[1]))
    string = "+" + "-" * (obter_tamanho_x(m) - 2) + "+" + "\n"
    y = 1
    while y != obter_tamanho_y(m) - 1:
        i = 0
        lista = []
        while i != len(obter_posicao_animais(m)):
            if obter_pos_y(obter_posicao_animais(m)[i]) == y:
                lista = lista + [obter_posicao_animais(m)[i], ]
            i = i + 1
        i = 0
        while i != len(rocha):
            if obter_pos_y(rocha[i]) == y:
                lista = lista + [rocha[i], ]
            i = i + 1
        lista = ordenar_posicoes(lista)
        x = 1
        string = string + "|"
        while x != obter_tamanho_x(m) - 1:
            if len(lista) > 0:
                if obter_pos_x(lista[0]) == x and lista[0] not in rocha:  # quando a posição é ocupada por um animal
                    string = string + animal_para_char(obter_animal(m, lista[0]))
                    lista = lista[1:]
                elif obter_pos_x(lista[0]) == x and lista[0] in rocha:   # quando a posição é ocupada por um rochedo
                    string = string + "@"
                    lista = lista[1:]
                else:
                    string = string + "."
            else:
                string = string + "."
            x = x + 1
        if not lista:      # quando já não há animais nem rochedos a colocar na linha
            string = string + "|" + "\n"
        y = y + 1
    return string + "+" + "-" * (obter_tamanho_x(m) - 2) + "+"


# Funções de alto nível
def obter_valor_numerico(m, p):
    """
    obter valor numerico(m, p) devolve o valor numérico da posição p correspondente
    à ordem de leitura no prado m.
    """
    return obter_tamanho_x(m) * obter_pos_y(p) + obter_pos_x(p)


def obter_movimento_sem_presa_adjacente_aux(m, p):
    """
    obter_movimento_sem_presa_adjacente_aux(m,p) devolve o movimento de qualquer presa ou qualquer predador
     que não tenha nenhuma presa nas suas posições adjacentes.
    """
    posicoes_livres = []
    N = obter_valor_numerico(m, p)
    for i in range(len(obter_posicoes_adjacentes(p))):
        if eh_posicao_livre(m, obter_posicoes_adjacentes(p)[i]):
            posicoes_livres = posicoes_livres + [obter_posicoes_adjacentes(p)[i], ]
    if not posicoes_livres:
        return p
    else:
        y = N % len(posicoes_livres)
    return posicoes_livres[y]


def obter_movimento(m, p):
    """
    obter movimento(m, p) devolve a posiçãa seguinte do animal na posição p dentro
    do prado m de acordo com as regras de movimento dos animais no prado.
    """
    if eh_presa(obter_animal(m, p)):
        return obter_movimento_sem_presa_adjacente_aux(m, p)
    else:
        possiveis_presas = []
        presas = []
        animais_e_adj = ordenar_posicoes(((list(obter_posicoes_adjacentes(p))) + list(obter_posicao_animais(m))))
        i = 1
        while i != len(animais_e_adj):
            if animais_e_adj[i - 1] == animais_e_adj[i]:   # se a posição adjacente de p for igual à de um animal
                possiveis_presas = possiveis_presas + [animais_e_adj[i], ]
            i = i + 1
        if len(possiveis_presas) == 0:
            return obter_movimento_sem_presa_adjacente_aux(m, p)
        for i in range(len(possiveis_presas)):
            if eh_predador(possiveis_presas[i]):     # se o animal adjacente for um predador
                pass
            else:
                presas = presas + [possiveis_presas[i], ]    # se o animal adjacente for uma presa
        if len(presas) == 0:                     # se não houver presas adjacentes o animal move-se como uma presa
            return obter_movimento_sem_presa_adjacente_aux(m, p)
        else:
            N = obter_valor_numerico(m, p)
            y = N % len(presas)
            return ordenar_posicoes(presas)[y]


def geracao(m):
    """
    geracao(m) é a função auxiliar que modifica o prado m fornecido como argumento de
    acordo com a evolução correspondente a uma geração completa, e devolve o próprio
    prado. Isto é, seguindo a ordem de leitura do prado, cada animal (vivo) realiza o seu
    turno de açao de acordo com as regras descritas.
    """
    posicao = obter_posicao_animais(m)
    i = 0
    while i != len(posicao):
        m = mover_animal(m, posicao[i], obter_movimento(m, posicao[i]))
        i = i + 1
    return m
