from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='perceptible',
    packages=['perceptible'],
    version='0.1',
    description='Observable versions of python data structures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Chris Brake',
    author_email='chris.brake@gmail.com',
    url='https://github.com/chrisbrake/perceptible',
    download_url='https://github.com/chrisbrake/perceptible/archive/0.1.tar.gz',
    keywords=['perceptible', 'observable', 'observer'],
    classifiers=[],
)
