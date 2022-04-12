
pyenv global 3.7.9
python3 -m pip install pyperformance
pyperformance run -r -o py30709.json  # --debug-single-value -b nbody

pyenv global 3.8.10
python3 -m pip install pyperformance
pyperformance run -r -o py30810.json  # --debug-single-value -b nbody

pyenv global 3.9.12
python3 -m pip install pyperformance
pyperformance run -r -o py30912.json  # --debug-single-value -b nbody

pyenv global 3.10.4
python3 -m pip install pyperformance
pyperformance run -r -o py31004.json  # --debug-single-value -b nbody

pyenv global 3.11.0a6
python3 -m pip install pyperformance
pyperformance run -r -o py311a6.json  # --debug-single-value -b nbody


python3 -m pyperf compare_to py30709.json py30810.json py30912.json py31004.json py311a6.json --table > pyperf.txt

pyperformance compare --csv pyperf.csv py30709.json py311a6.json
