"""
setup for code-katas
"""
from setuptools import setup

DEPENDENCIES = ['ipython']
MODULES = [
    'shortest_word',
    'tribonnaci_sequence',
    'case_reversal_of_consecutive_duplicates',
    'find_the_odd_int',
    'counting_duplicates',
    'the_hidden_word'
    ]
EXTRA_PACKAGES = {
    'test': ['tox', 'pytest', 'pytest-cov']
}
CONSOLE_SCRIPTS = {
    'console_scripts': [
    ]
}
setup(
    name="code-katas",
    description="""A module containing solutions to various
    code katas on codewars.""",
    version='0.1',
    author='Elyanil Castro',
    author_email='yanil3500@gmail.com',
    license='MIT',
    package_dir={'': 'src'},
    # insert the names of pymodule into array
    py_modules=MODULES,
    install_requires=DEPENDENCIES,
    extras_require=EXTRA_PACKAGES,
    # console scripts allow for custom commands
    entry_points=CONSOLE_SCRIPTS


)
