from unittest.mock import patch
from src.main import *
import pytest
import pytest_asyncio



@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Emanuel", curso ="Devops", ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result

@pytest.mark.asyncio
async def test_update_estudante_negativo():
    result = await update_estudante(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positivo():
    result = await update_estudante(10)
    assert result
@pytest.mark.asyncio

async def test_delete_estudante_positivo(id_estudante: int):
    result = await delete_estudante(10)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negativo(id_estudante: int):
    result = await delete_estudante(-5)
    assert not result



