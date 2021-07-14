# Testing

- Tests can be added in scripts within this folder
- All test file names must begin with "test_"
- All test function names must start with "test_" and have client as a parameter, for example:
  ```
  def test_empty_db_default_root(client):
  ```
- All test files must have the following import
  ```
  from component_test.conftest import *
  ```
- The tests can be run by running test.sh from the root directory
  ```
  sh ./scripts/test.sh
  ```
