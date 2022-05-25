from datetime import datetime

import pytest
from model_bakery import baker

from mytodo.models import Tarefa
from mytodo.services import tarefa_service


def test_should_get_tarefa_as_pending(db):
    my_tarefa = baker.make(Tarefa, description='Create an ansible deploy script', due_to=datetime.now())

    assert my_tarefa.status == 'pending'


def test_should_get_tarefa_as_done(db):
    my_tarefa = baker.make(Tarefa, description='Create an ansible deploy script', due_to=datetime.now())

    tarefa_updated = tarefa_service.mark_as_done(my_tarefa.id)

    assert tarefa_updated.status == 'done'


def test_should_raise_an_erro_for_invalid_tarefa_id(db):
    invalid_tarefa = 0
    with pytest.raises(RuntimeError) as error:
        tarefa = tarefa_service.mark_as_done(invalid_tarefa)

    assert str(error.value) == f"Tarefa ID: {invalid_tarefa} invalida"


def test_should_mark_as_undone(db):
    my_tarefa = baker.make(
        Tarefa,
        description='Create an ansible deploy script',
        due_to=datetime.now(),
        done=True)

    tarefa_updated = tarefa_service.mark_as_done(my_tarefa.id)

    assert tarefa_updated.status == 'pending'
