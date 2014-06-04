from distutils.core import setup

setup(
    name='PYmuco',
    version='0.1dev0000',
    author='Hans-Nikolai Viessmann',
    author_email='hv15@hw.ac.uk',
    packages=['pymuco',],
    scripts=['pymuco.sh',],
    license='LICENSE',
    long_description=open('README.markdown').read(),
)