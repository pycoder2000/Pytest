"""
! COMMANDS
* Normal Command Test
$ pytest -v agg_test.py

* Run multiple tests
$ pytest -v

* Test with substring
$ pytest -k 'fun' -v test_demo_2.py

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