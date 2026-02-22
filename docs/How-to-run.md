# How to run

## Prerequisite
1. Ensure virtual environment is active
2. In command line, run ```pip install -r requirements.txt```
3. In command line, run ```pip install -e .```

## Running program
```bash
python -m simulation
```

## Running tests
```bash
# All tests (test files must start with test*)
python -m nose2

# Run individual test
python -m unittest <Test file path>

# Example
python -m unittest .\src\tests\test_plane_eqs.py   
```