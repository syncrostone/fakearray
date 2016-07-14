# fakearray

> simulated n-dimensional array data

Small package for generating different kinds of structured array data, for scientific and numerical computing applications. Each method returns one or more arrays, and optionally returns a dictionary of parameters used in the simulation.

# example

```python
import fakearray as fa 

images = fa.calcium_imaging(k=5)
mat = fa.low_rank(k=5, n=100)
```

# current data types

- `calcium_imaging`

# planned additions

- `low_rank`

