# Install Dependencies
- All applications needed can be installed with the install.sh script
  ```
  sh ./scripts/install.sh
  ```

# Initial Setup
- Create a virtual environment with virtualenv
  ```
  virtualenv env
  ```
- Activate virtual environment, **this must be done every time the project is opened**
  ```
  source ./env/bin/activate
  ```
- Install the requirments
  ```
  pip install -r requirements.txt
  ```
- Run the setup script to generate the python models for json schemas and sqlalchemy
  ```
  sh ./scripts/setup.sh
  ```

# Installing New Requirments

- Whenever new requirments are installed using pip run
  ```
  pip freeze > requirements.txt
  ```
# Running Application Localy
- Ensure the virtual environment is running if not already
  ```
  source ./env/bin/activate
  ```
- Run the local_run.sh script
  ```
  sh ./scripts/local_run.sh
  ```
# Testing
- Ensure the virtual environment is running if not already
  ```
  source ./env/bin/activate
  ```
- To run the component tests use the test.sh script
  ```
  sh ./scripts/test.sh
  ```
