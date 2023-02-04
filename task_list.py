
from _base import db
import json
from sqlalchemy import Column, Integer, String
from _types import *
from sqlalchemy.orm import relationship


class TaskList(db.Model):

    __tablename__ = 'task_lists'
    id = Column(Integer, primary_key=True)
    stage = Column(String, nullable=False)
    tasks = relationship("Task", backref="task_lists")

    @property
    def rows(self):
        return list(filter(lambda item: item is not None, [k if not k.startswith("_") else None for k in self.__dict__.keys()]))

    @property
    def public_attributes(self):
        return {row: self.__dict__[row] for row in self.rows}

    def __repr__(self) -> str:
        return f"{self.__tablename__}{json.dumps({ k : self.__dict__[k] for k in self.rows}, indent=2)}\n"
