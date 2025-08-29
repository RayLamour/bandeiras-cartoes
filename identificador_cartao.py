python identificador_cartao.pydef identificar_bandeira(numero):
    numero = str(numero)
    if numero.startswith('4'):
        return 'Visa'
    elif (numero.startswith(tuple(str(i) for i in range(51, 56))) or
          (len(numero) >= 4 and 2221 <= int(numero[:4]) <= 2720)):
        return 'MasterCard'
    elif (numero.startswith('34') or numero.startswith('37')):
        return 'American Express'
    elif (numero.startswith('6011') or numero.startswith('65') or
          (len(numero) >= 3 and 644 <= int(numero[:3]) <= 649)):
        return 'Discover'
    elif numero.startswith('6062'):
        return 'Hipercard'
    elif (numero.startswith('4011') or numero.startswith('4312') or numero.startswith('4389')):
        return 'Elo'
    else:
        return 'Bandeira não identificada'

if __name__ == "__main__":
    numero = input("Digite o número do cartão: ")
    bandeira = identificar_bandeira(numero)
    print(f"Bandeira identificada: {bandeira}")
