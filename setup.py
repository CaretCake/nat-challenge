from setuptools import setup, find_packages

setup(
    name='coins',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-cors',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)