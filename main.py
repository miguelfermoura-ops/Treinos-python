import time
import builtins
import unicodedata 
from treinamento import treinos #importando treinos do outro arquivo

def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')
#Costumização do print para efeito de Digitação
def print(*args, **kwargs):
    texto = " " .join(map(str, args) )
    for letra in texto:
        builtins.print(letra, end='', flush = True)
        time.sleep(0.09)
    builtins.print()

# Boas-vindas
print("Olá, seja bem-vindo ao seu programa particular de treino individualizado.\n Eu, TREINADOR MIGUELITO, vou montar sua rotina de treinamentos.")
nome= input("Antes de começarmos, informe seu nome: ").strip().capitalize()
#função para escolher o tipo de treino
def escolher_treino():
    opcoes = {"forca": "força", "resistencia": "resistencia", "hipertrofia": "hipertrofia"}
    while True:
        print(f"""Certo, {nome} para começar, me conta qual o seu objetivo?
Força
Resistência
Hipertrofia""")
        entrada = input().strip().lower()
        escolha_treino = remover_acentos(entrada)  # Captura, limpa espaços, padroniza letras minúsculas e remove acentos
        if escolha_treino in opcoes:
            return escolha_treino
        else:
            print("Opção inválida, tente novamente!")

def escolha_musculo():
    opcoes = {"1": "peito", "2": "costas", "3": "pernas"}
    while True:
        print(f"""Ótimo, {nome} agora escolha o musculo que você deseja treinar:
1 - PEITO/OMBRO/TRICEPS
2 - COSTAS/BICEPS
3 - PERNAS""")
        musculo = input().strip().lower()
        if musculo in opcoes:
            return opcoes[musculo]
        else:
            print("Opção invalida, tente novamente!")
            
treino = escolher_treino()
musculo = escolha_musculo()
treino_escolhido = treinos[musculo]
print(f"Certo! seu treino de {treino_escolhido ['nome']} é:")
print(treino_escolhido[treino])







