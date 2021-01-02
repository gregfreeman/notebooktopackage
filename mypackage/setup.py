from setuptools import setup

setup(name='mypackage',
      version='1.0',
      description='Utility to demonstrate packages',
      author='Greg Freeman',
      author_email='greg@freemanscience.com',
      packages=['mypackage'],
      requirements=['numpy',
                    'matplotlib'],
      )
