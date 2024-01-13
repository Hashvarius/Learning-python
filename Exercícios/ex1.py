#tarefa: selecione todos os números impares de 1 a 100, e então conte quantos números tem.
#adicional: faça o usuário selecionar entre ímpar ou par e a faixa numérica, não deixe que o programa deixe de rodar.

def inicio():
    f1 = int(input(f"Digite o primeiro número da faixa desejada: "))
    f2 = int(input(f"Digite o último número da faixa desejada: "))
    ip = input(f"Par ou ímpar? ").lower()
    contagem = 0

    if ip == "ímpar":
        numeros_impares = [numero for numero in range(f1, f2) if numero % 2 != 0]
        contagem = len(numeros_impares)
        print(numeros_impares)
        print(f"Existem {contagem} números ímpares nesta faixa de números.")
    elif ip == "par":
        numeros_pares = [numero for numero in range(f1, f2) if numero % 2 == 0]
        contagem = len(numeros_pares)
        print(numeros_pares)
        print(f"Existem {contagem} números pares nesta faixa de números.")
    else:
        print("Opção inválida. Digite 'par' ou 'ímpar'.")

inicio()