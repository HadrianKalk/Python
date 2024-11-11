#Usando a função Print. O SEP indica qual sera o separador das strings na função, pode ser com "" ou com ''
print(1, 2, 3, 4, sep="-")

# CRLF é o quebrador de linhas do Windows. Ele adiciona automaticamente uma quebra de linha no compilador, que no caso é /r/n.
# LF utiliza /n apenas

# A função end adiciona no fim da string.
print("TESTE DE FIM", end="\r\n")
print("TESTE DE FIM", end="###")