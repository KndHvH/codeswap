from setuptools import setup, find_packages
from service.version import version_number

setup(
    name='codeswap',
    version=version_number(),
    license='MIT',
    author='Matias Herklotz',
    author_email='matherklotzz@gmail.com',
    packages=find_packages(),
    url='https://www.github.com/kndhvh/codeswap',
    include_package_data=True,
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'cswap = main:main',
        ],
    },
)
