# The main file to run/test Continuum Removal.

from spectra_generator import SpectraGenerator
from visualizer import Visualizer
from continuum_hull import ContinuumHull

if __name__ == "__main__":
    # Generates or loads original spectra.
    generator = SpectraGenerator()
    spectra = generator.bell_curve_with_random_walk(40)

    # Computes ContinuumHull and normalizes the original spectra.
    hull = ContinuumHull()
    normalized_spectra = hull.normalize_spectra(spectra)

    # Visualizes the original spectra, the ContinuumHull and the normalized spectra.
    visualizer = Visualizer()
    visualizer.visualize(spectra, normalized_spectra, hull)