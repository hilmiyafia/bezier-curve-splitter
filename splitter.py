import math
import numpy

def position(control_points, time):
   position_x = (
      1 * ((1 - time) ** 3) * (time ** 0) * control_points[0][0] +
      3 * ((1 - time) ** 2) * (time ** 1) * control_points[1][0] +
      3 * ((1 - time) ** 1) * (time ** 2) * control_points[2][0] +
      1 * ((1 - time) ** 0) * (time ** 3) * control_points[3][0]
   )
   position_y = (
      1 * ((1 - time) ** 3) * (time ** 0) * control_points[0][1] +
      3 * ((1 - time) ** 2) * (time ** 1) * control_points[1][1] +
      3 * ((1 - time) ** 1) * (time ** 2) * control_points[2][1] +
      1 * ((1 - time) ** 0) * (time ** 3) * control_points[3][1]
   )
   return position_x, position_y

def speed(control_points, time):
   velocity_x = (
      3 * ((1 - time) ** 2) * (time ** 0) * (control_points[1][0] - control_points[0][0]) +
      6 * ((1 - time) ** 1) * (time ** 1) * (control_points[2][0] - control_points[1][0]) +
      3 * ((1 - time) ** 0) * (time ** 2) * (control_points[3][0] - control_points[2][0])
   )
   velocity_y = (
      3 * ((1 - time) ** 2) * (time ** 0) * (control_points[1][1] - control_points[0][1]) +
      6 * ((1 - time) ** 1) * (time ** 1) * (control_points[2][1] - control_points[1][1]) +
      3 * ((1 - time) ** 0) * (time ** 2) * (control_points[3][1] - control_points[2][1])
   )
   return math.sqrt(velocity_x ** 2 + velocity_y ** 2) + 1e-6

def split(control_points, interval, epsilon=1e-2, maximum_iteration=100):
   time   = [0]
   points = [control_points[0]]
   while True:
      iteration  = 0
      delta_time = interval / speed(control_points, time[-1])
      while True:
         new_position   = position(control_points, time[-1] + delta_time)
         delta_position = math.sqrt(
            (new_position[0] - points[-1][0]) ** 2 + 
            (new_position[1] - points[-1][1]) ** 2
         )
         iteration += 1
         if abs(delta_position - interval) < epsilon or iteration > maximum_iteration:
            break
         delta_time *= (interval / delta_position + 1) / 2
      time.append(time[-1] + delta_time)
      points.append(new_position)
      if time[-1] > 1:
         break
   return numpy.array(time[:-1]), numpy.array(points[:-1])
