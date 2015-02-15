import json
import robotbird.engine

def load_dungeon(filename):
    dungeon = json.load(open(filename))

    items = {}
    map = engine.Map()

    for item in dungeon['items']:
        items[item['name']] = engine.Item(**item)
    for room in dungeon['rooms']:
        r = engine.Room(name=room['name'], description=room['description'])
        for item in room['items']:
            r.add_item(items[item])
        map.add_room(r)

    for exit in dungeon['exits']:
        map.connect_rooms(
            room_from=map.rooms[exit['from']],
            room_to=map.rooms[exit['to']],
            direction=exit['direction'],
            two_way=exit['two_way']
        )
    return map
