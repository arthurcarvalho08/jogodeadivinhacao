import random
print("##########################")
print("#         JOGO DE        #")
print("#       ADIVINHAÇÃO      #")
print("#                        #")
print("#         ARTHUR         #")
print("##########################")

print("         *********        ")
print("       *           *      ")
print("      *  (O)   (O)  *     ")
print("     *               *    ")
print("     *               *    ")
print("     *     *****     *    ")
print("      *             *     ")
print("        ***********       ")

numeroSecreto = random.randrange(0, 100)
totalTentativas = 0
pontos = 100