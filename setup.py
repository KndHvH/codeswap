from setuptools import setup

setup(
    name='codeswap',
    version='0.2.0',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cswap = main:main',
        ],
    },
)