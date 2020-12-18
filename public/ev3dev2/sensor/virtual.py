import simPython, time

# Needed to prevent loops from locking up the javascript thread
SENSOR_DELAY = 0.001

class GPSSensor:
  _DRIVER_NAME = 'virtual-gps'

  def __init__(self, address=None):
    self.sensor = simPython.GPSSensor(address)

  @property
  def position(self):
    time.sleep(SENSOR_DELAY)
    pos = tuple(self.sensor.position())
    return (float(pos[0]), float(pos[2]), float(pos[1]))

  @property
  def x(self):
    return self.position[0]

  @property
  def y(self):
    return self.position[1]

  @property
  def altitude(self):
    return self.position[2]

class Pen:
  _DRIVER_NAME = 'virtual-pen'

  def __init__(self, address=None):
    self.pen = simPython.Pen(address)

  def down(self):
    self.pen.down()

  def up(self):
    self.pen.up()

  def isDown(self):
    return self.pen.isDown()

  def setColor(self, r=0.5, g=0.5, b=0.5):
    """
    Set the color of the current pen trace.  rgb values should be in the
    range [0,1].  If called after pen down(), will affect the trace
    from the down() point.
    """
    for channel_val, c_name in [(r, 'red'), (g, 'green'), (b, 'blue')]:
      if channel_val < 0.0 or channel_val > 1.0:
        raise ValueError('{} color channel must be in range [0,1]', c_name)
      self.pen.setColor(r, g, b)

  def setWidth(self, width=1.0):
    self.pen.setWidth( width )
