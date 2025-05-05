[![Downloads](https://static.pepy.tech/badge/mclustpy)](https://pepy.tech/project/mclustpy) ![Python package](https://github.com/KalinNonchev/mclustpy/actions/workflows/python-package.yml/badge.svg) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/KalinNonchev/mclustpy/issues)

# mclustpy

mclustpy is a Python function for clustering data using the Mclust algorithm from the R package [mclust](https://www.rdocumentation.org/packages/mclust/versions/5.4.6/topics/Mclust). The function takes a 2D numpy array of data and returns a dictionary containing various output values computed by the Mclust algorithm.

## Installation

mclustpy requires the following dependencies:

- numpy
- rpy2

To install mclustpy, you can use pip:

```
pip install mclustpy
```

## Usage

```python
from mclustpy import mclustpy
import numpy as np

data = np.random.rand(1000, 10)
data.shape

res = mclustpy(data, G=9, modelNames='EEE', random_seed=2020)
```

### The mclustpy function takes the following parameters:

- data: a 2D numpy array of data to be clustered.
- G: an integer specifying the maximum number of mixture components to be considered (default is 9).
- modelNames: a string specifying the model types to be considered (default is 'EEE').
- random_seed: an integer specifying the random seed for reproducibility (default is 2020).


### The function returns a dictionary containing the following output values:

- call: the function call used to run the Mclust algorithm.
- data: the input data as an R matrix.
- modelName: the model name(s) selected by the algorithm.
- n: the number of observations in the data.
- d: the number of variables in the data.
- G: the number of mixture components selected by the algorithm.
- BIC: the Bayesian Information Criterion (BIC) value for the selected model.
- loglik: the log-likelihood of the selected model.
- df: the number of degrees of freedom in the selected model.
- bic: the BIC value for each model considered.
- icl: the Integrated Completed Likelihood (ICL) value for each model considered.
- hypvol: the hypervolume of the cluster tree for each model considered.
- parameters: the estimated parameters for each component in the selected model.
- z: the posterior probabilities of assignment to each component for each observation.
- classification: the classification of each observation under the selected model.
- uncertainty: a measure of uncertainty in the classification of each observation.


For more info take a look at the original [mclust page](https://www.rdocumentation.org/packages/mclust/versions/5.4.6/topics/Mclust)


#### License Notice:
This package, mclustpy, is licensed under the MIT License. However, it depends on the R package mclust, which is licensed under the GNU General Public License (GPL ≥2). Users must ensure compliance with the GPL license when using mclustpy.
