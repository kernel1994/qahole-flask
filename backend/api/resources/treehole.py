import flask_restful as restful

from api.common.db import get_db


class Treehole(restful.Resource):
    def __init__(self):
        self.db = get_db()

    def get(self, comment_id=None):
        if comment_id:
            sql = 'SELECT * FROM qahole WHERE comment_id = (?) AND t_type = (?)'
            data = self.db.execute(sql, (comment_id, 'treehole')).fetchall()
        else:
            sql = 'SELECT * FROM qahole WHERE t_type = (?) ORDER BY comment_id DESC LIMIT 20'
            data = self.db.execute(sql, ('treehole',)).fetchall()

        return {
            'code': 0,
            'data': data
        }
