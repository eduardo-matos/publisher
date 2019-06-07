from setuptools import setup, find_packages

setup(
    name='publisher',
    version='1.0',
    author='Eduardo Matos',
    description='Publishes messages in RabbitMQ',
    packages=find_packages(),    
    install_requires=['pika==1.0.1'],
)
