def Position(controls, time):
   a = 1 * ((1 - time) ** 3) * (time ** 0)
   b = 3 * ((1 - time) ** 2) * (time ** 1)
   c = 3 * ((1 - time) ** 1) * (time ** 2)
   d = 1 * ((1 - time) ** 0) * (time ** 3)
   x = a * controls[0][0] + b * controls[1][0] + c * controls[2][0] + d * controls[3][0]
   y = a * controls[0][1] + b * controls[1][1] + c * controls[2][1] + d * controls[3][1]
   return x, y

def Speed(controls, time):
   a = 3 * ((1 - time) ** 2) * (time ** 0)
   b = 6 * ((1 - time) ** 1) * (time ** 1)
   c = 3 * ((1 - time) ** 0) * (time ** 2)
   x = a * (controls[1][0] - controls[0][0]) + b * (controls[2][0] - controls[1][0]) + c * (controls[3][0] - controls[2][0])
   y = a * (controls[1][1] - controls[0][1]) + b * (controls[2][1] - controls[1][1]) + c * (controls[3][1] - controls[2][1])
   return (x ** 2 + y ** 2) ** 0.5

def Split(controls, interval, epsilon=1e-2, maximum_iteration=100):
   times = [0]
   points = [controls[0]]
   while True:
      delta_time = interval / (Speed(controls, times[-1]) + 1e-6)
      for iteration in range(maximum_iteration):
         new_time = times[-1] + delta_time
         new_point = Position(controls, new_time)
         delta_point = ((new_point[0] - points[-1][0]) ** 2 + (new_point[1] - points[-1][1]) ** 2) ** 0.5
         if abs(delta_point - interval) < epsilon: break
         delta_time *= 0.5 * (interval / delta_point + 1)
      if new_time > 1: break
      times.append(new_time)
      points.append(new_point)
   return times, points
