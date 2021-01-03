# comfpy
Several python scripts for the offline evaluation of ride comfort in vehicles using measured acceleration signals follwing diverse standards, such as EN 12299 or Wz-Method.

## Current state
+ EN 12299: filtering implemented
+ Wz: Filtering and calculation of Wz-values

## To Do
+ ISO 2631: additional filters need to be implemented
+ ISO 2631: VDV, ... missing
+ add measured test data
+ Maybe introduce ```sensor objects``` that contain multiple acceleration channels (at the moment channels dict is used)
+ ```measurement setup``` containing ```sensor objects```

## Usage
First a channels dictionary needs to be composed:
```python
channels = {'x': {'1': ax1},
            'y': {'1': ay1},
            'z': {'1': az1}}
```
### EN 12299
```python
f = en12299(fs=200, channels=channels, analyse='full')
print(f.get('1', 'cc'))
```

### Wz Values
```python
w = wz(fs=200, channels=channels, analyse='full')
print(w.get('1', 'wz'))
```
# References
<a id="1">[1]</a> EN 12299:2009. Railway applications-ride comfort for passengers-measurements and evaluation. Brussels: CEN; 2009 April.
