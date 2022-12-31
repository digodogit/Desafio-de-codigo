import os 
import sys
#Desenvolvido por Rodrigo Carvalho QUaglio Magalhães.
#E-mail: Rodrigo.quaglio@hotmail.com
#github: @digodogit

#Função para realizar os testes
def main():
    Sair = False
    while not Sair:
        print("Escolha entre as opções 1, 2 e 3!")
        print("1 - digitar endereço")
        print ("2 - casos de testes")
        print ("3 - sair")
        Escolha = input("escolha: ")
        if Escolha== "1":
            Endereco_num = input("Qual o Endereço e o número? ")
            if len(Endereco_num) > 0 :
                logica(Endereco_num)
            else:
                print("Endereço invalido, tente novamente")

        elif Escolha== "2":
                Endereco_num = ["Miritiba 339","Cambuí 804B","Quirino dos Santos 23 b", "4, Rue de la République", "Calle 44 No 1991"]
                for Enderecos in Endereco_num:
                    logica(Enderecos)

        elif Escolha == "3":
            Sair = True
        else:
            print("Valor invalido, tente novamente")

# Função com a Lógica da aplicação.
def logica(Endereco_num):
    # Variáveis utilizadas para armazenamento das strings
    nome = []
    numero = []
    chars = []
    print_Numero =''
    print_Nome =''
    check_chars=''

    # Vetor contendo numeros de 0 a 9 com o tipo sendo String. Utilizado mais a frente para comparação.
    numeros = ['0','1','2','3','4','5','6','7','8','9']

    # Variáveis utilizadas para controle de exceções
    execoes = ['st','th','nd']
    ignorar = [',','.']

    # Chamada de função que divide uma String a partir de um caractere identificado, nesse caso o espaço (" ").
    endereco = Endereco_num.split()

    # De inicio, o código verifica se o endereço passado começa com um número ou uma letra. Importante a separação para evitar conflitos de certas situações excepcionais.
    # Se o endereço começar com número realizará os seguintes passos:
    if endereco[0][0] in numeros:
        for palavra in endereco:
            # O código checa se o primeiro caractere da palavra atual começa com um número. Se sim, ele irá verificar cada caractere separadamente. Existem 2 casos:
            # Caso 1 - Se o caractere for número ele irá adicionar ao Vetor Número.
            # Caso 2 - Se o caractere for letra ele irá adicionar ao Vetor Chars.
            # A divisão é feita para tratar casos de alguns países, como EUA, onde algumas ruas possuem números ordinais.
            if palavra[0] in numeros:
                for caractere in palavra:
                    #Caso 1
                    if caractere not in numeros:
                        chars.append(caractere)     
                        check_chars=''.join(chars)

                #checa se é um caso de número ordinal ou não.
                if check_chars in execoes:
                    nome.append(palavra)
                    nome.append(' ')
                    print_Nome = ''.join(nome)
                    chars.clear()
                    check_chars=''.join(chars) 

                #caso 2   
                else: 
                    #Condição para detectar virgula e ignora-la para números.
                    if palavra[-1] in ignorar:
                        numero.append(palavra[:len(palavra)-1])
                    else:
                        numero.append(palavra)
                    numero.append(' ')
                    print_Numero = ''.join(numero)

            #Se for identificado que não começa com número, adiciona automaticamente no Vetor Nome.
            else:
                #Condição para detectar virgula e ignora-la para letras.
                if palavra[-1] in ignorar:
                    nome.append(palavra[:len(palavra)-1])

                else:
                    nome.append(palavra)
                nome.append(' ')
                print_Nome = ''.join(nome)

    #Se o endereço NÃO começar com número a lógica seguirá de forma parecida, porém com uma exceção para casos com ruas onde há 1 número fazendo parte do nome da rua:
    else:
        for palavra in endereco:
            if palavra[0] in numeros:
                for caractere in palavra:
                    if caractere not in numeros:
                        chars.append(caractere)
                        check_chars=''.join(chars)

                if check_chars in execoes:
                    nome.append(palavra)
                    nome.append(' ')
                    print_Nome = ''.join(nome)
                    chars.clear()
                    check_chars=''.join(chars) 
                else:
                    if palavra[-1] in ignorar:
                        numero.append(palavra[:len(palavra)-1])
                    else:
                        numero.append(palavra)
                    numero.append(' ')
                    print_Numero = ''.join(numero)
            else:
                if len(numero) != 0 :
                    #Tratamento para o caso descrito anteriormente.
                    if palavra== 'No' or palavra == 'nº' or palavra== 'n°':
                        nome.append(numero[0])
                        nome.append(' ')
                        numero.clear()
                        print_Nome = ''.join(nome)
                    numero.append(palavra)
                    numero.append(' ')
                    print_Numero = ''.join(numero)

                elif palavra[-1] in ignorar:
                    nome.append(palavra[:len(palavra)-1])
                    nome.append(' ')
                    print_Nome = ''.join(nome)

                else:
                    nome.append(palavra)
                    nome.append(' ')
                    print_Nome = ''.join(nome)

    print ("Nome: "+ print_Nome)
    print ("Número: "+ print_Numero)
    print ("\n")

#Inicia a aplicação.
if __name__ == '__main__':
    main()