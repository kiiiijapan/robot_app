try:
	from setuptools import setup, find_packages
except ImportError:
	from distutils.core import setup


setup(
	name = 'ROBOT_APP',
	version = '0.0.1',
	packages = ['roboter', 'roboter.models', 'roboter.controller', 'roboter.views'],
	packages_data = {'roboter':['templates/*.txt']},
	author = 'kaai',
	long_description=open('README.txt').read()
)