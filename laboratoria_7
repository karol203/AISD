from typing import Any, List, Union, Callable


class TreeNode:
    def __init__(self, value, children=None):
        if children is None:
            children = []
        self.value = value
        self.children = children

    def __str__(self):
        return self.value

    def is_leaf(self) -> bool:
        if not self.children:
            return True
        else:
            return False

    def add(self, child: "TreeNode"):
        self.children.append(child)

    def for_each_deep_first_rec(self, visit: Callable[["TreeNode"], None]):
        visit(self)
        if self.children is not None:
            for i in range(len(self.children)):
                self.children[i].for_each_deep_first_rec(visit)

    def for_each_breadth_first(self, visit: Callable[["TreeNode"], None]) -> None:

        fifo = []
        fifo.append(self)
        if self.children is not None:
            while len(fifo) != 0:
                current = fifo.pop(0)
                visit(current)
                if not current.is_leaf():
                    for el in current.children:
                        fifo.append(el)
    def search(self, value: Any)->Union["TreeNode",None]:
        fifo = []
        fifo.append(self)
        if self.children is not None:
            while len(fifo) != 0:
                current = fifo.pop(0)
                if current.value==value:
                    return current
                if not current.is_leaf():
                    for el in current.children:
                        fifo.append(el)
    def node_to_nested_dict(self):
        klucz={self.value: {}}
        for child in self.children:
            child_dict=child.node_to_nested_dict()
            klucz[self.value].update(child_dict)
        return klucz

node0 = TreeNode("F")
assert node0.value == "F"
assert node0.children == []
assert str(node0) == "F"
assert node0.is_leaf() == True
node1 = TreeNode("B", [TreeNode("A"),TreeNode("D")])
node2 = TreeNode("G")
assert node2.children == []
assert node1.children[0].value == "A"
node0.add(node1)
node0.add(node2)
assert node0.children == [node1, node2]
assert node2.children == []
l_deep_rec = []
node0.for_each_deep_first_rec(l_deep_rec.append)
assert [x.value for x in l_deep_rec] == ["F", "B", "A", "D", "G"]
#l_deep = []
 #node0.for_each_deep_first(l_deep.append)
#assert [x.value for x in l_deep] == ["F", "B", "A", "D", "G"]
l_breadth = []
node0.for_each_breadth_first(l_breadth.append)
assert [x.value for x in l_breadth] == ["F", "B", "G", "A", "D"]
assert node0.search("G") == node2
assert node1.search("G") is None
assert(node0.node_to_nested_dict()) == {"F": {"B": {"A": {}, "D": {}}, "G": {}}}
