#Game Function Library
#09/01/17

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from direct.interval.IntervalGlobal import *
import TankClass

def configureCamera(lens, fieldOfView, nearDistance, farDistance):
	lens.setFov(fieldOfView)
	lens.setNear(nearDistance)
	lens.setFar(farDistance)

	return lens

def loadVehicleComponent(model, texture, componentName, objectParent, posX, posY, posZ):
	#loads model and reparents to render
	componentName = loader.loadModel(model)
	componentName.reparentTo(render)

	#loads texture and applies to model
	componentTexture = loader.loadTexture(texture)
	componentName.setTexture(componentTexture)

	#sets orientation
	if objectParent != None: 
	    componentName.setPos(objectParent, posX, posY, posZ)

	return componentName

def displayScreenText(pos, msg, size):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), scale=size,
                        shadow=(0, 0, 0, 1), parent=base.a2dTopLeft,
                        pos=(0.08, -pos - 0.04), align=TextNode.ALeft)


def changePosition(occupiedPosition, positionToMove, associatedSpace, cameraPosX, cameraPosY, cameraPosZ, positionUIelements, positionUIToSwitch, textUIElementsList):
	if occupiedPosition == positionToMove:
		pass		
	else:
		camera.setPos(associatedSpace, cameraPosX, cameraPosY, cameraPosZ)

		for x in textUIElementsList:
			del x

		for i in positionUIelements:
			if i != positionUIToSwitch:
				i = displayScreenText(i['textPos'], i['posString'], 0.04)

def lookThroughSight(sightObject, screenElement, associatedSpace, cameraPosX, cameraPosY, cameraPosZ, lens, fieldOfView):
	if base.mouseWatcherNode.hasMouse():
		mpos = base.mouseWatcherNode.getMouse()
		pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())


		
       



            

