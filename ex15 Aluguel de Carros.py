dias = int(input('Quantos dias o carro foi alugado?'))
diaria = 60.00
km = float(input('Quantos KM foi rodado?'))
valor_km = 0.15
print('O valor total a pagar será R${:.2f}'.format((dias * diaria)+(km * valor_km)))