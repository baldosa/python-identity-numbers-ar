from setuptools import find_packages, setup
setup(
    name='identitynumbersar',
    packages=find_packages(include=['identitynumbersar']),
    version='0.1.0',
    description='Limpiar, formatea y valida CUIL/T y DNI',
    author='Ema',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
