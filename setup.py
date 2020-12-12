#
# Created by maks5507 (me@maksimeremeev.com)
#

from setuptools import setup, find_packages
import setuptools.command.build_py as build_py


setup_kwargs = dict(
    name='worker_compose',
    version='1.0',
    packages=['worker_compose'],
    install_requires=[
        'numpy',
        'multiprocessing',
        'rmq_interface'
    ],
    setup_requires=[
    ],

    cmdclass={'build_py': build_py.build_py},
)

setup(**setup_kwargs)
