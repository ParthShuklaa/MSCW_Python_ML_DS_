import matplotlib.pyplot as pt
from matplotlib.image import
from matplotlib import *

#Select * from Emp
from matplotlib import pyplot as pt1
import matplotlib.image as im

myImage = im.imread("phelps.PNG")

print(im)
print(myImage)

imgplt =  pt.imshow(myImage)
pt.colorbar()
pt.show()

NewImage = myImage[:,:,0]
pt.imshow(NewImage,cmap="hot")
pt.imshow(NewImage)
pt.show()


