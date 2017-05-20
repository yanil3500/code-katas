"""
setup for code-katas
"""
from setuptools import setup

DEPENDENCIES = ['pytest', 'pytest-cov', 'ipython']
MODULES = [
    'shortest_word',
    'tribonnaci_sequence',
    'case_reversal_of_consecutive_duplicates',
    'find_the_odd_int',
    'counting_duplicates'
    ]
EXTRA_PACKAGES = {
    'test': ['tox']
}
CONSOLE_SCRIPTS = {
    'console_scripts': [
        'shortest_word = shortest_word:main',
        'tribonnaci_sequence = tribonnaci_sequence:main',
        'case_reversal_of_consecutive_duplicates = case_reversal_of_consecutive_duplicates:main',
        'find_the_odd_int = find_the_odd_int:main',
        'counting_duplicates = counting_duplicates:main'

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
