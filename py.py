import random  # Importação para gerar números aleatórios

# Função q inicia o jogo
def iniciar_jogo():
    print("jogo de adivinhação!")
    n_secreto = random.randint(1, 100)  # Gera um número entre 1 e 100
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))  # Interação com o usuário
            tentativas += 1

            # Estrutura de decisão
            if palpite < n_secreto:
                print("Tente um número maior!")
            elif palpite > n_secreto:
                print("Tente um número menor!")
            else:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
                break  # Sai do laço quando acerta
        except ValueError:
            print("Digite um número válido.")  # Tratamento de erro caso o usuário não digite um número

# Função principal
def jogar():
    while True:
        iniciar_jogo()
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()  # Interação com o usuário
        
        # Estrutura de decisão para continuar ou sair do jogo
        if jogar_novamente == 'n':
            print("Obrigado por jogar!")
            break
        elif jogar_novamente != 's':
            print("Entrada inválida. Encerrando o jogo.")
            break

# Chama a função principal
jogar()
