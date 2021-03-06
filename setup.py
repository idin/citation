from setuptools import setup, find_packages

def readme():
	with open('./README.md') as f:
		return f.read()

setup(
	name='citation',
	version='0.0.2',
	license='MIT',

	author='Idin',
	author_email='py@idin.ca',
	url='https://github.com/idin/citations',

	keywords='encryption decryption',
	description='Python library for managing package dependencies',
	long_description=readme(),
	long_description_content_type='text/markdown',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],

	packages=find_packages(exclude=("jupyter_tests", ".idea", ".git")),
	install_requires=['dill', 'base32hex', 'route'],
	python_requires='~=3.6',
	zip_safe=True
)