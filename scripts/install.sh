sudo apt install python3
sudo apt install pip
if [[ "$VIRTUAL_ENV" == "" ]]
then
pip install virtualenv
fi