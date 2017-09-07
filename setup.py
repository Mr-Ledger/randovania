from setuptools import setup

setup(
    name='prime-checker',
    version='0.0.1',
    author='Henrique Gemignani',
    url='https://github.com/henriquegemignani/prime-checker',
    description='A randomizer validator for the Metroid Prime series.',
    packages=[
        'primechecker',
    ],
    scripts=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Games/Entertainment',
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
        ]
    },
)