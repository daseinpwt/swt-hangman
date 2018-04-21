from .base import BasePainter
from .hardgamepainter import HardGamePainter

class PainterFactory:
    def get_painter(self, max_fails, mask = " - "):
        if max_fails == 8:
            return BasePainter(mask)
        elif max_fails == 4:
            return HardGamePainter(mask)