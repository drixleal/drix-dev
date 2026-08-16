# PROGRAMA: Demonstrando o Código-Fonte
# Importamos a ferramenta 'dis' que permite ver as instruções internas do Python
import dis

# 1. O NOSSO CÓDIGO-FONTE (Linguagem de Alto Nível)
# Criamos uma operação simples e legível para humanos: uma função que dobra um número.
def calcular_dobro(numero):
    resultado = numero * 2
    return resultado

print("--- 1. Executando o Código de Alto Nível ---")
print(f"O dobro de 5 é: {calcular_dobro(5)}")
print("\n") # Pula uma linha para originar o visual no terminal

# 2. A LISTA DE INSTRUÇÕES (Aproximação da Linguagem de Máquina)
print("--- 2. Revelando as Instruções de Máquina (IL / Bytecode) ---")
# Aqui usamos a ferramenta para demonstrar a nossa função e ver o que o computador realmente lê
dis.dis(calcular_dobro)