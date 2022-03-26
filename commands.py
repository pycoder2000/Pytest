"""
! COMMANDS
* Normal Command Test
$ py.test
$ pytest

* Verbose Command Test (To understand the failed tests better)
$ pytest -v agg_test.py

* To print log messages to console
$ pytest -sv

* Run multiple tests
$ pytest -v

* Test with substring
$ pytest -k <substring>
$ pytest -k 'fun' -v test_demo_2.py

* Test with multiple substring
$ pytest -k <substring or substring>
$ pytest -k 'fun or sum' -v
$ pytest -k 'fun and sum' -v
$ pytest -k 'not fun' -v

* Test with Markers
^ import pytest
^ @pytest.mark.demo
$ pytest -m 'fun' -v

~ NOTE: Both Markers and Substrings are used to run group selective tests
~       If we are willing to change the name of the tests then we can use -k <substring>
~       If not then we can use markers as -m


* Test with Fixtures
^ import pytest
^ @pytest.fixture
~ Add function and return value
$ pytest -k 'sum' -v test_demo_fixtures.py

~ NOTE : Fixture has scope only within a test file where it is defined.
~        To make a fixture available to multiple test files, we have to define the fixture function
~        in a file called conftest.py
~        Pytest will look for the fixture function in the test file and if not found it will look in the ~        conftest.py file.


* Test with Parametrize
^ import pytest
^ @pytest.mark.parametrize("input, expected",[(1,2),(3,4)])
$ pytest -k 'sum' -v test_demo_fixtures.py

* Stopping file after n fails
$ pytest test_demo_2.py -v --maxfail 3
"""