pyinstaller --noconsole --clean --icon=".\GW2TG\icon.ico" ".\GW2TG\Start.py" -n "GW2TG.exe"
COPY ".\GW2TG\icon.ico" ".\dist\GW2TG.exe\icon.ico"
COPY ".\GW2TG\players.tsv" ".\dist\GW2TG.exe\players.tsv"
pause