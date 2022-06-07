class States:
    A = list()
    B = list()
    C = list()
    D = list()
    E = list()
    F = list()
    G = list()
    H = list()


class StateMachine:
    state = States.A

    def __init__(self):
        States.A.append(('erase', 0, States.B))
        States.B.append(('init', 1, States.C))
        States.C.append(('init', 2, States.D))
        States.C.append(('scale', 3, States.H))
        States.D.append(('init', 4, States.E))
        States.E.append(('wreck', 5, States.F))
        States.E.append(('scale', 6, States.B))
        States.E.append(('init', 7, States.G))
        States.E.append(('erase', 8, States.C))
        States.F.append(('scale', 9, States.G))
        States.G.append(('scale', 10, States.H))
        States.H.append(('erase', 11, States.A))

    def __get_next_node(self, method_name):
        found = None
        for node in self.state:
            if node[0] == method_name:
                found = node
                break
        return found

    def base_method(self, next_state):
        if next_state is not None:
            self.state = next_state[2]
            return next_state[1]
        else:
            raise KeyError("No such edge!")

    def erase(self):
        next_state = self.__get_next_node('erase')
        return self.base_method(next_state)

    def init(self):
        next_state = self.__get_next_node('init')
        return self.base_method(next_state)

    def scale(self):
        next_state = self.__get_next_node('scale')
        return self.base_method(next_state)

    def wreck(self):
        next_state = self.__get_next_node('wreck')
        return self.base_method(next_state)


def main():
    return StateMachine()
