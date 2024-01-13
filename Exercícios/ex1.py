#tarefa: selecione todos os números impares de 1 a 100, e então conte quantos números tem.
#adicional: faça o usuário selecionar entre ímpar ou par e a faixa numérica, não deixe que o programa deixe de rodar.
def inicio():
    f1 = int(input(f"digite o primeiro número da faixa desejada: "))
    f2 = int(input(f"digite o último número da faixa desejada: "))
    ip = input(f"par ou ímpar? ")
    contagem = 0
    if ip == "impar":
        for numero in range((f1), (f2)):
            if numero % 2 != 0:
                print(numero)
        contagem += 1
    print(f"existem {contagem} números ímpares nesta faixa de números.")

    if ip == "par":
      for numero in range((f1), (f2)):
         if numero % 2 == 0:
            print(numero)
            contagem += 1
    print(f"existem {contagem} números pares nesta faixa de números.")
inicio()