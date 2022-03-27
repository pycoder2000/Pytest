## COMMANDS

Pytest identifies files whose names start with <span style="color:green"><b><i>test_</i></b></span> or ending with <span style="color:green"><b><i>_test</i></b></span> as the test files.

Pytest identifies functions whose names are starting with <span style="color:green"><b><i>test</i></b></span> as test functions.

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
  pytest -k 'fun' -v test_demo_2.py
  ```

- **Test with multiple substring**
  ```bash
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
  > - Both Markers and Substrings are used to run group selective tests.
  > - If we are willing to change the name of the tests then we can use `-k <substring>`.
  > - If not then we can use markers as `-m`.

  ---

- **Test with Fixtures**
  
  ```python
  import pytest

  @pytest.fixture(scope="function")
  def func():
      i =20
      return i
  ```
 
  ```bash
  pytest -k 'sum' -v test_demo_fixtures.py
  ```
  
  ---
  #### **Fixture Scope**
  - `function`: the default scope, the fixture is destroyed at the end of the test.
  - `class`: the fixture is destroyed during teardown of the last test in the class.
  - `module`: the fixture is destroyed during teardown of the last test in the module.
  - `package`: the fixture is destroyed during teardown of the last test in the package.
  - `session`: the fixture is destroyed at the end of the test session.

  Also we can `autouse = True` if we want to run the fixture before every test.
  
  ---

  ---
  > **_NOTE:_**
  > - Fixture has scope only within a test file where it is defined.
  > - To make a fixture available to multiple test files, we have to define the fixture function in a file called [conftest.py](./fixture/conftest.py)
  > - Pytest will look for the fixture function in the test file and if not found it will look in the [conftest.py](./fixture/conftest.py) file.
  
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

- **Skip Tests**

  ```python
  import pytest

  @pytest.mark.skip("This is a reason for skipping the test")
  def func():
      pass
  ```

  We can also provide conditions to skip the test.
  ```python
  @pytest.mark.skipif(condition,reason = "This is a reason for skipping the test")
  ```
  
  ```bash
  pytest -sv
  ```

- **xfail Tests**

  ```python
  import pytest

  @pytest.mark.xfail
  def func():
      pass
  ```
  
  ```bash
  pytest -sv
  ```

  ---
  > **_NOTE:_**
  > - There are used in cases where the test cases are not relevant for a specific period of time.
  > - The xfail tests will be executed, but will not counted as failed or passed tests.

  ---

- **Stopping file after n fails**
  
  If N number of test fails then pytest stops the execution
  ```bash
  pytest test_demo_2.py -v --maxfail 3
  ```

- **Running pytest in parallel**
  ```bash
  pip install pytest-xdist
  ```
  
  To run the tests in parallel
  ```bash
  pytest -n 2
  ```

  Here -n specifices the number of workers to run the tests.

  To view the logs add `sys.stdout = sys.stderr` at the top of the file.

- **Save pytest results**
  To get results in XML format, we have to use
  ```bash
  pytest --junitxml="results.xml"
  ```
  To get results in HTML format, we have to use
  ```bash
  pip install pytest-html
  pytest --html="results.html"
  ```
