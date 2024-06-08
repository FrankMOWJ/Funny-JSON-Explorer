from .jsonNode import JSONNode

class JSONTreeBuilder:
    # 建造者模式
    def build_tree(self, json_obj):
        root = JSONNode("root")
        self.parse_object(json_obj, root)
        return root

    def parse_object(self, json_obj, parent):
        for key, value in json_obj.items():
            node = JSONNode(key, None if isinstance(value, dict) else value)
            if not isinstance(value, dict):
                node.is_leaf = True
            parent.add_child(node)
            if isinstance(value, dict):
                self.parse_object(value, node)
