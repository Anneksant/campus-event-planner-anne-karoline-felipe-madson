# estudanteb.py - Módulo de Interação com Usuário e Relatórios (Anne - Estudante B)

import os
import sys

# adiciona estudanteA-feature ao sys.path de forma simples e direta (caminho absoluto)
_estudanteA = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "estudanteA-feature"))
if _estudanteA not in sys.path:
    sys.path.insert(0, _estudanteA)

import funcoes_eventos as funcoes

def display_menu(): 
    print("\n=== Planejador de Eventos ===") 
    print("1. Adicionar evento") 
    print("2. Ver todos os eventos") 
    print("3. Buscar evento por nome") 
    print("4. Deletar evento por ID") 
    print("5. Sair") 