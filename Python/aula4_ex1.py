valorCompra = float(input("Digite o valor da compra: "))
codigo = int (input("Digite o código da compra: "))
if codigo == 1:
    print("Sua compra será no valor de: R$" , (valorCompra - (valorCompra *0.10)))
elif codigo == 2:
    print("Sua compra será no valor de: R$" , (valorCompra - (valorCompra *0.05)))
elif codigo == 3:
    print("A compra ficará no valor de: R$", valorCompra , "em duas parcelas no valor de: R$" , (valorCompra/2))
else: 
    print("A compra ficará no valor de: " , ((valorCompra * 0.10) + valorCompra))
