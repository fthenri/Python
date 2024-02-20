# \r\n > CRLF > windows
# \n > LF > outros sistemas baseados em unix 
print(12, 34, 1000, sep=' ', end='#\n'),
print(56, 78, sep=" ", end="\n"),
print(9, 10, sep=' ', end="\r\n")

# (sep="digito para separar cada valor") no meu caso utilizei o proprio espaço que é o padrao
#exemplo do padrao sem o (sep=)

print(23, 23)

#pode notar que o padrão é um espaço
#outro teste separando com um caracter

print(23, 23, sep="-")