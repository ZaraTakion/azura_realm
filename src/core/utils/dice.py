import random

def roll(dice: str) -> int:
    quantidade, lados = dice.lower().split('d')
    quantidade = int(quantidade)
    lados = int(lados)

    soma = 0
    for _ in range(quantidade):
        soma += random.randint(1, lados)

    return soma

def roll_d20() -> int:
    return random.randint(1, 20)
