pyinstaller --clean -c -F --icon=".\GW2TG\icon.ico" ".\GW2TG\Start.py" -n "GW2TG.exe"
COPY ".\GW2TG\icon.ico" ".\dist\icon.ico"
COPY ".\GW2TG\players.tsv" ".\dist\players.tsv"
pause