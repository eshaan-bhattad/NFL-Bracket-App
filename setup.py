from distutils.core import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n') if (line and not
                                                     line.startswith('--'))
    ]

setup(
    name='NFLPlayoffBracketChallenge',
    version=__import__('NFLPlayoffBracketChallenge').__version__,
    author='Eshaan Bhattad',
    author_email='eshaan2@illinois.edu',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/eshaan-bhattad/nflplayoffbracketapp',
    license='BSD',
    description='NFL Bracket App',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=install_requires,
)
