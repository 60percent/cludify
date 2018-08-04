from setuptools import setup

setup(
    name='example-terraform-plugin',
    version='0.1.0',
    author='Example',
    packages=['example_package'],
    install_requires=['cloudify-plugins-common==4.2'],
)
