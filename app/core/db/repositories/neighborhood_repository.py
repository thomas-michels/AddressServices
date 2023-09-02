from app.core.db import DBConnection
from app.core.db.repositories.base_repository import Repository
from app.core.entities import NeighborhoodInDB
from app.core.configs import get_logger

_logger = get_logger(__name__)


class NeighborhoodRepository(Repository):
    def __init__(self, connection: DBConnection) -> None:
        super().__init__(connection)

    async def insert(self, name: str) -> NeighborhoodInDB:
        try:
            query = """
            INSERT INTO public.neighborhoods("name")
            VALUES(%(name)s)
            RETURNING id, name;
            """

            raw_neighborhood = await self.conn.execute(
                sql_statement=query, values={"name": name}
            )

            if raw_neighborhood:
                return NeighborhoodInDB(**raw_neighborhood)

        except Exception as error:
            _logger.error(f"Error: {str(error)}. Data: {dict(name=name)}")

    async def select_by_id(self, id: int) -> NeighborhoodInDB:
        try:
            query = 'SELECT id, "name" FROM public.neighborhoods WHERE id=%(id)s;'

            raw_neighborhood = await self.conn.execute(sql_statement=query, values={"id": id})

            if raw_neighborhood:
                return NeighborhoodInDB(**raw_neighborhood)

        except Exception as error:
            _logger.error(f"Error: {str(error)}. Data: {dict(id=id)}")

    async def select_by_name(self, name: str) -> NeighborhoodInDB:
        try:
            query = "SELECT id, name FROM public.neighborhoods WHERE name ILIKE %(name)s ESCAPE '';"

            raw_neighborhood = await self.conn.execute(
                sql_statement=query, values={"name": "%{}%".format(name)}
            )

            if raw_neighborhood:
                return NeighborhoodInDB(**raw_neighborhood)

        except Exception as error:
            _logger.error(f"Error: {str(error)}. Data: {dict(name=name)}")
