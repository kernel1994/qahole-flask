import flask_restful as restful

from api.common.db import get_db


class Random(restful.Resource):
    def __init__(self):
        self.db = get_db()

    def get(self, number=None):
        if not number:
            number = 20

        sql = """
            SELECT *
            FROM qahole
            WHERE comment_id
            IN (
                SELECT comment_id
                FROM qahole
                ORDER BY RANDOM()
                LIMIT ?
            )
        """
        data = self.db.execute(sql, (number,)).fetchall()

        return {
            'code': 0,
            'data': data
        }
