#coding: utf-8

valorDeposito = input("Digite o valor do depósito \n")
taxaJuros = input("Digite o valor da taxa de juros aplicada \n")
dep = int(valorDeposito)
taxa = int(taxaJuros)
prazoAplicacao = input("Digite o prazo de resgate da aplicação \n")
prazo = int(prazoAplicacao)
porcento = taxa/100
rend = dep*(1+porcento)**prazo

print("=======================================================\n")

print("Valor depositado: R$", valorDeposito)
print("Taxa de juros aplicada: ", taxa, "%")
print("Prazo da aplicação: ",prazo, "vezes\n")

print("========================================================\n")

print("O valor do rendimento será: R$", rend - dep)
print("O valor total do investimento será: R$", rend, "\n")

print("========================================================")
