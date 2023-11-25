#=============================Calcular saldo de vitorias=============================#
def calcularSaldo(vitorias,derrotas):
    saldoVitorias = vitorias - derrotas
    if saldoVitorias <= 10:
        nivel = 'Ferro'
    elif saldoVitorias >= 11 and saldoVitorias <= 20:
        nivel = 'Bronze'
    elif saldoVitorias >= 21 and saldoVitorias <= 50:
        nivel = 'Prata'
    elif saldoVitorias >= 51 and saldoVitorias <= 80:
        nivel = 'Ouro'
    elif saldoVitorias >= 81 and saldoVitorias <= 90:
        nivel = 'Diamante'
    elif saldoVitorias >= 91 and saldoVitorias <= 100:
        nivel = 'Lendário'
    elif saldoVitorias >= 101:
        nivel = 'Imortal'
    print(f"O Herói tem de saldo de *{saldoVitorias}* está no nível de *{nivel}*")



while True:
    try:
        vitorias = int(input("Digite a quantidade de vitórias (ou digite '0' para sair): "))
        if vitorias == 0:
            break
        derrotas = int(input("Digite a quantidade de derrotas: "))

        resultado = calcularSaldo(vitorias, derrotas)
        print(resultado)
    except ValueError:
        print("Por favor, digite um número inteiro.")
