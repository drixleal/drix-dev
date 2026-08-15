print("Olá, Parceiro! Iniciando os estudos de Fundamentos do Python.")

#----------------------------------------------------------------------------------------------------------------

# PROGRAMA: Calculadora de Velocidade Média

# Passo 1: Aceitar um número que represente a distância;
# Usamos input() para fazer a pergunta na tela.
# Usamos float() para transformar a resposta digitada em um número decimal.
distancia = float(input("Digite a distância percorrida na sua jornada (em km): "))

# Passo 2: Aceitar um número que represente o tempo de viagem.
tempo = float(input("Digite o tempo gasto na viagem (em horas): "))

# Passo 3: Dividir a distância pelo tempo e armazenar na memória (na variável 'velocidade_media').
velocidade_media = distancia / tempo

# Passo 4: Exibir o resultado em um formato legível.
# O 'f' antes das aspas permitem injetar o valor da variável diretamente no texto usando chaves {}.
print(f"Resultado: A velocidade média da sua jornada foi de {velocidade_media} km/h.")

#----------------------------------------------------------------------------------------------------------------

