class JSONNode:
    # 组合模式
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.is_leaf = False
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def get_children(self):
        return self.children

    def __str__(self):
        return self.name + (": " + self.value if self.value else "")
