import versioneer
from setuptools import setup


with open('README.rst', 'r') as fh:
    long_description = fh.read()


github_url = 'https://github.com/chrisbrake/perceptible'


setup(
    name='perceptible',
    packages=['perceptible'],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Observable versions of python data structures',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Chris Brake',
    author_email='chris.brake@gmail.com',
    url=github_url,
    download_url='%s/archive/0.1.tar.gz' % github_url,
    keywords=['perceptible', 'observable', 'observer'],
    classifiers=[],
)
