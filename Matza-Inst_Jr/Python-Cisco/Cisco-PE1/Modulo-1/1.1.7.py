# SCRIPT: Descobrindo a Plataforma (Cross-Platform)

# Passo 1: Importamos a biblioteca 'platform' que já vem instalada com o Python.
# Ela contém ferramentas para investigar o sistema operacional da máquina.
import platform

# Exibindo um cabeçalho simples para organizar a saída
print("--- Verificador de Ambiente Python ---")

# Passo 2: Usamos a função 'platform.system()' para descobrir o nome do sistema operacional.
# O interpretador Python fará o trabalho de traduzir isso para a linguagem da sua máquina.
# Vamos guardar a resposta na variável 'nome_do_sistema'.
nome_do_sistema = platform.system()

# Passo 3: Exibimos o resultado na tela.
print(f"Sucesso Este script foi interpretado e está rodando em um sistema: {nome_do_sistema}")

# Passo 4 (Extra): Vamos ser um pouco mais curiosos e pedir a versão do sistema.
verao_do_sistema = platform.release()
print(f"A versão detalhada desta máquina é: {verao_do_sistema}")