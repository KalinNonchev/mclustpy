import numpy as np
import rpy2.robjects as robjects
import rpy2.robjects.numpy2ri
import rpy2

# Define a list of strings that specifies the names of the output values returned by the mclust function.
OUT_NAMES = ["call", "data", "modelName", "n", "d", "G", "BIC", "loglik", "df", "bic", "icl", "hypvol", "parameters", "z", "classification", "uncertainty"]


def mclustpy(data, G=9, modelNames='EEE', random_seed=2020):
    """\
    Clustering using the mclust algorithm.
    The parameters are the same as those in the R package mclust.
    
    Parameters
    ----------
    data : numpy.ndarray
        A 2D array of the data to be clustered.
    G : int, optional
        An integer specifying the maximum number of mixture components to be considered. Default is 9.
    modelNames : str, optional
        A string specifying the model types to be considered. Default is 'EEE'.
    random_seed : int, optional
        An integer specifying the random seed for reproducibility. Default is 2020.

    Returns
    -------
    dict
        A dictionary containing the output values returned by the mclust function, with keys specified by OUT_NAMES.
    """
    
    # Set the random seed.
    np.random.seed(random_seed)
    # Load the mclust library in R.
    robjects.r.library("mclust")

    # Activate numpy2ri to convert data between NumPy arrays and R objects.
    rpy2.robjects.numpy2ri.activate()
    # Set the random seed in R.
    r_random_seed = robjects.r['set.seed']
    r_random_seed(random_seed)
    # Get the Mclust function from R.
    rmclust = robjects.r['Mclust']
    
    # Run the Mclust function with the given parameters and convert the output to a dictionary.
    res = rmclust(rpy2.robjects.numpy2ri.numpy2rpy(data), G, modelNames)
    
    res = dict(zip(OUT_NAMES, res))
    
    return res