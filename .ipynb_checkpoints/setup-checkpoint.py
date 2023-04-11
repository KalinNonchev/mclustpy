from setuptools import setup, find_packages

setup(name='mclustpy',
      version='0.0.1',
      description='Clustering using the mclust algorithm.',
      author='KalinNonchev',
      author_email='boo@foo.com',
      license='MIT License',
      long_description_content_type='text/markdown',
      long_description=open('README.md').read(),
      url="https://github.com/KalinNonchev/mclustpy",
      packages=find_packages(),  # find packages
      include_package_data=True,
      # external packages as dependencies,
      install_requires=['mclustpy'],
      python_requires='>=3.6'
      )