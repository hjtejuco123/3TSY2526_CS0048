# shapes/__init__.py

from .circle import calculate_area as circle_area
from .rectangle import calculate_area as rectangle_area

__all__ = ['circle_area', 'rectangle_area']