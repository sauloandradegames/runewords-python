def printdatabase():
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
				name = '"'
				name = name + r[3:-2]
				name = name + '"'
			elif r[0:3] == '[r]':
				rune.append(r[3:-2].capitalize())
			elif r[0:3] == '[e]':
				equip.append(r[3:-2].capitalize())
			elif r[0:3] == '[l]':
				level = r[3:-2]
			elif r[0:3] == '[s]':
				stats.append(r[3:-2])
			elif r[0:3] == '[?]':
				ladder = r[3:-2]
		print "{"
		print '    "Nome"' + ' : ' + name
		print '    "Runa"' + " : " + str(rune)
		print '    "Equipamento"' + " : " + str(equip)
		print '    "Nivel"' + " : " + '"' + level + '"'
		print '    "Atributo"' + " : " + str(stats)
		print '    "Servidor"' + " : " + '"' + ladder + '"'
		print "},"
		s = f.readline()
	f.close()
		
printdatabase()

#runeword
#{
#	"Nome" : "Ancient's Pledge"
#	"Runa" : ["ral", "ort", "tal"]
#	"Equipamento" : ["escudos"]
#	"Nivel" : 21
#	"Atributo" :
#	[
#		"Resistencia ao frio +43%",
#		"Resistencia ao fogo +48%",
#		"Resistencia ao raio +48%",
#		"Resistencia ao veneno +48%",
#		"Aumento de defesa +50%"
#	]
#	"Servidor" : "Livre"
#}
