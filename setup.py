

from distutils.core import setup


setup(
    name='snaptime',
    packages=['snaptime'],  # this must be the same as the name above
    version='0.1',
    description='Transform and truncate timestamps with a short syntax',
    install_requires=['python-dateutil'],
    author='Philipp Hitzler',
    author_email='phj.hitzler@gmail.com',
    url='https://github.com/zartstrom/snaptime',  # use the URL to the github repo
    download_url='https://github.com/zartstrom/snaptime/tarball/0.1',
    keywords=['snap', 'datetime', 'date', 'truncate', 'transform'],  # arbitrary keywords
    classifiers=[],
)