from setuptools import setup, find_packages

version = __import__('everybit').get_version()

kwargs = {
    'name': 'everybit-python',
    'version': version,
    'packages': find_packages(),
    'author': 'Tony Mugavero',
    'author_email': 'tony@everybit.co',
    'description': 'Everybit Python API Wrapper',
    'license': 'See License File',
    'keywords': 'Video API Library Everybit',
    'url': 'https://github.com/everybit/everybit-python.git',

    'test_suite': 'example',

    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
}

setup(**kwargs)