import random
print("##########################")
print("#         JOGO DE        #")
print("#       ADIVINHAÇÃO      #")
print("#                        #")
print("#         ARTHUR         #")
print("##########################")
print(".")
print(".")
print(".")
print("Este é você!")
print(".")
print("         *********        ")
print("       *           *      ")
print("      *  (O)   (O)  *     ")
print("     *               *    ")
print("     *       v       *    ")
print("     *               *    ")
print("     *     *****     *    ")
print("      *             *     ")
print("        *         *       ")
print("          *******         ")

numeroSecreto = random.randrange(0, 100)
totalTentativas = 0
pontos = 100

print("Quais níveis de dificuldade?")
print("(1)- Fácil (2)- Médio (3)- Difícil")

nivel = int(input("Escolha um nível:"))

if nivel == 1:
    print("20 tentativas? Fraco demais!")
    totalTentativas = 20
elif nivel == 2:
    print("10 tentativas? Ah, até vai ein...")
    totalTentativas = 10
elif nivel == 3:
    totalTentativas = 5
    print("5 TENTATIVAS????? VOCÊ É LOUCO OU CORAJOSO??????")
