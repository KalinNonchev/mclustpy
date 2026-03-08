from setuptools import setup, find_packages

setup(name='mclustpy',
      version='0.0.3',
      description='Python wrapper for R Mclust algorithm: Gaussian model-based clustering with automatic model selection',
      author='Kalin Nonchev',
      license='MIT License',
      long_description_content_type='text/markdown',
      long_description=open('README.md').read(),
      url="https://github.com/KalinNonchev/mclustpy",
      packages=find_packages(),
      include_package_data=True,
      install_requires=['numpy', 'rpy2'],
      python_requires='>=3.8',
      keywords=[
          'clustering', 'mclust', 'gaussian-mixture-models',
          'model-based-clustering', 'rpy2', 'unsupervised-learning',
          'bayesian-information-criterion', 'statistics',
      ],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],
      )
