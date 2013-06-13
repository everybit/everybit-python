everybit-python
===============

Everybit API Python Wrapper

Various Ways of Installing
--------------------------

1. Using easy_install
 * easy_install everybit-python

2. Grab from git and run setup
 * git clone https://github.com/everybit/everybit-python.git
 * cd everybit-python
 * python setup.py install

3. Grab from git and throw it in your project
 * git clone https://github.com/everybit/everybit-python.git

Examples
--------

    from everybit.api import *


    Everybit = EverybitAPI()
    print Everybit.get_account_info()


For further examples, see example.py.