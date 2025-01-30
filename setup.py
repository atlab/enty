from setuptools import setup, find_packages

version = {}
with open("enty/version.py") as fp:
    exec(fp.read(), version)

with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name='enty',
    version=version['__version__'],
    packages=find_packages(),
    install_requires=install_requires,
    author='Stelios Papadopoulos, Frank DeGuire',
    author_email='stelios@spapa.us',
    description='A lightweight ORM with a simple interface.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/atlab/enty',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
