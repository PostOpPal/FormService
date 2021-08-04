sudo apt install python3
sudo apt install pip
sudo apt install jq
if [[ "$VIRTUAL_ENV" == "" ]]
then
pip install virtualenv
fi