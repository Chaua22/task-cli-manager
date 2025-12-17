import argparse
from taskmanager import TaskManager
def main():
    parser = argparse.ArgumentParser(description='Gerenciador de Tarefas')
    parser.add_argument('command', help='Comando: add, list, done')
    parser.add_argument('content', nargs='?', help='Conteúdo, (tarefa ou ID)')

    args = parser.parse_args()
    manager = TaskManager()
    
    if args.command == 'add':
        if not args.content:
            print('Voce precisa informar a tarefa!')
            return
        manager.add_task(args.content)
        print(f'Tarefa adcionada: {args.content}')
    elif args.command == 'list':
        tasks = manager.list_task()
        if not tasks:
            print('Nenhuma tarefa encontrada.')
            return
        for task in tasks:
            status = '✔' if task.get('done') else '✘'
            print(f"{task['id']} - {task ['description']} {[{status}]}")

    elif args.command == 'done':
        if not args.content:
            print('Você precisa informar o ID da tarefa!')
            return
        manager.mark_done(int(args.content))
        print(f'Tarefa {args.content} marcada como concluída!')

    else:
        print('Comando inválido. Use: add, list ou done.')
if __name__ == '__main__':
    main()
