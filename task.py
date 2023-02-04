from sqlalchemy import Column, Integer, String, ForeignKey
import json
from _base import db

class Task(db.Model):
    """Task is a class"""
    
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    title = Column(String)
    deadline = Column(String)
    SOP = Column(String)
    task_list_id = Column(Integer, ForeignKey('task_lists.id'))
    
    @property
    def rows(self):
        return list(filter(lambda item: item is not None, [k if not k.startswith("_") else None for k in self.__dict__.keys()]))

    @property
    def public_attributes(self):
        return {row: self.__dict__[row] for row in self.rows}

    def __repr__(self) -> str:
        return f"{self.__tablename__}{json.dumps({ k : self.__dict__[k] for k in self.rows}, indent=2)}\n"