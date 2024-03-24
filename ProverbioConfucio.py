# Provérbio de Confúcio
proverbio = "O homem superior é modesto em sua fala, mas excede em suas ações."

# Nome do arquivo onde o provérbio será salvo
nome_arquivo = "proverbio_confucio.txt"

# Escrever o provérbio no arquivo
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(proverbio)

print(f"Provérbio de Confúcio salvo no arquivo '{nome_arquivo}'.")