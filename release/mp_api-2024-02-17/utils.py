import math
import random
from typing import Any, Callable, Tuple

import sympy

from .draw import Color


class Enum:
    @staticmethod
    def get_color_block(index: int) -> str:
        """Enum color block
        :param index:
        :return:
        """
        color_blocks = [
                "black_concrete",
                "blue_concrete",
                "brown_concrete",
                "cyan_concrete",
                "gray_concrete",
                "green_concrete",
                "light_blue_concrete",
                "light_gray_concrete",
                "lime_concrete",
                "magenta_concrete",
                "orange_concrete",
                "pink_concrete",
                "purple_concrete",
                "red_concrete",
                "white_concrete",
                "yellow_concrete",

        ]
        return color_blocks[index % len(color_blocks)]

    @staticmethod
    def get_color_falling_block(index: int) -> str:
        """Enum color falling block
        :param index:
        :return:
        """
        color_blocks = [
                "black_concrete_powder",
                "blue_concrete_powder",
                "brown_concrete_powder",
                "cyan_concrete_powder",
                "gray_concrete_powder",
                "green_concrete_powder",
                "light_blue_concrete_powder",
                "light_gray_concrete_powder",
                "lime_concrete_powder",
                "magenta_concrete_powder",
                "orange_concrete_powder",
                "pink_concrete_powder",
                "purple_concrete_powder",
                "red_concrete_powder",
                "white_concrete_powder",
                "yellow_concrete_powder",
        ]
        return color_blocks[index % len(color_blocks)]

    @staticmethod
    def get_color(index: int) -> Color:
        """Enum color by concrete
        :param index:
        :return: #FFFFFF
        """
        colors = [
                Color('#FFA500'),
                Color('#FFFF00'),
                Color('#5DADE2'),
                Color('#2ECC71'),
                Color('#D7DBDD'),
                Color('#BB8FCE'),

                Color('#BA4A00'),
                Color('#B9770E'),
                Color('#2E86C1'),
                Color('#239B56'),
                Color('#909497'),
                Color('#76448A'),
                Color('#00FF00'),
                Color('#FFC0CB'),
                Color('#800080'),
                Color('#FFFFFF'),

        ]
        return colors[index % len(colors)]


def func2math_exp(func: Callable | str,
                  var: str = 't'
                  ) -> str:
    """Convert a Python function to a mathematical expression.

    Args:
        func: Python function
        var: Variable name

    Returns:
        str: Mathematical expression
    """
    if isinstance(func, int) or isinstance(func, float):
        return str(func)
    elif isinstance(func, str):
        return func
    else:
        t = sympy.symbols(var)
        return func(t)


def delta(*args) -> Tuple[str,]:
    """Convert a list of minecraft pos to a list of delta pos. such as ~1 ~1 ~1
    """
    place = 6
    str_list = []
    for x in args:
        str_list.append(f'~{x:.5f}')

    return tuple(str_list)


def mp_clamp(value: Any, min_value: Any, max_value: Any) -> str:
    """mp_clamp
    :param value:
    :param min_value:
    :param max_value:
    :return:
    """
    return f'clamp({value},{min_value},{max_value})'


def mp_min(a, b) -> str:
    """mp_min
    :param a:
    :param b:
    :return:
    """
    return f'min({a},{b})'


def mp_max(a, b) -> str:
    """mp_max
    :param a:
    :param b:
    :return:
    """
    return f'max({a},{b})'


def mp_if(condition: str, if_true: Any, if_false: Any) -> str:
    """mp_if
    :param condition:
    :param if_true:
    :param if_false:
    :return:
    """
    return f'if({condition},{if_true},{if_false})'


def mp_deg(x: Any) -> str:
    """mp_degrees
    :param x:
    :return:
    """
    return f'deg({x})'


def mp_radian(x: Any) -> str:
    """mp_radian
    :param x:
    :return:
    """
    return f'rad({x})'


def mp_and(a, b) -> str:
    """mp_and
    :param a:
    :param b:
    :return:
    """
    return f'and({a},{b})'


def mp_or(a, b) -> str:
    """mp_or
    :param a:
    :param b:
    :return:
    """
    return f'or({a},{b})'


def mp_rgb(r: Any, g: Any, b: Any) -> str:
    """mp_rgb
    :param r:
    :param g:
    :param b:
    :return:
    """
    return f'rgb({func2math_exp(r)},{func2math_exp(g)},{func2math_exp(b)})'


def mp_sin(x: Any) -> str:
    """mp_sin
    :param x:
    :return:
    """
    return f'sin({x})'


def mp_cos(x: Any) -> str:
    """mp_cos
    :param x:
    :return:
    """
    return f'cos({x})'


mp_t = 't'
