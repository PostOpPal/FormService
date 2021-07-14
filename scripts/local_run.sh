#Application variables 
export JWT_SECRET=secret

#These variables are just for configuring flask
export DEPLOY=local
export FLASK_ENV=development
export FLASK_APP=app.py
flask run
#Remove the test database
rm test.sqlite