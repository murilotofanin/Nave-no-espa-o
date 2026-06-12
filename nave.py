##Definir as variaveis

combustivel = 100

tripulantes = [6]

##Definir funçoes2

def viajar():
    if (tripulantes) ==0:
        print("\nNão contem nenhum tripulante na nave, a nave não podera partir para viajem!!")
    input()
    return
    ##Aqui vamos ter que gastar os combustivel
    global combustivel ## Avisa a função que vamos modificar uma variavel interna
    if(combustivel >= 30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Voce esta sem combustivel para poder viajar, Abasteça!")

        ##Criar uma função para pausar o código entre as interações do usuario
    
def travarMenu():
    ##nosso code vai aqui
    input("\nPresione <ENTER> para continuar....")


def abastecer():
    global combustivel
    combustivel =  100

    print("A nava já esta pronta para viajar denovo, BOA VIAJEM 👍!!! .")
    travarMenu()

def status_nave():
        ##Mostrar a quantidade de combuistivel e a quantidade de tripulante
        print(f"Temos {combustivel} de combustivel")
        print(f"OS tripulantes são: {tripulantes}")
        
        travarMenu()
    

def registrartripulantes():
        ##Adiciona tripulantes na lista de tripulantes
        novotripulante = input("Qual o nome do novo tripulante:")
        tripulantes.append(novotripulante)
        print("Tripulante inseirdo com sucesso!!!")
        travarMenu()

def removertripulante():
    global tripulante

    if len(trupulante) ==0:
        print("\nOs tripulantes restantes são: {tripulantes}")

    else:
        tripulantes.pop()
        print(f"\nOs tripulantes restantes são: {tripulantes}")

    travarMenu()


##Criar um menu

while True:
    print("\nBem vindo ao menu interativo da nave. Por favor  selecione uma opção:")
    print("\n1 - Mostrar staus da nave | 2- Viajar | 3-Abastecer  | 4- Novo Tripulante | 5-Sair  | 6-Saida de um tripulante 2")
    opcao = input("Escolha:")
    if (opcao == "1"):
        status_nave()
    elif (opcao == "2"):
        viajar()

    elif (opcao == "3"):
        abastecer()

    elif (opcao == "4"):
        novotripulante()
    elif (opcao =="5"):
        print("Viagem encerrada!!🛬")

    elif (opcao == "6"):
        tripulantes.pop()
        print("Tripulante retirado com sucesso👍👍!!")
        break
        
    elif (opcao =="7"):
        len(tripulantes)
        print("Os tripulantes restantes são:")


    if (tripulantes) ==0:
        print("\nNão contem nenhum tripulante na nave, a nave não podera partir para viajem!!")

        











#status_nave()
#registrartripulantes()
#status_nave
#viajar()
#viajar()
#status_nave()
#viajar()
#viajar()
#abastecer()
#viajar()
