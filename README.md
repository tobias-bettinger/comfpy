# comfpy
Several python scripts for the offline evaluation of ride comfort in vehicles using measured acceleration signals follwing diverse standards, such as EN 12299 or Wz-Method.

## Current state
+ EN 12299: filtering implemented and calculation of CC-values
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
```ax1, ay1, az1``` are all ```np.ndarray``` datatypes.

The channels dictionary may also contain more channels:
```python
channels = {'x': {'1': ax1, '2': ax2, ..., 'n': axn},
            'y': {'1': ay1, '2': ay2, ..., 'n': ayn},
            'z': {'1': az1, '2': az2, ..., 'n': azn}}
```
If more channels are provided, each method will iterate over all data and calculate the comfort indices for each channel and direction following the method, described in each standard respectively.

### EN 12299
A detailed description of the method can be found in <a id="1">[1]</a>. Using the previously composed channels dictionary ```channels```, a sample frequency of the acceleration channels of ```fs=200``` Hz (consistancy for each channel assumed), the Continuous Comfort Values CC can be calculated. The application of the appropriate filters is done automatically:
```python
f = en12299(fs=200, channels=channels, analyse='full')
print(f.get('1', 'cc'))
```
...will output:
```
             x         y         z
0     0.001375  0.000607  0.002540
1     0.001360  0.000623  0.005034
2     0.073673  0.003369  0.013517
3     0.027843  0.012021  0.030859
4     0.042937  0.030399  0.071295
        ...       ...       ...
```

### Wz Values
```python
w = wz(fs=200, channels=channels, analyse='full')
print(w.get('1', 'wz'))
```
# References
<a id="1">[1]</a> EN 12299:2009. Railway applications-ride comfort for passengers-measurements and evaluation. Brussels: CEN; 2009 April.
