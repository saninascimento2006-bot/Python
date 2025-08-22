import math

num= float(input("\nDigite um número e você saberá a raiz quadrada dele: "))  #pergunta o número
raiz= math.sqrt(num)  #funcao da biblioteca math pra achar a raiz
print(f"\nA raiz exata do número {num:.0f} é {raiz}")  #mostra a raiz sem virgulas no numero mas com virgula no resultado
raiz_cima= math.ceil(raiz)  #funcao para arredondar para cima
print(f"\nMas a raiz arredondada dele é {raiz_cima:.0f}")  #mostra o resultado sem virgula
print(f"\nIsso meio que quer dizer que raiz do número {math.trunc(num)} é aproximadamente {math.ceil(raiz)}\n")  #usando o f
#print("\nIsso meio que quer dizer que raiz do número {} é aproximadamente {}\n".format (math.trunc(num), math.ceil(raiz)))  #usando o format
