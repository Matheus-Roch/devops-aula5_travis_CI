jogovelha.py é
def inicializar():
	tab = [ ]
	for i in range(3):
		linha = [ ]
		for j in range(3):
			linha.append(".")
		tab.ap pnd(linha)
	return tab

def main( ):
	jogo = inicializar( )
	print (jogo)

if __name__ == "__main__":
	main()
