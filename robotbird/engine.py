class HasInventory(object):
    def __init__(self):
        self.inventory = {}
    def add_item(self, item):
        self.inventory[item.name] = item
    def remove_item(self, item_name):
        return self.inventory.pop(item_name)

class Room(HasInventory):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description
        self.exits = {}
    def connect(self, direction, room, locked = False):
        self.exits[direction] = Door(room, locked)

class Door(object):
    def __init__(self, target, locked = False):
        self.target = target
        self.locked = locked

class Map(object):
    DIRECTIONS = {"n": "s",
                  "s": "n",
                  "e": "w",
                  "w": "e"}
    def __init__(self):
        self.rooms = {}
    def add_room(self, room):
        self.rooms[room.name] = room
    def connect_rooms(self, room_from, room_to, direction, two_way = True):
        room_from.connect(direction, room_to)
        if two_way:
            room_to.connect(Map.DIRECTIONS[direction], room_from)
    def move_item(self, source, destination, item_name):
        item = source.remove_item(item_name)
        destination.add_item(item)

class Entity(HasInventory):
    def __init__(self, name, description):
        super().__init__()
        self.name = name
        self.description = description

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
