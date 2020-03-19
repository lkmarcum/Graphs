from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Queue, Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
map = {}

for room in world.rooms.items():
    exits = room[1].get_exits()
    map[room[0]] = {}
    for exit in exits:
        map[room[0]][exit] = '?'


def bfs(starting_point):
    q = Queue()
    q.enqueue([starting_point])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        current_room = path[-1]
        visited.add(current_room)
        for direction in map[current_room]:
            if map[current_room][direction] == '?':
                return path
            if map[current_room][direction] not in visited:
                path_copy = path.copy()
                path_copy.append(map[current_room][direction])
                q.enqueue(path)


def make_path():
    starting_room = player.current_room
    inv_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
    finished_rooms = set()

    s = Stack()
    s.push([starting_room.id])

    while s.size() > 0:
        path = s.pop()
        current_room = path[-1]
        print(f"Current room: {current_room}")
        if len(path) > 1:
            prev_room = path[-2]
            prev_direction = traversal_path[-1]
            map[prev_room][prev_direction] = current_room
            map[current_room][inv_directions[prev_direction]] = prev_room

            if '?' not in map[prev_room].values():
                finished_rooms.add(prev_room)
            if len(map[current_room]) == 1 and current_room not in finished_rooms:
                finished_rooms.add(current_room)

        if len(finished_rooms) == len(room_graph):
            return

        exits = []
        if '?' in map[current_room].values():
            exits = [key for (key, value)
                     in map[current_room].items() if value == '?']
        # elif '?' not in map[current_room].values() and len(map[current_room].items()) > 1:
        #     exits = [key for key in map[current_room].keys()]

        if len(exits) > 0:
            next_direction = random.choice(exits)
            next_room = world.rooms[current_room].get_room_in_direction(
                next_direction).id
            traversal_path.append(next_direction)
            path.append(next_room)
            s.push(path)
        else:
            pass

            # q = Queue()
            # q.enqueue([current_room])
            # visited = set()
            # while q.size() > 0:
            #     path = q.dequeue()
            #     current_room = path[-1]
            #     visited.add(current_room)
            #     for direction in map[current_room]:
            #         if map[current_room][direction] == '?':
            #             return path
            #         if map[current_room][direction] not in visited:
            #             path_copy = path.copy()
            #             path_copy.append(map[current_room][direction])
            #             q.enqueue(path)

    return


print(make_path())
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
