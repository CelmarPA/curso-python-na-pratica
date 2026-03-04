from random import random, randint

# random() gera números decimais (float) aleatórios seguindo o intervalo 0 -1 onde 0 está incluso e 1 não.
resultado_random = random()
print(f"Valor gerado com random {resultado_random}")

# randint() gera número inteiros (int) aleatórios seguindo o intervalo definido pelos parâmetros (incluindo cada um deles)
resultado_randint = randint(20, 30)
print(f"Valor gerado com randint {resultado_randint}")
