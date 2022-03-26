## COMMANDS

- **Normal Command Test**

  ```bash
  py.test
  pytest
  ```

- **Verbose Command Test (To understand the failed tests better)**

  ```bash
  pytest -v agg_test.py
  ```

- **To print log messages to console**

  ```bash
  pytest -sv
  ```

- **Run multiple tests**

  ```bash
  pytest -v
  ```

- **Test with substring**
  ```bash
  pytest -k <substring>
  pytest -k 'fun' -v test_demo_2.py
  ```

- **Test with multiple substring**
  ```bash
  pytest -k <substring or substring>
  pytest -k 'fun or sum' -v
  pytest -k 'fun and sum' -v
  pytest -k 'not fun' -v
  ```

- **Test with Markers**
  ```python
  import pytest
  
  @pytest.mark.demo
  def func():
      pass
  ```
  ```bash
  pytest -m 'fun' -v
  ```

  ---
  > **_NOTE:_**
  Both Markers and Substrings are used to run group selective tests.
  If we are willing to change the name of the tests then we can use `-k <substring>`.
  If not then we can use markers as `-m`.

  ---


- **Test with Fixtures**
  
  ```python
  import pytest

  @pytest.fixture
  def func():
      i =20
      return i
  ```
 
  ```bash
  pytest -k 'sum' -v test_demo_fixtures.py
  ```

  ---
  > **_NOTE:_**
  Fixture has scope only within a test file where it is defined.
  To make a fixture available to multiple test files, we have to define the fixture function in a file called [conftest.py](./fixture/conftest.py)
  Pytest will look for the fixture function in the test file and if not found it will look in the [conftest.py](./fixture/conftest.py) file.
  
  ---

- **Test with Parametrize**

  ```python
  import pytest

  @pytest.mark.parametrize("input, expected",[(1,2),(3,4)])
  def func(input,expected):
      assert input + 1 == expected
  ```
  
  ```bash
  pytest -k 'sum' -v test_demo_fixtures.py
  ```

- **Stopping file after n fails**
  ```bash
  pytest test_demo_2.py -v --maxfail 3
  ```