import flask_restful as restful

from api.common.db import get_db


class QaHole(restful.Resource):
    def __init__(self):
        self.db = get_db()
        self.error = None

    def get(self, comment_id=None):
        if self.db.execute(
            'SELECT * FROM qahole LIMIT 1'
        ).fetchone() is None:
            self.error = 'Database is empty.'

        if self.error:
            return {
                'code': -1,
                'error': self.error
            }

        if comment_id:
            sql = 'SELECT * FROM qahole WHERE comment_id = (?)'
            data = self.db.execute(sql, (comment_id,)).fetchall()
        else:
            sql = 'SELECT * FROM qahole ORDER BY comment_id DESC LIMIT 100'
            data = self.db.execute(sql).fetchall()

        return {
            'code': 0,
            'data': [dict(x) for x in data]
        }
