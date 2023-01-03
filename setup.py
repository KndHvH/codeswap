from setuptools import setup, find_packages
from src.service.version import version_number


setup(
    name='codeswap',
    version=version_number(),
    license='MIT',
    author='Matias Herklotz',
    author_email='matherklotzz@gmail.com',
    packages=find_packages(),
    py_modules=['os', 'subprocess', 'platform','json','random','shutil','itertools'],
    url='https://www.github.com/kndhvh/codeswap',
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
        'setuptools',

    ],
    entry_points={
        'console_scripts': [
            'cswap = src.main:main',
        ],
    },
)
