

Nota1 = float(input("Digite Nota 1: "))
Nota2 = float(input("Digite Nota 2: "))
Nota3 = float(input("Digite Nota 2: "))


Soma = ((Nota1) + (Nota2) + (Nota3))/3


if Soma >= 7:
    print(f"Aluno aprovado com {Soma} na média")
elif 3.5 < Soma < 7:
    print(f"Aluno foi para a recuperação com {Soma} na média")

else:
    print (f"Aluno reprovado com {Soma} na media") 