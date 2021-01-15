from setuptools import setup
setup(
    name = 'pythoncli',
    version = '0.1.0',
    packages = ['pythoncli'],
    entry_points = {
        'console_scripts': [
            'pythoncli = pythoncli.__main__:main'
        ]
    })
