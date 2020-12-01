import matplotlib.pyplot as plt

red_x = [3,5,7,3]
red_y = [3,5,3,3]
blue_x = [3,5,7,3]
blue_y = [5,3,5,5]
green_x = [3,3,7,3]
green_y = [3,5,4,3]
yellow_x = [7,7,3,7]
yellow_y = [3,5,4,3]

def combined():
  plt.plot(red_x, red_y, 'ro--')
  plt.plot(blue_x, blue_y, 'bs:')
  plt.plot(green_x, green_y, 'g*-.')
  plt.plot(yellow_x, yellow_y, 'yp-')

plt.show()
combined()

def separated():
	fig, axes = plt.subplots(2,2)
	axes[0,0].plot (red_x, red_y, 'ro--')
	axes[0,1].plot (blue_x, blue_y, 'bs:')
	axes[1,0].plot (green_x, green_y, 'g*-.')
	axes[1,1].plot (yellow_x, yellow_y, 'yp-')
  
separated()

def data():

	red = {"x":[3,5,7,3] , "y":[3,5,3,3], "format":"ro--"}
	blue = {"x":[3,5,7,3] , "y":[5,3,5,5], "format":"bs:" }
	green = {"x":[3,3,7,3] , "y":[3,5,4,3], "format":"g*-."}
	yellow = {"x":[7,7,3,7] , "y":[3,5,4,3], "format":"yp-"}
	return [red,blue,green,yellow]

def improved_separated():

  values = data()
  fig, axes = plt.subplots(2,2)
  axes[0,0].plot (values[0]['x'], values[0]['y'], values[0]['format'])
  axes[0,1].plot (values[1]['x'], values[1]['y'], values[1]['format'])
  axes[1,0].plot (values[2]['x'], values[2]['y'], values[2]['format'])
  axes[1,1].plot (values[3]['x'], values[3]['y'], values[3]['format'])
  plt.show()

improved_separated()