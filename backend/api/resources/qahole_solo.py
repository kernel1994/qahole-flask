import flask_restful as restful

from api.common.db import get_db


class QaHoleSolo(restful.Resource):
    def __init__(self):
        self.db = get_db()

    def get(self, comment_id):
        sql = 'SELECT * FROM qahole WHERE comment_id = (?)'
        comments = self.db.execute(sql, (comment_id,)).fetchall()

        sql = 'SELECT * FROM tucao WHERE comment_parent = (?)'
        tucaos = self.db.execute(sql, (comment_id,)).fetchall()

        return {
            'code': 0,
            'comment': comments[0],
            'tucaos': tucaos
        }
