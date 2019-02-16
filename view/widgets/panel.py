from PIL import ImageDraw

from view.widgets.widget_base import WidgetBase


class PanelWidget(WidgetBase):
    def __init__(self, height: int, width: int):
        super().__init__(height, width)

    def draw(self, draw: ImageDraw):
        super().draw(draw)
        for child in self._children:
            if not child._yellow:
                child.draw(draw)

    def draw_yellow(self, draw: ImageDraw):
        super().draw(draw)
        for child in self._children:
            if child._yellow:
                child.draw(draw)
