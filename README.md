<img src="https://github.com/continuumsecurity/IriusTest.core/blob/master/themes/default/assets/images/logo_iriustest.png" width="300px"/>

# IriusTest.core
A Threat Model as Code framework that uses the [Gauge](https://gauge.org) BDD framework to describe a threat model and to implement tests that verify the presence of countermeasures. It uses Python to implement the tests.  This is a generic implementation that can be adapted to test specific security domains.

## Install
* Install python3
* Install [Gauge](https://gauge.org/getting-started-guide/quick-install/)
* Install the necessary Python modules:
```
pip install sure
pip install pyyaml
```

## Define the Threat Model
Each threat should be created in its own markdown file in the threatmodel directory.  This file can contain any number of countermeasures and each countermeasure must contain at least one test step.
Each test step should be mapped to python code in the step_impl directory.  See the common_impl.py file for examples.

## Run
Run the tests with:
```
gauge run threatmodel
```
