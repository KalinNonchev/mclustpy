import numpy as np
import rpy2.robjects as robjects
from rpy2.robjects import conversion, numpy2ri

# Define a list of strings that specifies the names of the output values returned by the Mclust function.
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

    # Use modern conversion context (no warnings)
    with conversion.localconverter(conversion.default_converter + numpy2ri.converter):
        res = rmclust(data, G, modelNames)

    # Convert to Python dictionary
    res = dict(zip(OUT_NAMES, res))
    return res
