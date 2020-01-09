from module.Vector2DInt import Vector2D
import copy


def get_vec2d_cartesian_num(in_vec):
    return abs(in_vec.x) + abs(in_vec.y)


class PathNode:
    pos, f, g, h, parent = Vector2D(), 0, 0, 0, None

    def __str__(self):
        return str(self.pos) + ' f:' + str(self.f) + ' g:' + str(self.g) + ' h:' + str(
            self.h) + '\n parent:' + str(self.parent)

    def __init__(self, in_pos=Vector2D()):
        self.pos = copy.deepcopy(in_pos)

    def init_member(self, start_pos, end_pos, in_g, in_parent=None):
        self.g = copy.deepcopy(in_g)
        self.h = get_vec2d_cartesian_num(end_pos - self.pos)
        self.f = self.g + self.h
        self.parent = in_parent


class MapNode:
    pos, type = Vector2D(0, 0), 0

    def __init__(self):
        self.pos, self.type = Vector2D(), 0

    def __init__(self, in_pos, in_type):
        self.pos, self.type = in_pos, in_type

    def __str__(self):
        return str(self.pos) + "," + str(self.type)


map_size = 6
scene_map = [[MapNode(Vector2D(x, y), 0) for y in range(map_size)] for x in range(map_size)]
dirs = [Vector2D(1, 0), Vector2D(1, 1), \
        Vector2D(0, 1), Vector2D(-1, 1), \
        Vector2D(-1, 0), Vector2D(-1, -1), \
        Vector2D(0, -1), Vector2D(1, -1)]
open_list = []
close_list = []


def make_wall(x, y):
    scene_map[x][y].type = 1


def show_map():
    for i in range(len(scene_map)):
        show_str = ""
        for j in range(len(scene_map[i])):
            show_str += str(scene_map[i][j])
            show_str += " "
        print(show_str)
    print('\n')


def show_map_block():
    for i in range(len(scene_map)):
        show_str = ""
        for j in range(len(scene_map[i])):
            show_str += str(scene_map[i][j].type)
            show_str += " "
        print(show_str)


def get_pos_type(pos):
    if 0 <= pos.x < map_size and 0 <= pos.y < map_size:
        return scene_map[pos.x][pos.y].type
    return 1


def get_min_f_node():
    cur_min = 9999
    ret = None
    for i in open_list:
        if i.f < cur_min:
            cur_min = i.f
            ret = i
    return ret


def is_in_list(list, pos):
    for i in list:
        if i.pos == pos:
            return True
    return False


def get_list_node(list, pos):
    for i in list:
        if i.pos == pos:
            return i
    return None


def start():
    start_pos = Vector2D(2, 1)
    end_pos = Vector2D(0, 5)
    make_wall(0, 1)
    make_wall(0, 2)
    make_wall(1, 2)
    make_wall(1, 3)
    make_wall(2, 3)
    make_wall(3, 3)
    make_wall(3, 2)
    make_wall(3, 1)
    start_node = PathNode(start_pos)
    start_node.init_member(start_node, end_pos, 0)
    open_list.append(start_node)
    show_map_block()
    while True:
        cur_node = get_min_f_node()
        if cur_node is None:
            break
        close_list.append(cur_node)
        open_list.remove(cur_node)
        for i in dirs:
            check_pos = cur_node.pos + i
            if get_pos_type(check_pos) > 0:
                continue
            if is_in_list(close_list, check_pos):
                continue
            step_cost = 10
            if abs(i.x) + abs(i.y) > 1:
                step_cost = 14
            if not is_in_list(open_list, check_pos):
                new_node = PathNode(check_pos)
                new_node.init_member(start_pos, end_pos, cur_node.g + step_cost, in_parent=cur_node)
                open_list.append(new_node)
            else:
                find_node = get_list_node(open_list, check_pos)
                if find_node.g > cur_node.g + step_cost:
                    find_node.init_member(start_pos, end_pos, cur_node.g + step_cost, cur_node)

        if is_in_list(close_list, end_pos) > 0:
            end_node = get_list_node(close_list, end_pos)
            print(end_node)
            break;

        if len(open_list) <= 0:
            print('error')
            break;
