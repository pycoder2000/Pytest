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

* Test with Markers
^ import pytest
^ @pytest.mark.demo
$ pytest -m 'fun' -v

* Test with Fixtures
^ import pytest
^ @pytest.fixture
~ Add function and return value
$ pytest -k 'sum' -v test_demo_fixtures.py

* Test with Parametrize
^ import pytest
^ @pytest.mark.parametrize("input, expected",[(1,2),(3,4)])
$ pytest -k 'sum' -v test_demo_fixtures.py

* Stopping file after n fails
$ pytest test_demo_2.py -v --maxfail 3
"""