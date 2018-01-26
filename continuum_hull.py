# ContinuumHull class computes the ContinuumHull of a Spectra, and normalizes the ContinuumHull.
#
# Requires: There are at least 2 points in the input spectra.

from point import Point
from spectra import Spectra


class ContinuumHull(object):
    def normalize_spectra(self, spectra):
        """
        Given the input original spectra, computes the ContinuumHull and normalizes the spectra.
        
        :param spectra: The original spectra
        :return: The normalized spectra
        """
        self._compute_hull(spectra)
        normalized_spectra = Spectra()
        for p in self._points:
            normalized_spectra.add_point(self._normalize_point(p))
        return normalized_spectra

    def get_hull_x(self):
        """
        Gets the x-values of ContinuumHull points.
        
        :return: The x-values of ContinuumHull points. 
        """
        return [p.x for p in self._hull_points]

    def get_hull_y(self):
        """
        Gets the y-values of ContinuumHull Points.
         
        :return: The y-values of ContinuumHull points. 
        """
        return [p.y for p in self._hull_points]

    def _init_variables(self, spectra):
        """
        Inits the class variables.
        
        :param spectra: The original spectra 
        :return: None
        """
        if not spectra.is_sorted():
            spectra.sort()
        self._points = spectra.points()
        self._n = len(self._points)
        assert self._n >= 2
        self._hull_points = []

    def _compute_hull(self, spectra):
        """
        Given the original spectra, computes the ContinuumHull using a variant of Jarvis’s Algorithm.
        
        :param spectra: The original spectra
        :return: None
        """
        self._init_variables(spectra)
        # If there's less or equal to two points, this is the hull.
        if self._n <= 2:
            self._hull_points = self._points
            return

        # Find the rightmost point as P1, and the leftmost point as P2, and adds P2 to the Hull points.
        # NOTE: There is a trick that we add and only add P2 to the Hull points. P1 is the rightmost point, so in the
        # Hull it's supposed to be the last point being added. We designed the while-loop in such way, that ensures it
        # adds P1 as the last round.
        p1, p2 = self._n - 1, 0
        p = p2
        self._hull_points.append(self._points[p2])

        # Keep moving clockwise until reach the rightmost point again.
        while True:
            # Search for a point q such that orientation(p, i, q) is clockwise for all points 'i'. At start, we
            # arbitrarily assign q to any point that's *not* p.
            q = (p + 1) % self._n
            for i in range(self._n):
                if self.orientation(self._points[p], self._points[i], self._points[q]) == 1:
                    q = i
            # Updates p and adds to the Hull.
            p = q
            self._hull_points.append(self._points[p])
            if p == p1:
                break

    @staticmethod
    def orientation(p, q, r):
        """
        Find the orientation of points (p, q, r).
        
        :param p: the first point in Point format
        :param q: the second point in Point format
        :param r: the third point in Point format
        :return:
            0 to represent p, q and r are colinear
            1 to represent p, q and r are clockwise
            2 to represent p, q and r are counterclockwise
        """
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def _normalize_point(self, p):
        """
        Given a point from original spectra, converts it to a point in the normalized spectra.
        
        In this method, we start with the leftmost segment in the ContinuumHull, move all the way to the rightmost
        segment until we find the segment that contains the p in terms of x-axis range. Generally the number of segments
        in ContinuumHull is relatively small, so that we don't need more sophisticated algorithms like binary search or
        hashing.
        
        :param p: The point from original spectra.
        :return: The point in the normalized spectra.
        """
        segment_right_index = 1
        while p.x > self._hull_points[segment_right_index].x and segment_right_index < len(self._hull_points) - 1:
            segment_right_index += 1
        p1, p2 = self._hull_points[segment_right_index - 1], self._hull_points[segment_right_index]
        k = (p2.y - p1.y) / (p2.x - p1.x)
        b = p1.y - k * p1.x
        return Point(p.x, p.y / (k * p.x + b))
