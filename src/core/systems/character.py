from core.utils.modifiers import calc_mod
from core.utils.json_db import load_json, save_json

def validar_atributos(atributos: dict) -> bool:
    # Checa se todos entre 8 e 15
    for valor in atributos.values():
        if valor < 8 or valor > 15:
            return False
    
    # Soma exata deve ser 27
    if sum(atributos.values()) != 27:
        return False

    return True


def calcular_hp_inicial(classe: str, con_mod: int) -> int:
    classes = load_json('classes.json')
    
    if classe not in classes:
        raise ValueError(f"Classe '{classe}' não existe")
    
    hit_die = classes[classe]['hit_die']
    return hit_die + con_mod


def criar_personagem(user_id: str, nome: str, classe: str, atributos: dict):
    # Validar atributos
    if not validar_atributos(atributos):
        return {"erro": "Atributos inválidos. Devem somar 27 pontos e ficar entre 8 e 15."}

    con_mod = calc_mod(atributos["CON"])
    hp_inicial = calcular_hp_inicial(classe, con_mod)

    # Carregar db
    users = load_json('users.json')

    # Criar player
    users[user_id] = {
        "name": nome,
        "class": classe,
        "level": 1,
        "xp": 0,
        "attributes": atributos,
        "hp": {
            "max": hp_inicial,
            "current": hp_inicial
        },
        "inventory": [],
        "equipment": {}
    }

    save_json('users.json', users)

    return {
        "nome": nome,
        "classe": classe,
        "hp": hp_inicial,
        "atributos": atributos
    }
