"""
setup for code-katas
"""
from setuptools import setup

DEPENDENCIES = ['pytest', 'pytest-cov', 'ipython']
MODULES = ['shortest_word']
EXTRA_PACKAGES = {
    'test': ['tox']
}
CONSOLE_SCRIPTS = {
    'console_scripts': [
        'shortest_word = shortest_word:main'
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
