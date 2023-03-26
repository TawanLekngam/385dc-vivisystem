from collections import namedtuple
from enum import Enum
import pickle

from typing import NamedTuple


class EventType(Enum):
    CONNECT = 1
    DISCONNECT = 2
    STATUS = 3
    MIGRATE = 4

class Payload:
    def __init__(self, action: EventType, data=object):
        self.action = action
        # data is either fish or pond below
        self.data = data

class VivisystemPond(NamedTuple):
    name: str
    total_fishes: int = 0
    pheromone: float = 0

class VivisystemFish(NamedTuple):
    fish_id: int
    parent_id: int
    genesis: str
    crowd_threshold: int 
    pheromone_threshold: int 
    lifetime: int # seconds, remaining lifetime or must elapsed?
