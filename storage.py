import json
FILE_NAME = 'tarefas.json'

def salvar(tarefas):
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)
def carregar():
    try: 
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return[]