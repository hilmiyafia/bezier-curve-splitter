# Bezier Curve Splitter
This repository contains a python module that splits a bezier curve into several points with specified interval / distance.

## Example
<p align="center">
  <img src="example.gif">
</p>

## Usage Example
```python
import splitter
import matplotlib.pyplot as pyplot

points_interval = 0.5
control_points = [
  [0,  0],
  [0,  5],
  [5, -5],
  [5,  0]
]

time, points = splitter.split(control_points, points_interval)

point_x = [point[0] for point in points]
point_y = [point[1] for point in points]

pyplot.plot(point_x, point_y)
pyplot.scatter(point_x, point_y)
pyplot.show()
```
