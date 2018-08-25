class Node:
    def __init__(self, value, dot=None, dash=None):
        self.value = value
        self.dot = dot
        self.dash = dash
        self.oval = None
        self.line = None


class DecodeTree:
    def __init__(self):
        self.root_node = Node("",
                              Node("E",
                                   Node("I",
                                        Node("S",
                                             Node("H",
                                                  Node("5"),
                                                  Node("4")),
                                             Node("V",
                                                  None,
                                                  Node("3"))),
                                        Node("U",
                                             Node("F"),
                                             Node("",
                                                  Node("",
                                                       Node("?"),
                                                       Node("-")),
                                                  Node("2")))),
                                   Node("A",
                                        Node("R",
                                             Node("L"),
                                             Node("",
                                                  Node("+",
                                                       None,
                                                       Node(".")))),
                                        Node("W",
                                             Node("P",
                                                  None,
                                                  Node("",
                                                       Node("@"))),
                                             Node("J",
                                                  None,
                                                  Node("1"))))),
                              Node("T",
                                   Node("N",
                                        Node("D",
                                             Node("B",
                                                  Node("6",
                                                       None,
                                                       Node("-")),
                                                  Node("=")),
                                             Node("X",
                                                  Node("/"))),
                                        Node("K",
                                             Node("C",
                                                  None,
                                                  Node("",
                                                       Node(";"))),
                                             Node("Y",
                                                  Node("(",
                                                       None,
                                                       Node(")"))))),
                                   Node("M",
                                        Node("G",
                                             Node("Z",
                                                  Node("7"),
                                                  Node("",
                                                       None,
                                                       Node(","))),
                                             Node("Q")),
                                        Node("O",
                                             Node("",
                                                  Node("8",
                                                       Node(":"))),
                                             Node("",
                                                  Node("9"),
                                                  Node("0"))))))

        self.current_node = self.root_node

    def reset(self):
        self.current_node = self.root_node

    def dash(self):
        if self.current_node and self.current_node.dash:
            self.current_node = self.current_node.dash

    def dot(self):
        if self.current_node and self.current_node.dot:
            self.current_node = self.current_node.dot

    def is_char_available(self):
        return self.current_node != self.root_node

    def current_char(self):
        if self.current_node and self.current_node.value:
            return self.current_node.value
        else:
            return None

