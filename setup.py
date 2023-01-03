from setuptools import setup, find_packages
from src.service.version import version_number


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
        'click',
        'requests',
        'setuptools',

    ],
    entry_points={
        'console_scripts': [
            'cs = src.main:main',
            'cswap = src.main:main',
        ],
    },
)
