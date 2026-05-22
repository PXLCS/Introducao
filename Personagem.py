# Sistema de Cadastrar Personagem
#Entrada de Dados

def calcular_nivel(f1, d2):
    nivel = (f1 + d2) / 2
    return nivel

def verificar_nivel(nivel):
    if nivel >= 100:
        return "Nível 50 (Forte)"
    elif nivel >= 50:
        return "Nível 25 (Mediano)"
    else:
         return "Personagem Fraco"
    
def main():

        print("Sistema de Nível")

        continuar = "s"

        while continuar == "s":
            nome = input ("Digite o Nome do Personagem: ")

            for1 = float(input("Digite o Nível de Forca: "))
            des2 = float(input("Digite o Nível de Destreza: "))

            nivel = calcular_nivel(for1, des2)

            status = verificar_nivel(nivel)

            print (" --- Resultado --- ")
            print (f"Personagem: {nome}")
            print (f"Nível: {nivel} ")
            print (f"Status: {status}")

            continuar = input(" Deseja criar outro Personagem?(s/n)").lower()

main()