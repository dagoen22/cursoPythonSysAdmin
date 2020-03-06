#!/usr/bin/env python3

def vermelho(falar):
    def alterar_cor(texto):
        return f'\033[91m{texto}\033[0m'
    return alterar_cor

@vermelho
def falar(texto):
    return texto

print(falar('Olá mundo'))