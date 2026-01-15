#classes utilizadas no main
import unicodedata 
import time
import builtins

def print(*args, **kwargs):
    texto = " " .join(map(str, args) )
    for letra in texto:
        builtins.print(letra, end='', flush = True)
        time.sleep(0.09)
    builtins.print()
def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.objetivo = None
        self.musculo = None

    def escolher_treino(self):
        opcoes = {"forca": "força", "resistencia": "resistencia", "hipertrofia": "hipertrofia"}
        while True:
            print(f"""Perfeito, {self.nome} agora me diga: qual o seu objetivo?
Força
Resistência 
Hipertrofia""")
            entrada = input().strip().lower()
            escolha_treino = remover_acentos(entrada)  # Captura, limpa espaços, padroniza letras minúsculas e remove acentos
            if escolha_treino in opcoes:
             self.objetivo = escolha_treino
             return 
            else:
                print("Opção inválida, tente novamente!")

    def escolha_musculo(self):
        opcoes = {"1": "peito", "2": "costas", "3": "pernas"}
        while True:
            print(f"""ENTENDIDO! {self.nome}!\n Qual grupo muscular você deseja treinar hoje?
1 - PEITO/OMBRO/TRICEPS
2 - COSTAS/BICEPS
3 - PERNAS""")
            musculo = input().strip().lower()
            if musculo in opcoes:
                self.musculo = opcoes[musculo]
                return self.musculo
            else:
                print("Opção invalida, tente novamente!")
            