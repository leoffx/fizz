import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    author="Leonardo Ferreira",
    author_email="leonardoff.eng@gmail.com",
    name='fizz',
    license="MIT",
    description='fizzbuzz is a python package for acing fizzbuzz questions at coding interviews.',
    version='v4.2.0',
    url='https://github.com/leoffx/fizz',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    long_description_content_type='text/markdown',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)