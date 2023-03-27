from client import VivisystemClient
from models import EventType, VivisystemFish, VivisystemPond
import sys
import time
import random


# connect to default port
# try testing by running multiple clients with different pond_id
pond_id = "matrix-pond" if len(sys.argv) < 2 else sys.argv[1]
vivi = VivisystemClient("ws://127.0.0.1:5000", pond_id=pond_id)
connected_ponds = set()

# register your handlers


def handle_status(pond: VivisystemPond):
    # will receive this model, use it as you wish
    # see the model for other properties
    pond_origin = pond.name
    total_fishes = pond.total_fishes
    print(pond_origin, total_fishes)
    connected_ponds.add(pond_origin)
    print('connected ponds: ', connected_ponds)


def handle_disconnect(pond_id: str):
    # e.g. pond_id = "matrix-pond",
    print(pond_id, "disconnected")
    if pond_id in connected_ponds:
        connected_ponds.remove(pond_id)
        print('connected ponds: ', connected_ponds)


def handle_migrate(fish: VivisystemFish):
    # will receive this fish model, map it into your own model, then whatever
    print(fish, "received")


vivi.handle_event(EventType.STATUS, handle_status)
vivi.handle_event(EventType.DISCONNECT, handle_disconnect)
vivi.handle_event(EventType.MIGRATE, handle_migrate)

# Sending messages

# Send Pond Status, do this every 2 seconds
# map fields with your own pond
pond = VivisystemPond(name=pond_id, total_fishes=200, pheromone=50)
vivi.send_status(pond)

# Migrate Fish, based on your fish conditions
# map to your own fish
fish = VivisystemFish(fish_id=301301, parent_id=105151, genesis=pond_id,
                      crowd_threshold=100, pheromone_threshold=50, lifetime=40)
# choose your destination, other pond_id's
if connected_ponds:
    random_pond = random.choices(list(connected_ponds))
    vivi.migrate_fish(random_pond, fish)

# more example, send status & try to migrate every 2 second
start = time.time()
while True:
    current_time = time.time()
    if current_time - start >= 2:
        pond = VivisystemPond(name=pond_id, total_fishes=200, pheromone=50)
        vivi.send_status(pond)
        # try to migrate fish, if there are connected ponds
        if connected_ponds:
            random_pond = random.choice(list(connected_ponds))
            vivi.migrate_fish(random_pond, fish)

        start = current_time
