from setuptools import setup

setup(
    name='shitback',
    version='0.1',
    py_modules=['main'],
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
                'shitback = main:main',
            ],
    },
)
