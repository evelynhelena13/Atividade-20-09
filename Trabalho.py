print("AGENDA DE ALUNOS")

nome = input("Digite seu nome: ")
rua = input("Digite o nome da sua rua: ")
cep = input("Digite seu cep: ")
bairro= input("Digite seu bairro: ")
estado= input("Digite seu estado: ")
telefone = input("Digite seu telefone: ")
C = input("Deseja inserir mais dados: ")

arq=open("teste.txt","a")
arq.write("NOME")
arq.write("\n")
arq.write(nome)
arq.write("\n")
arq.write("RUA")
arq.write("\n")
arq.write(rua)
arq.write("\n")
arq.write("CEP")
arq.write("\n")
arq.write(cep)
arq.write("\n")
arq.write("BAIRRO")
arq.write("\n")
arq.write(bairro)
arq.write("\n")
arq.write("ESTADO")
arq.write("\n")
arq.write(estado)
arq.write("\n")
arq.write("TELEFONE")
arq.write("\n")
arq.write(telefone)


while C =="sim":
    nome = input("Digite seu nome: ")
    rua = input("Digite o nome da sua rua: ")
    cep = input("Digite seu cep: ")
    bairro= input("Digite seu bairro: ")
    estado= input("Digite seu estado: ")
    telefone = input("Digite seu telefone: ")
    C = input("Deseja inserir mais dados: ")

    arq=open("teste.txt","a")
    arq.write("NOME")
    arq.write("\n")
    arq.write(nome)
    arq.write("\n")
    arq.write("RUA")
    arq.write("\n")
    arq.write(rua)
    arq.write("\n")
    arq.write("CEP")
    arq.write("\n")
    arq.write(cep)
    arq.write("\n")
    arq.write("BAIRRO")
    arq.write("\n")
    arq.write(bairro)
    arq.write("\n")
    arq.write("ESTADO")
    arq.write("\n")
    arq.write(estado)
    arq.write("\n")
    arq.write("TELEFONE")
    arq.write("\n")
    arq.write(telefone)
    

