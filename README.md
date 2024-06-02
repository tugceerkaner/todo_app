# Capstone Project
- CLI commands for build, test and coverage

## Run the source code
```python main.py``` 

## Run the unit tests
```python -m unittest discover tests ```<br>
```python -m unittest tests/test_routes.py```<br>
```python -m unittest```</br></br>

## Coverage information
```coverage run -m unittest discover``` <br>
- creates .coverage output <br>

```coverage report``` <br>
- to see coverage detail, not necessary for the xml report <br>

```coverage xml``` 
- creates coverage.xml report, it will use Sonarcloud integration <br> 