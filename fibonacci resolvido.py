n = int(input("Termo que deseja encontrar:"))
ultimo = 0
penultimo = 1
# comentario
# cheio de ; num tem ; em python
# ultimo estava declarado como 1, tinha que ser 0
# não precisa desse if
# input tava declarado como char e não int
# não precisa printar o termo no final
# count deveria ser 3 ao invés de 6

print("{}, {}".format(ultimo, penultimo), end = "")

count = 3

while count <= n:
    termo = ultimo + penultimo
    print(", {}".format(termo), end = "")
    ultimo = penultimo
    penultimo = termo
    count += 1
 
