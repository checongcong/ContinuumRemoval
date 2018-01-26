# Visualizer class handles visualization-related operations.

import matplotlib.pyplot as plt


class Visualizer(object):
    @staticmethod
    def visualize(original_spectra, normalized_spectra, hull):
        """
        The main method to visualize the original spectra, the normalized spectra, and the continuum hull.
        
        :param original_spectra: the original spectra 
        :param normalized_spectra: the normalized spectra
        :param hull: the continuum hull.
        :return: None
        """
        plt.subplot(211)
        plt.plot(original_spectra.get_x(), original_spectra.get_y())
        plt.plot(hull.get_hull_x(), hull.get_hull_y(), '-+')
        plt.title('The original spectra and continuum hull')
        plt.subplot(212)
        plt.plot(normalized_spectra.get_x(), normalized_spectra.get_y())
        plt.title('The normalized spectra')
        plt.show()
