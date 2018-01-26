# Spectra represents a spectra measurement that is composed of N 2-dimensional points.

from point import Point


class Spectra(object):
    def __init__(self):
        self._points = []
        self._is_sorted = True

    def __str__(self):
        return "".join(["(%s,%s)" % (p.x, p.y) for p in self._points])

    def add_point(self, p):
        """
        Adds p to the sequence of points in the spectra, p needs to be type Point.
        
        :param p: The point to be added. 
        :return: None
        """
        assert type(p) is Point
        self._points.append(p)
        self._is_sorted = False

    def points(self):
        """
        :return: The sequence of points in the spectra. 
        """
        return self._points

    def get_x(self):
        """
        Gets the x-values of spectra points.

        :return: The x-values of spectra points. 
        """
        return [p.x for p in self._points]

    def get_y(self):
        """
        Gets the y-values of spectra points.

        :return: The y-values of spectra points. 
        """
        return [p.y for p in self._points]

    def is_sorted(self):
        """
        :return: whether the points in the spectra are sorted or not. 
        """
        return self._is_sorted

    def sort(self):
        """
        Sorts the points in the spectra.
        
        :return: None 
        """
        self._points.sort()
        self._is_sorted = True
