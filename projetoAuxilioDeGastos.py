#aqui o usuario digitirá o quanto deseja gastar nesse dia
limite_de_gastos = float(input("digite o valor maximo a ser gasto nesse dia:"))

#variavel para acumular os valores gastos no dia
total_gasto = 0

#eu determinei essa variavel como não a principio para o while iniciar,
#dava pra fazer um "while true" e depois usar o break em baixo, 
#mas achei mais pratico dessa forma
terminar = "n"

#loop de repetição para perguntar os gastos do dia
while terminar =="n":

    #neste campo, o usuario irá digitar os gastos quando os fazê-los
    gasto_feito = float(input("digite quanto você gastou:"))

    #validação se o numero digitado foi positivo ou não,
    #se foi positivo continua o codigo se não o codigo pede um valor positivo
    if gasto_feito < 0:
        print("por favor digite um valor positivo.")
    else:
        #variavel acumulativa

        total_gasto = total_gasto + gasto_feito
        #aqui eu pergunto se esse foi todo o gasto do dia

        terminar = input("isso foi tudo? (s/n).")

#calculo da porcentagem gasta
porcentagem = total_gasto / limite_de_gastos * 100

#respostas do sistema
if porcentagem < 50 :
    print("parabens! você conseguiu se manter em menos da metade do limite.😄​")

elif porcentagem < 100 :
    print("boa você se manteve abaixo do limite estipulado.👌​")

elif porcentagem <= 120 :
    print("voce passou do limite, mais cuidado na proxima.😟​")

else :
    print("voce passou MUITO do limite...😡​")
    
print(f"você gastou {total_gasto: .2f}, de {limite_de_gastos: .2f}, um total de {porcentagem: .2f}% do total.")