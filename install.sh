sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get -y install postgresql

sudo apt-get install python3-dev libpq-dev -y
sudo apt-get install python3-venv -y

pip install venv

python3 -m venv env/
source env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt 

sudo -i -u postgres psql
ALTER USER postgres PASSWORD 'postgres';
create database weatherprobe;
exit

python3 ./database/create_init_tables.py
pip install .

echo "Installation successfull"
