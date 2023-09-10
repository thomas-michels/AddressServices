import pytest
from unittest.mock import AsyncMock
from app.core.db.repositories.neighborhood_repository import NeighborhoodRepository
from app.core.entities import NeighborhoodInDB
from tests.core.db import mock_connection

@pytest.fixture
def neighborhood_repository(mock_connection):
    conn = NeighborhoodRepository(connection=mock_connection)
    conn.execute = AsyncMock()
    return conn

@pytest.mark.asyncio
async def test_insert(neighborhood_repository):
    neighborhood_repository.conn.execute.return_value = {
        "id": 1,
        "name": "Neighborhood 1",
    }

    result = await neighborhood_repository.insert("Neighborhood 1")

    assert isinstance(result, NeighborhoodInDB)
    assert result.name == "Neighborhood 1"

@pytest.mark.asyncio
async def test_select_by_id_found(neighborhood_repository):
    neighborhood_repository.conn.execute.return_value = {
        "id": 1,
        "name": "Neighborhood 1",
    }

    result = await neighborhood_repository.select_by_id(1)

    assert isinstance(result, NeighborhoodInDB)
    assert result.id == 1

@pytest.mark.asyncio
async def test_select_by_id_not_found(neighborhood_repository):
    neighborhood_repository.conn.execute.return_value = None

    result = await neighborhood_repository.select_by_id(999)

    assert result is None

@pytest.mark.asyncio
async def test_select_by_name_found(neighborhood_repository):
    neighborhood_repository.conn.execute.return_value = {
        "id": 1,
        "name": "Neighborhood 1",
    }

    result = await neighborhood_repository.select_by_name("Neighborhood 1")

    assert isinstance(result, NeighborhoodInDB)
    assert result.name == "Neighborhood 1"

@pytest.mark.asyncio
async def test_select_by_name_not_found(neighborhood_repository):
    neighborhood_repository.conn.execute.return_value = None

    result = await neighborhood_repository.select_by_name("Nonexistent Neighborhood")

    assert result is None