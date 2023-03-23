from dataclasses import dataclass

from enum import Enum
import pickle


class ActionType(Enum):
    CONNECT = 1
    DISCONNECT = 2
    STATUS = 3
    MIGRATE = 4


class Payload:
    def __init__(self, action: ActionType, data=object):
        self.action = action
        # data is either fish or pond below
        self.data = data


@dataclass
class VivisystemPond:
    name: str
    total_fishes: int = 0
    pheromone: float = 0


@dataclass
class VivisystemFish:
    fish_id: int
    parent_id: int
    genesis: str
    state: str
    status: str
    crowd_threshold: int
    pheromone_threshold: int
    lifetime: int
