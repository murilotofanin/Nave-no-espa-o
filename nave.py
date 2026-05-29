##Definir as variaveis

combustivel = 110

tripulantes = []

##Definir funçoes
def viajar():
    ##Aqui vamos ter que gastar os combustivel
    global combustivel ## Avisa a função que vamos modificar uma variavel interna
    if(combustivel >= 30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Voce esta sem combustivel para poder viajar, Abasteça!")


def abastecer():
    global combustivel
    combustivel =  110

    print("A nava já esta pronta para viajar denovo, BOA VIAJEM 👍!!! .")


def status_nave():
        ##Mostrar a quantidade de combuistivel e a quantidade de tripulante
        print(f"Temos {combustivel} de combustivel")
        print(f"OS tripulantes são: {tripulantes}")
    

def registrartripulantes():
        ##Adiciona tripulantes na lista de tripulantes
        novotripulante = input("Qual o nome do novo tripulante:")
        tripulantes.append(novotripulante)
        print("Tripulante inseirdo com sucesso!!!")




##Criar um menu

while True:
    print("\nBem vindo ao menu interativo da nave. Por favor  selecione uma opção:")
    print("\n1 - Mostrar staus da nave | 2- Viajar | 3-Abastecer  | 4- Novo Tripulante | 5-Sair")
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
        break
        

















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
