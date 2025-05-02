import random
import string

def gerar_senha(comprimento, usar_caracteres_especiais = True):
    # Define os conjuntos de caracteres a serem usados
    caracteres = string.ascii_letters + string.digits
    if usar_caracteres_especiais:
        caracteres += string.punctuation #Inclui caracteres especiais

    # Gera a senha aleatório
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def menu ():
    print("===== Gerador de Senha Alratória =====")

    while True:
        try:
            comprimento = int(input("Digite o comprimento desejado para a senha: "))
            if comprimento < 6:
                print ("A senha deve ter pelo menos 6 caracteres.")
                continue
            break
        except ValueError:
            print("Por favor, inisra um número válido.")

    usar_caracteres_especiais = input ("Deseja incluir caracteres especiais? (sim/não): ").strip().lower() == 'sim'

    senha = gerar_senha(comprimento, usar_caracteres_especiais)
    print(f"\nSua senha gerada é: {senha}")

    continuar = input("\nDeseja gerar outra senha? (sim/não): ").strip().lower()
    if continuar != 'sim':
        print("Até logo!")
        return  
#Iniciar o menu
menu()