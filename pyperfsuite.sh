
sudo apt update
sudo apt upgrade -y
pyenv update || cd ~/.pyenv && git pull && cd

# Install some Python versions
pyenv install --skip-existing 3.7.9
pyenv install --skip-existing 3.8.10
pyenv install --skip-existing 3.9.12
pyenv install --skip-existing 3.10.4
pyenv install --skip-existing 3.11.0a6

pyenv global system
python3 -m pip install --upgrade pip || sudo apt install python3-pip
python3 -m pip install --upgrade pyperformance || python3 -m pip install pyperformance
python3 -m pyperformance run -r -o pyperfsys.json

pyenv global 3.7.9
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyperformance || python3 -m pip install pyperformance
python3 -m pyperformance run -r -o pyperf30709.json

pyenv global 3.8.10
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyperformance || python3 -m pip install pyperformance
python3 -m pyperformance run -r -o pyperf30810.json

pyenv global 3.9.12
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyperformance || python3 -m pip install pyperformance
python3 -m pyperformance run -r -o pyperf30912.json

pyenv global 3.10.4
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyperformance || python3 -m pip install pyperformance
python3 -m pyperformance run -r -o pyperf31004.json

pyenv global 3.11.0a6
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade pyperformance || python3 -m pip install pyperformance
python3 -m pyperformance run -r -o pyperf311a6.json

pyenv global system

python3 -m pyperf compare_to pyperf30709.json pyperf30810.json pyperf30912.json pyperf31004.json pyperf311a6.json pyperfsys.json --table > pyperftable.txt
pyperformance compare --csv pyperfdata.csv py30709.json py311a6.json
