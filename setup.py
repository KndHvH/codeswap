from setuptools import setup, find_packages
from src.helper.app import AppHelper

app = AppHelper()


setup(
    name='codeswap',
    version=app.version,
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
            'cs = main:main',
            'cswap = main:main',
        ],
    },
)
