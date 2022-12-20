from setuptools import setup, find_packages
from service.version import version_number

setup(
    name='codeswap',
    version=version_number(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cswap = main:main',
        ],
    },
)
