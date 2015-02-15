import engine
game_map = engine.Map()

room_1 = engine.Room("That room", "it's neat")
room_2 = engine.Room("The other room", "it's not neat")
game_map.add_room(room_1)
game_map.add_room(room_2)

game_map.connect_rooms(room_1, room_2, "n")
