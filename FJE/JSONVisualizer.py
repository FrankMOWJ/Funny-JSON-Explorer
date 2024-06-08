class JSONVisualizer:
    def __init__(self, renderer):
        self.renderer = renderer

    def visualize(self, root):
        self.renderer.render(root, 0)
