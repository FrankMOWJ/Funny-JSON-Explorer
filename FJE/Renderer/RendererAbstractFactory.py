from  .JSONRendererFactory import RectangleRendererFactory, TreeRendererFactory
from ..Icon.IconFamily import IconFamily
# 抽象工厂类
class RendererAbstractFactory:
    def create_RendererFactory(renderer_type: str, icons: IconFamily):
        if renderer_type == "tree":
            return TreeRendererFactory(icons=icons)
        elif renderer_type == "rectangle":
            return RectangleRendererFactory(icons=icons)
        else:
            raise ValueError(f"Invalid shape type: {renderer_type}")
        