import flask_restful as restful

from api.common.db import get_db


class Tucao(restful.Resource):
    def __init__(self):
        self.db = get_db()

    def get(self, comment_parent):
        sql = 'SELECT * FROM tucao WHERE comment_parent = (?)'
        data = self.db.execute(sql, (comment_parent,)).fetchall()

        return {
            'code': 0,
            'data': data
        }
