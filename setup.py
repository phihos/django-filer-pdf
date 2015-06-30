from setuptools import setup, find_packages
import os

version = __import__('filer_pdf').__version__

def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-filer-pdf",
    version = version,
    url = 'https://github.com/phihos/django-filer-pdf',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "A django-filer plugin for PDF file support.",
    long_description = read('README.rst'),
    author = 'Philipp Hossner',
    author_email = 'philipp.hossner@posteo.de',
    packages=find_packages(),
    install_requires = (
        'django-filer>0.9a2',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
