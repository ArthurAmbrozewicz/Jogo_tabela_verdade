import random 
import ttg
import time
jogo = 1
suspeitos = ["A Secretária", "O Guarda Costas", "A Faxineira", "O Vice Presidente", "A Primeira Dama", "O Cozinheiro"]
locais = ["na Cozinha", "no Salão Oval"," na Sala de Reuniões", "na Varanda", "no jardim","no Banheiro"]
random.shuffle(locais)
random.shuffle(suspeitos)
dicas = [
    f"{suspeitos[0]} estava {locais[1]}.",
    f"Se {suspeitos[0]} estava {locais[1]}, {suspeitos[1]} estava {locais[4]}.",
    f"Se {suspeitos[1]} estava {locais[0]}, {suspeitos[3]} estava {locais[3]}.",
    f"{suspeitos[4]} nunca esteve com {suspeitos[0]}.",
    f"Se {suspeitos[4]} estava {locais[1]}, {suspeitos[2]} estava {locais[5]}.",
    f"Ou {suspeitos[0]} estava {locais[0]} ou {suspeitos[5]} estava {locais[2]}.",
    f"Crime aconteceu {locais[5]}, e só havia uma pessoa lá.",
    f"Se {suspeitos[5]} estava {locais[2]}, {suspeitos[3]} estava {locais[1]}.",
    f"Se {locais[1]} tem mais de uma pessoa, {suspeitos[4]} estava {locais[3]}.",
    f"Se {suspeitos[4]} estava {locais[3]}, ou {suspeitos[0]} estava {locais[1]} ou {suspeitos[2]} estava {locais[0]}."
]
random.shuffle(dicas)

print("Em uma noite tensa, no auge da madrugada na Casa Branca, um disparo ecoou pelos corredores,")
time.sleep(1.5)
print("interrompendo abruptamente uma reunião silenciosa. O presidente do país está morto, e todos")
time.sleep(1.5)
print("estão em choque. Os suspeitos estão próximos, cada um com uma possível motivação escondida.\n")
time.sleep(1.5)
print("O guarda-costas, sempre ao lado do presidente, tem o olhar afiado e a postura firme, mas")
time.sleep(1.5)
print("há algo de inquietante em seu silêncio.")
time.sleep(1.5)
print("A primeira-dama, ainda em estado de choque, parece distante e evita o contato visual.")
time.sleep(1.5)
print("O vice-presidente, conhecido por suas ambições, apresenta um nervosismo que vai além do esperado.")
time.sleep(1.5)
print("O cozinheiro, sujo de ingredientes, esconde as mãos tremendo ligeiramente, como se temesse")
time.sleep(1.5)
print("ser interrogado.")
print("A faxineira, humilde e discreta, desvia o olhar rapidamente, enquanto a secretária, sempre")
time.sleep(1.5)
print("atenta a tudo, observa a cena como se calculasse o próximo movimento.\n")
time.sleep(1.5)

print("Agora, você deve solucionar esse crime o mais rápido possível e identificar o criminoso")
print("antes que tudo seja encoberto.") 
time.sleep(1.5)
print("Boa sorte, e que Deus cuide do futuro dessa nação!")


opcoes = ["1-Mais uma dica", "2-Escolher o culpado", "3-Sair do jogo "]
suspeitos_ordenado = ["Secretária", "Guarda Costas", "Faxineira", "Vice Presidente", "Primeira Dama", "Cozinheiro"]
dicas_dadas = 0
while jogo == 1:
    print("________________________________________________________________________________________")
    assassino = suspeitos[2][2:]
    for i in opcoes:
        print(i)
    print("________________________________________________________________________________________")
    escolha = int(input("Qual ação você deseja tomar?"))
    if escolha == 1:
        print(dicas[dicas_dadas])
        print("________________________________________________________________________________________")
        dicas_dadas +=1
        continue
    elif escolha == 2:
        print("Certo, depois de muita dúvida, escolha o seu culpado:")
        for indice, suspeito  in enumerate(suspeitos_ordenado, start=1):
            print(f'{indice}-{suspeito}')

        print("________________________________________________________________________________________")
        escolha_do_assassino = int(input())
        if suspeitos_ordenado[escolha_do_assassino-1]== assassino:
            print(f"Parabéns o misterio foi resolvido!") 
            if assassino[-1] == "a":
                print(f"quem matou o Sr. Presidente foi a {assassino}")
            else:
                print(f'Quem matou o Sr. Presidente foi o {assassino}')
            if dicas_dadas == 0:
                print("Você precisou de nenhuma dica para resolver o mistério")
                break
            elif dicas_dadas >0 and dicas_dadas < 9:
                print(f"Você só precisou de {dicas_dadas} dicas, parabéns!")
                break
            else:
                print(f"Você precisou de {dicas_dadas} dicas, foi por pouco, mas o importante é resolver o caso")
                break
        else:
            print("Você prendeu um inocente")
            del suspeitos_ordenado[escolha_do_assassino-1]
    else:
        break
