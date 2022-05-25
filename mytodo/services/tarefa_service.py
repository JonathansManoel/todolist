from mytodo.models import Tarefa


def mark_as_done(tarefa_id):
    tarefa = Tarefa.objects.filter(id=tarefa_id).first()
    if not tarefa:
        raise RuntimeError(f"Tarefa ID: {tarefa_id} invalida")

    tarefa.done = not tarefa.done
    tarefa.save()
    return tarefa
