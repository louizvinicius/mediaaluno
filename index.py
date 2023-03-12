
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if (media >= 9.0) and (media <= 10):
    print(f"\n**********\n Nota 1: {nota1}\n Nota 2: {nota2}\n Media: {media} Conceito: A\n APROVADO!")

if (media >= 7.5) and (media <= 8.9):
    print(f"\n**********\n Nota 1: {nota1}\n Nota 2: {nota2}\n Media: {media} Conceito: B\n APROVADO!")

if (media >= 6.0) and (media <= 7.4):
    print(f"\n**********\n Nota 1: {nota1}\n Nota 2: {nota2}\n Media: {media} Conceito: C\n APROVADO!")

if (media >= 4.0) and (media <= 5.9):
    print(f"\n**********\n Nota 1: {nota1}\n Nota 2: {nota2}\n Media: {media} Conceito: D\n REPROVADO!")

if (media >= 0) and (media <= 3.9):
    print(f"\n**********\n Nota 1: {nota1}\n Nota 2: {nota2}\n Media: {media} Conceito: E\n REPROVADO!")