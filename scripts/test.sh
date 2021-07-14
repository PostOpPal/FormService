# Application environment variables
export JWT_SECRET=secret


#Flask environment variables
export DEPLOY=test
export FLASK_ENV=development
rm -f test.sqlite
python -m pytest -s
#Remove the test database
rm test.sqlite