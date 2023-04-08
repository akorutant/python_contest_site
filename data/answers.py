import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Contests(SqlAlchemyBase):
    __tablename__ = "contests"

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    true_answers = sqlalchemy.Column(sqlalchemy.Boolean, nullable=False)
    contest_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey('contests.id'))
    contests = orm.relationship('Contests')



