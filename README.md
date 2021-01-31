# Code base describing different algos written in python

This is a practice repo for my own understanding programming languages. At the same time follow python standards 
when declaring python projects, usage of python virtual environment, pytests


### Build and install

```python3
python3 setup.py clean build install

### Run tests
To run unit tests alone -

```
pytest tests

or

python3 setup.py test
```

### Lint the code

```pylint
cd algos
pylint  *
```

### Lint the test cases too

```pylint
cd tests/algos
pylint  *
```