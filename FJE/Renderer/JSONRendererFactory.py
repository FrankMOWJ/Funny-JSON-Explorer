from __future__ import annotations
from abc import ABC, abstractmethod

from .JSONRenderer import *

# 工厂模式
class JSONRendererFactory(ABC):
    def __init__(self, icons):
        pass
    @abstractmethod
    def createRenderer(self) -> JSONRenderer:
        raise NotImplementedError


class RectangleRendererFactory(JSONRendererFactory):
    def __init__(self, icons):
        self.icons = icons
    def createRenderer(self) -> RectangleRenderer:
        return RectangleRenderer(self.icons)
    
class TreeRendererFactory(JSONRendererFactory):
    def __init__(self, icons):
        self.icons = icons
    def createRenderer(self) -> TreeRenderer:
        return TreeRenderer(self.icons)