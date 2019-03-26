# Fuzzer SDK for regular people

This repo is intended as a test case for creating a python general purpose SDK for building fuzzers;

The intention of this framework is to be executed in a distributed environment in which each node orchestrates its fuzzing sessions internally.

A shared location is used to commute the next data elements:
* Samples Corpus for input to the fuzzing
* Logging repository
* Coverage and statistics repository
* Crash repository 

### Main components
The SDK composed of the next components:
* Main Fuzzer dispatcher with life cycle awareness & resource monitoring ⚡️
* Generator strategy provider - serving the fuzzer with samples from corpus(es) ⚡️
* Logging Service collecting and minimizing fuzzing run logs 📬
* Coverage Service collecting and minimizing fuzzing run statistics  📬
* Crash analyzer Service collecting analyzing crash 📬


## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/rmotr/flask-api-example.git
$ cd flask-api-example
```

##### Create the virtualenv
```bash
$ mkvirtualenv flask-api-example
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Run the app
```bash
$ python run_app.py
```

## Running the app

```bash
$ python run_app.py
```


## Test

```bash
$ make test
```
