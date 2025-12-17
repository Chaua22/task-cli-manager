from storage import salvar, carregar
class TaskManager:
    def __init__(self):
        self.tarefas = carregar()

    def add_task(self, descricao):
        nova_tarefa = {
            'id': len(self.tarefas) + 1,
            'description': descricao, 
            'done': False
        }
        self.tarefas.append(nova_tarefa)
        salvar(self.tarefas)

    def list_task(self):
        return self.tarefas
    def mark_done(self, task_id):
        for task in self.tarefas:
            if task ['id'] == task_id:
                task['done'] = True
                salvar(self.tarefas)
                return True 
            return False
        