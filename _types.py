
from typing import TypedDict, List, Any, Union, Dict, Tuple, Optional, Protocol
            

class Task(TypedDict):
    description: str
    title: str
    deadline: str
    SOP: str

class BackLogTasklist(TypedDict):
    tasks: list[Task]


class CompletedTask(TypedDict):
    title: str
    description: str
    time_taken: str

class CompletedTasklist(TypedDict):
    completed_tasks: list[CompletedTask]
