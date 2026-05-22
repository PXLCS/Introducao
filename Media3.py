# Média Alunos

# Função Calcular Média

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media 

# Função Status do Aluno

def verificar_dados(media):
    if media >= 70:
        return "Aprovado"
    elif media >= 50:
        return "Recuperação"
    else:
        return "Reprovado"
    
    # Função Principal

def main():

        print("Sistema de Calculo da Média")

        continuar = "s"

        while continuar == "s":
            nome = input ("Digite o Nome do Aluno: ")

            nota1 = float(input("Digite a Primeira Nota: "))
            nota2 = float(input("Digite a Segunda Nota: "))

            media = calcular_media(nota1, nota2)

            status = verificar_dados(media)

            print ("/n------ Resultado ------")
            print (f"Aluno: {nome}")
            print (f"Média: {media} ")
            print (f"Status: {status}")

            continuar = input("/n Deseja cadastrar outro aluno?(s/n)").lower()

main()