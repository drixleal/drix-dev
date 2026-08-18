# PROGRAMA: O Poder da Semântica Dinâmica

# Passo 1: Criamos uma variável e guardamos um texto (String) nela.
minha_variavel = "Monty Python's Flying Circus"

print("--- Passo 1 ---")
print(f"O valor guardado é: {minha_variavel}")
# A função type() vai nos dizer que isso é da classe 'str' (String/Texto)
print(f"O Python enxerga isso como: {type(minha_variavel)}")

print("\n") # Pulando uma linha para organizar o terminal

# Passo 2: A Mágica Dinâmica!
# Na mesma variável, vamos jogar fora o texto e colocar um número inteiro (o ano de estreia do programa).
minha_variavel = 1969

print("--- Passo 2 ---")
print(f"O novo valor guardado é: {minha_variavel}")
# A função type() vai nos dizer que agora isso mudou para a classe 'int' (Integer/Inteiro).
print(f"O Python agora enxerga isso como: {type(minha_variavel)}")

#Conclusão: O Python não gerou erro, ele se adaptou dinamicamente ao novo tipo de dado!