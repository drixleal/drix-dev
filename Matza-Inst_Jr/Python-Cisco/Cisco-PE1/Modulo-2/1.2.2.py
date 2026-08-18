# PROGRAMA: O Pai do Python

# Passo 1: Armazenando as informações históricas nas variáveis corretas
criador = "Guido van Rossum"
ano_nascimento = 1956
pais_origem = "Holanda"
linguagem = "Python"

# Passo 2: Processando dados. 
# O Python é excelente em matemática. Vamos calcular a idade aproximada dele.
ano_atual = 2026
idade = ano_atual - ano_nascimento

# Passo 3: Exibindo as informações de forma estruturada na tela
print("=======================================")
print("          FICHA HISTÓRICA              ")
print("=======================================")

# Injetando as variáveis dentro dos textos usando f-strings
print(f"Linguagem: {linguagem}")
print(f"Criador:   {criador}")
print(f"Origem:    {pais_origem}")
print(f"Idade em {ano_atual}: {idade} anos")

# Um truque novo (Bônus): No Python, você pode multiplicar um texto para repeti-lo!
# Isso criará uma linha de 39 caracteres de igual '=' sem precisar digitar um por um.
print("=" * 39)