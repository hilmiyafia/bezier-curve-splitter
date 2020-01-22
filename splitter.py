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

def speed(control_points, time, epsilon=1e-6):
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
   return (velocity_x ** 2 + velocity_y ** 2) ** 0.5 + epsilon

def split(control_points, interval, epsilon=1e-2, maximum_iteration=100):
   time   = [0]
   points = [control_points[0]]
   while True:
      delta_time = interval / speed(control_points, time[-1])
      for iteration in range(maximum_iteration):
         new_point   = position(control_points, time[-1] + delta_time)
         delta_point = ((new_point[0] - points[-1][0]) ** 2 + (new_point[1] - points[-1][1]) ** 2) ** 0.5
         if abs(delta_point - interval) < epsilon:
            break
         delta_time *= (interval / delta_point + 1) / 2
      new_time = time[-1] + delta_time
      if new_time > 1:
         break
      time.append(new_time)
      points.append(new_point)
   return numpy.array(time), numpy.array(points)
