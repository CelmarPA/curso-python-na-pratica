# Variável no escopo global
meu_nome = "Celmar"

def exibir_nome():
    # Espaço no escopo local
    print(f"Seu nome é {meu_nome}")

exibir_nome()

# Escopo global NÃO ENXERGA o que está no escopo local
# Escopo local ENXERGA o que está no espoco glocal
