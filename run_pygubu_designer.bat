SET uifile=gui_pygubu.ui

pygubu-designer "%uifile%" >nul 2>&1 && (
	echo "Pygubu Designer found. Running."
	EXIT
) || (
	pip3 install pygubu
)
PAUSE