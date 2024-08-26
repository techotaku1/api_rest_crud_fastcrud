from setuptools import setup, find_packages

setup(
    name='mi-paquete',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fastcrud',
    ],
    long_description='Este paquete está basado en el paquete fastcrud. Ver más en https://github.com/igorbenav/fastcrud',
    # Otros campos de configuración
)