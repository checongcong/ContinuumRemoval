# The generator of spectras.

import random
import numpy as np
from point import Point
from spectra import Spectra


class SpectraGenerator(object):
    @staticmethod
    def uniform_random(n, x_left=0.0, x_right=1.0, y_bottom=0.0, y_top=1.0):
        """
        Generates a Spectra with n points, that's uniformly randomly distributed within the bounding box of
        ([x_left, y_bottom], [x_right, y_top]).
        
        :param n: Number of points to add to Spectra
        :param x_left: part of bounding box
        :param x_right: part of bounding box
        :param y_bottom: part of bounding box
        :param y_top: part of bounding box
        :return: A *sorted* Spectra with n data points.
        """
        assert x_left <= x_right and y_bottom <= y_top
        sp = Spectra()
        for i in range(n):
            p = Point(random.uniform(x_left, x_right), random.uniform(y_bottom, y_top))
            sp.add_point(p)
        sp.sort()
        return sp

    @staticmethod
    def bell_curve_with_random_walk(n, walk_range=0.2):
        """
        Generates a Spectra with n points, that's around y = -x^2 + 1, with a random walk factor on y-axis.
        
        :param n: The number of points to be added to Spectra
        :param walk_range: The random walk factor.
        :return: A *sorted* Spectra with n data points.
        """
        vec_x = np.linspace(-1.0, 1.0, n)
        sp = Spectra()
        for x in vec_x:
            y = -1.0 * x * x + 1.0 + random.uniform(-1.0 * abs(walk_range), abs(walk_range))
            sp.add_point(Point(x, y))
        return sp
