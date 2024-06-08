from abc import ABC, abstractmethod

# Abstract product class
class JSONRenderer(ABC):
    def __init__(self, icons) -> None:
        super().__init__()
        self.icons = icons
    @abstractmethod
    def render(self, node, level=0):
        pass
    @abstractmethod
    def get_indent(self):
        pass

# concrete product class1
class TreeRenderer(JSONRenderer):
    def render(self, node, level=0, is_last=True, has_siblings: list[bool]=[]):
        # 跳过根节点，不打印
        if level != 0:
            # 确定适当的分支字符
            branch_char = '└─' if is_last else '├─'
            # 打印当前节点，使用合适的图标和缩进
            print(self.get_indent(level, is_last, has_siblings) + branch_char + (self.icons.get_leaf_icon() if not node.get_children() else self.icons.get_node_icon()) + str(node))
        
        # 获取当前节点的子节点
        children = node.get_children()
        for i, child in enumerate(children):
            # 递归渲染每个子节点，标记是否是最后一个子节点
            self.render(child, level + 1, i == len(children) - 1, has_siblings + [True if i != len(children) -1  else False])
    
    def get_indent(self, level, is_last, has_siblings: list[bool]):
        indent = ''
        for i in range(level-1):
            # 上一级之后有同级子节点，则使用分支字符
            if has_siblings[i]:
                indent += '│  '
            else:
                indent += '   '
        return indent

# concrete product class2
class RectangleRenderer(JSONRenderer):
    def render(self, node, level=0, is_first = False, is_last=True):
        if level != 0:
            if is_first:
                print(self.get_top_border(level, node, is_last))
            elif is_last and node.is_leaf:
                print(self.get_bottom_border(level, node, is_last))
            else:
                print(self.get_middle_node(level, node, is_last))

        children = node.get_children()
        for i, child in enumerate(children):
            self.render(child, level + 1, is_first=(level==0 and i == 0), is_last=(is_last and i == len(children) - 1))

    def get_top_border(self, level, node, is_last):
        border = "┌─ " 
        border += (self.icons.get_leaf_icon() if not node.get_children() else self.icons.get_node_icon()) + node.name + " " 
        border += "─" * (38 - len(border)) + "─┐"
        return border

    def get_bottom_border(self, level, node, is_last):
        border = '└'
        border += '──' * (level - 1)
        border += '└─ ' + (self.icons.get_leaf_icon() if not node.get_children() else self.icons.get_node_icon()) + node.name
        border +=  "─" * (38 - len(border)) + "─┘" 
        return border

    def get_middle_node(self, level, node, is_last):
        border = self.get_indent(level) + (self.icons.get_leaf_icon() if not node.get_children() else self.icons.get_node_icon())
        border += str(node) + " " 
        border += "─" * (38 - len(border) ) + '─┤'      
        return border
    
    def get_indent(self, level):
        indent = ''
        indent += '│  ' * (level - 1)
        indent += '├─ '
        return indent
    

