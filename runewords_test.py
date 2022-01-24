#runewords

runes = {"el":0, "eld":1, "tir":2, "nef":3, "eth":4, "ith":5, "tal":6, "ral":7, "ort":8, "thul":9, "amn":10, "sol":11, "shael":12, "dol":13, "hel":14, "io":15, "lum":16, "ko":17, "fal":18, "lem":19, "pul":20, "um":21, "mal":22, "ist":23, "gul":24, "vex":25, "ohm":26, "lo":27, "sur":28, "ber":29, "jah":30, "cham":31, "zod":32}

class Runeword:
    def __init__(self, name, runes, equip, level, stats, ladder=False):
        self.name = name
        self.runes = runes
        self.equip = equip
        self.level = level
        self.stats = stats
        self.ladder = ladder

    def print_runeword(self):
        print "Nome:", self.get_name()
        print "Runas:", self.get_runes()
        print "Equipamento:", self.get_equip()
        print "Level:", self.get_level()
        print "Atributos:"
        for s in self.get_stats():
            print "-->", s
        print "Servidor:", self.is_ladder()

    def get_name(self):
        return self.name

    def get_runes(self):
        return self.runes

    def get_equip(self):
        return self.equip

    def get_level(self):
        return self.level

    def get_stats(self):
        return self.stats

    def is_ladder(self):
        return self.ladder

    def rune_exist(self, rune="runa"):
        """ A runa existe na runeword? """
        result = []
        for r in self.runes:
            if r == rune:
                result.append(r)
        if result != []:
            return True
        else:
            return False
            

#catalogo de runewords
rw = set([])
result = []

#inicializador do catalogo:
def inicializador():
    """ Inicializa o banco de dados a partir de arquivo """
    global rw
    f = open('database.txt')
    s = f.readline()
    while s != '[end]':
        runeword = []
        name = ""
        rune = []
        equip = []
        level = 0
        stats = []
        ladder = ""
        while s[0:3] != '[-]':
            runeword.append(s)
            s = f.readline()
        for r in runeword:
            if r[0:3] == '[n]':
                name = r[3:-1]
            elif r[0:3] == '[r]':
                rune.append(r[3:-1])
            elif r[0:3] == '[e]':
                equip.append(r[3:-1])
            elif r[0:3] == '[l]':
                level = int(r[3:-1])
            elif r[0:3] == '[s]':
                stats.append(r[3:-1])
            elif r[0:3] == '[?]':
                ladder = r[3:-1]
        rw.add(Runeword(name, rune, equip, level, stats, ladder))
        s = f.readline()
    f.close()

#busca por runa
def busca_runa(runa1=None, runa2=None, runa3=None, runa4=None, runa5=None, runa6=None):
    global result
    match = None
    while(len(result) != 0):
        result.pop()

    querry = set([runa1, runa2, runa3, runa4, runa5, runa6])
    querry.difference_update(set([None]))

    for r in rw:
        for q in querry:
            if r.rune_exist(q):
                match = True
            else:
                match = False
                break
        if match == True:
            result.append(r)
    print_result()
            
#busca por nivel
def busca_nivel(nivel):
    global result
    while(len(result) != 0):
        result.pop()

    for r in rw:
        if r.get_level() <= nivel:
            result.append(r)
    print_result()

#imprime os resultados
def print_result():
    print "-------------", len(result), "runewords encontradas --------------"
    for r in result:
        print result.index(r), ")", r.get_name(), "LV", r.get_level(), r.get_runes()
    if len(result) != 0:
        entrada = raw_input("---> Digite um numero de runeword para detalhes:")
        info(int(entrada))
    else:
        print "----------------------------------------------------"

#imprime informacoes detalhadas sobre a runeword
def info(index):
    try:
        result[index].print_runeword()
    except IndexError:
        print "Valor de id invalido"
    entrada = raw_input("--> Pressione qualquer tecla para continuar:")
    
def menu():
    opcao = -1
    input_runas = [None, None, None, None, None, None]
    while opcao != 4:
        print ""
        print "Runewords v1.0 - Menu Principal"
        print "1: Busca por runas"
        print "2: Busca por nivel"
        print "3: Mostrar resultado de busca anterior"
        print "4: Sair"
        entrada = raw_input("--> Digite sua opcao:")
        print ""

        opcao = int(entrada)

        if opcao == 1:
            print "**** Busca por runas ****"
            print "Digite o nome da runa"
            print "Todas as letras em minusculas"
            print "Qualquer expressao que nao seja uma runa sera descartada"
            for i in range(6):
                entrada = raw_input("--> "+str(i+1)+"a runa")
                if runes.has_key(str(entrada)):
                    input_runas[i] = str(entrada)
            busca_runa(input_runas[0], input_runas[1], input_runas[2], input_runas[3], input_runas[4], input_runas[5])
            input_runas = [None, None, None, None, None, None]
        elif opcao == 2:
            print "**** Busca por nivel ****"
            print "Digite o nivel da runa [0..100]"
            print "Serao exibidas todas as runas cujo nivel seja menor ou igual ao valor digitado"
            entrada = raw_input("--> Digite o nivel da runa:")
            if int(entrada) >= 0 and int(entrada) <= 100:
                busca_nivel(int(entrada))
            else:
                print "Valor invalido."
                entrada = raw_input("--> Pressione qualquer tecla para continuar:")
        elif opcao == 3:
            print_result()
                

    
#*******************************************************************#

print "Inicializando..."
inicializador()
print len(rw), " runewords registradas no banco de dados."
print "Pronto!!!"
menu()

