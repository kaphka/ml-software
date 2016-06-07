import vispy
from vispy import app, scene, color
from vispy import visuals
from vispy.visuals.transforms import STTransform
from vispy.geometry import create_box

import sys
import pickle
import os.path as op
import numpy as np


# In[2]:

with open('../theano/xor.keras' ,'rb') as kmodel:
    model = pickle.load(kmodel)


# In[5]:

canvas = scene.SceneCanvas(keys='interactive')
canvas.size = 800, 600
canvas.show()
view = canvas.central_widget.add_view()
interpolation = 'nearest'


xoffset = 0
yoffset = 0
line_data = np.array([[0,0],[10,0]],np.float32)
line1 = scene.visuals.Line(pos=line_data, color='red', method='gl',
                           antialias=False, name='line1', parent=view.scene)
for weight in model.get_weights():
    if len(weight.shape) <= 1:
        continue
    m, n = weight.shape
    yoffset = -m
    print('offset: {},{}  shape: {},{}'.format(xoffset,yoffset, m, n))
    image = scene.visuals.Image(weight, interpolation=interpolation,
                                parent=view.scene, cmap='grays', method='auto')
    image.transform = STTransform(scale=(1, 1), translate=(xoffset, yoffset))
    
    xoffset = xoffset + n

canvas.title = ''

# Set 2D camera (the camera will scale to the contents in the scene)
view.camera = scene.PanZoomCamera(aspect=1)
# flip y-axis to have correct aligment
view.camera.flip = (0, 1, 0)
view.camera.set_range()
view.camera.zoom(0.1, (0, 0))

if __name__ == '__main__' and sys.flags.interactive == 0:
    app.run()




