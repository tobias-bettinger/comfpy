# comfpy
Several python scripts for the offline evaluation of ride comfort in vehicles using measured acceleration signals follwing diverse standards, such as EN 12299 or Wz-Method.

## Current state
+ EN 12299: filtering implemented
+ Wz: Filtering and calculation of Wz-values

## To Do
+ ISO 2631: additional filters need to be implemented
+ ISO / EN: RMS, VDV, ... missing
+ Random test signal generator
+ add measured test data
+ Maybe introduce ```sensor objects``` that contain multiple acceleration channels
+ ```measurement setup``` containing ```sensor objects```

## Usage
First a channels dictionary needs to be composed:
```python
channels = {'x': {'1': ax1},
            'y': {'1': ay1},
            'z': {'1': az1}}
```
