from setuptools import setup

setup(
   name='csv-detective',
   packages = ['csv-detective']
   version='0.1.0',
   author='Greyson R. LaLonde',
   author_email='greyson.r.lalonde@gmail.com',
   description='Search a folder of csv files for value(s)',
   url = 'https://github.com/greysonlalonde/csv-detective',
    download_url = 'https://github.com/greysonlalonde/csv-detective/archive/0.0.1.tar.gz',
   keywords = ['tag1', 'tag2'],
   install_requires=[
    "pandas >= 1.2.1",
   ],
   classifiers = []
)
