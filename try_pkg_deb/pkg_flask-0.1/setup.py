import os

from setuptools import setup, find_packages

setup(
	name='flasky',
	version='0.1.0',
	description='Little workouts with debian packaging',
	long_description='Do we need a long discription with the one complex problem',
	license='Cyber-Itus',
	author='Nithin Gollapalli',
	author_email='nithin.gollapalli@cyber-itus.com',
	packages=find_packages(),
	install_requires=["Flask"],
	include_package_data=True,
	entry_points = {
		'console_scripts' : [
			'run_server = flasky.scripts.run_server:run_server'
				]
	},
	classifiers=[
		"Private :: Do Not Upload"
		],
)
