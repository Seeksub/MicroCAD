# MicroCAD


## Simple CAD 2D application.


>#### Application in development.


### To setup enviroment:


* clone this project:
```shell script 
git clone <project-link>
```
* open ```MicroCAD``` directory:
```shell script
cd MicroCAD
```
* run in the terminal following command to setup ```pipenv```:
```shell script
pipenv install
```
* Now move to the ```MicroCAD/src```:
```shell script
cd src
```
* Load ```pipenv``` enviroment and run ```main.py``` file:
```shell script
pipenv shell
python main.py
```
## There're 3 modules
1. ```main.py``` - executebla module with UI class
2. ```geometry_generator.py``` -  create structure of draw objects
3. ```geometry_solver.py``` - 8 geometry constraint solutions for objects
> All modules are in progress