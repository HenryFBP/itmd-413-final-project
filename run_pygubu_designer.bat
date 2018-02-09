pygubu-designer >nul 2>&1 && (
	echo "Pygubu Designer found. Running."
	EXIT
) || (
	pip3 install pygubu-designer
)
PAUSE