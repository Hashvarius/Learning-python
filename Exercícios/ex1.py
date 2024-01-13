#tarefa: selecione todos os números impares de 1 a 100, e então conte quantos números tem.
contagem = 0
for numero in range(1, 100):
    if numero % 2 != 0:
        print(numero)
        contagem += 1
print(f"existem {contagem} números ímpares nesta faixa de números.")