# DEDUÇÕES (Foram assumidos valores para os suspeitos e locais, já que no código isso é aleatório (518400 possibilidades diferentes de jogo) )
#pista 1 e pista 2: secretaria no salao oval entao cozinheiro no jardim 
# pista 3 é falsa 
# pista 7 o homicídio ocorreu no banheiro, e quem estava lá foi o culpado
# pista 4,5 e 1 se a primeira dama nunca esteve com a secretaria ela nao pode estar no salao oval 
#pista 6 e 1 como a secretaria esta não está na cozinha o cozinheiro está na sala de reuniões
#pista 8 e 6 como o cozinheiro esta na sala de reuniões, o vice presidente esta no salao oval 
#pista 9,8 e 1 tem duas pessoas no salao ovao(vice presidente e secretaria) entao a primeira dama esta na varanda
#pista 9 10 e 1 a primeira dama esta na varanda e já que é uma coisa ou outra, ja sabemos que a secretária esta no salão oval/
# então a faxineira não está na cozinha 
# usando todas as dicas (em especial a 7 ) somente a faxineira não tem um lugar definido, então só ela pode estar no banheiro.

# COMPROVAÇÃO DAS DICAS COM TABELA VERDADE:
dica1 = ttg.Truths(["p", "q"], ["p => ~q"]) # A secretaria está no salão oval, então ela não está na cozinha

# p = secretaria no salao oval
# q = secretaria na sala

dica2 = ttg.Truths(["p", "r"], ["p => r"])#Se a secretaria estava no salão oval, o guarda costas estava no jardim
# p = secretaria no salao oval
# r = guarda costas no jardim

dica3 = ttg.Truths(["s", "t"], ["s => t"])# Se o guarda costas estava na cozinha, o vice presidente estava na varanda
# s guarda costas na cozinha
# t vice presidente na varanda

dica4 = ttg.Truths(["p", "u"], ["p and ~u)"]) #A primeira dama nunca esteve com a secretaria
# p secretaria no salão oval
# u primeira dama no salão oval

dica5 = ttg.Truths(["v", "w"], ["v => w"])#Se a primeira dama estava no salão oval, a faxineira estava na sala de reuniões

# v primeira dama no salão oval
# w faxineira na sala de reuniões

dica6 = ttg.Truths(["w", "x"], ["(w or x) and not (w and x)"])#Ou a secretaria estava na cozinha ou cozinheiro estava na sala de reuniões
# w ou a secretaria esta na cozinha
# x ou o cozinheiro esta na sala de reunioes

dica7 = ttg.Truths(["y", "z"], ["y and z"])# O crime aconteceu no banheiro, e só havia uma pessoa lá 
# y O crime aconteceu no banheiro 
# z Só havia uma pessoa lá

dica8 = ttg.Truths(["x", "a"], ["x => a"] ) #Se o cozinheiro estava na sala de reuniões, então o vice presidente estava no salão oval
# x cozinheiro na sala de reuniões
# a vice presidente no salao oval

dica9 = ttg.Truths(["b", "c"], ["b => c"]) #Se no salão oval, tem mais de uma pessoa, a primeira dama estava na varanda
# b salão oval com mais de uma pessoa
# c primeira dama na varanda

dica10 = ttg.Truths(["c", "p", "d"], ["c =>((p or d) and not (p and d)) "]) #Se a primeira dama estava na varanda, ou a secretaria estava no salão oval ou a faxineira estava na cozinha
# c primeira dama na varanda
# p Secretaria no salão oval
# d Faxineira na cozinha



