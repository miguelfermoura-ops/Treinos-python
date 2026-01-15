import time
import builtins
from aluno import Aluno, remover_acentos
from treinamento import treinos #importando treinos do outro arquivo

#Costumização do print para efeito de Digitação
def print(*args, **kwargs):
    texto = " " .join(map(str, args) )
    for letra in texto:
        builtins.print(letra, end='', flush = True)
        time.sleep(0.09)
    builtins.print()

# Boas-vindas
print("Olá, seja bem-vindo ao seu programa particular de treino individualizado.\n Eu, Treinador Miguelito, vou montar sua rotina de treinamentos.")
nome= input("Antes de começar, informe o seu nome: ").strip().capitalize()
#função para escolher o tipo de treino
usuario = Aluno(nome)
usuario.escolher_treino()
musculo_nome = usuario.escolha_musculo()
ficha = treinos[musculo_nome]
print("-" *30 )
print(f"Certo! seu treino de {musculo_nome} é:")
print(ficha[usuario.objetivo])
print(f"Agora é com você, {usuario.nome}. Realize os exercícios com cuidado e não se esqueça de\n se alimentar e se hidratar bem.")







