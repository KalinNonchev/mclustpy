import numpy as np
import rpy2.robjects as robjects

# Try importing the correct converter depending on rpy2 version
try:
    # Modern rpy2 (>=3.5)
    from rpy2.robjects.conversion import localconverter
    DEFAULT_CONVERTER = robjects.default_converter
except ImportError:
    # Older rpy2 (<3.5)
    from rpy2.robjects import conversion
    localconverter = conversion.localconverter
    DEFAULT_CONVERTER = conversion.default_converter

# NumPy converter
from rpy2.robjects import numpy2ri

# Define the names of the output elements returned by Mclust
OUT_NAMES = [
    "call", "data", "modelName", "n", "d", "G", "BIC", "loglik", "df",
    "bic", "icl", "hypvol", "parameters", "z", "classification", "uncertainty"
]


def mclustpy(data, G=9, modelNames='EEE', random_seed=2020):
    """
    Clustering using the mclust algorithm (R package 'mclust').

    Parameters
    ----------
    data : numpy.ndarray
        2D array of data to be clustered.
    G : int, optional
        Maximum number of mixture components (default=9).
    modelNames : str, optional
        Model type (default='EEE').
    random_seed : int, optional
        Random seed for reproducibility (default=2020).

    Returns
    -------
    dict
        Dictionary of results with keys specified by OUT_NAMES.
    """
    # Set seeds
    np.random.seed(random_seed)
    robjects.r['set.seed'](random_seed)

    # Load R library
    robjects.r.library("mclust")
    rmclust = robjects.r['Mclust']

    # Convert NumPy array to R matrix and run Mclust
    with localconverter(DEFAULT_CONVERTER + numpy2ri.converter):
        res = rmclust(data, G, modelNames)

    # Convert to Python dictionary
    res = dict(zip(OUT_NAMES, res))
    return res
