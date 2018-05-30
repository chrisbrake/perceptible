import versioneer
from setuptools import setup


with open('README.rst', 'r') as fh:
    long_description = fh.read()


setup(
    name='perceptible',
    packages=['perceptible'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Observable versions of python data structures',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Chris Brake',
    author_email='chris.brake@gmail.com',
    url='https://github.com/chrisbrake/perceptible',
    keywords=['perceptible', 'observable', 'observer'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries'
    ],
)
