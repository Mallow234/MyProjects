#Game Function Library
#09/01/17

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenImage import OnscreenImage
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


def changePosition(occupiedPosition, positionToMove, associatedSpace, cameraPosX, cameraPosY, cameraPosZ, positionUIelements, positionUIToSwitch, textUIElementsList, isTurnedOut, keyIsTurnedOut):
	if occupiedPosition == positionToMove:
		pass		
	elif occupiedPosition != positionToMove and isTurnedOut[keyIsTurnedOut] == False:
		camera.setPos(associatedSpace, cameraPosX, cameraPosY, cameraPosZ)

		for x in textUIElementsList:
			del x

		for i in positionUIelements:
			if i != positionUIToSwitch:
				i = displayScreenText(i['textPos'], i['posString'], 0.04)

	else:
		pass

def lookThroughSight(sightObject, screenElement, associatedSpace, cameraPosX, cameraPosY, cameraPosZ, lens, fieldOfView):
	if base.mouseWatcherNode.hasMouse():
		mpos = base.mouseWatcherNode.getMouse()
		pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())

def turnOut(occupiedPosition, associatedSpace, associatedSpaceCom, camPosX, camPosY, camPosZ, camPosXCom, camPosYCom, camPosZCom, outsideCamPosZ, outsideCamPosZCom, isTurnedOut, keyIsTurnedOut, keyOccupiedPosition):
	if isTurnedOut[keyIsTurnedOut] == False and occupiedPosition[keyOccupiedPosition] == 0:
		camera.setPos(associatedSpaceCom, camPosXCom, camPosYCom, outsideCamPosZCom)
	elif isTurnedOut[keyIsTurnedOut] == False and occupiedPosition[keyOccupiedPosition] == 3:
		camera.setPos(associatedSpace, camPosX, camPosY, outsideCamPosZ)
	elif isTurnedOut[keyIsTurnedOut] == True and occupiedPosition[keyOccupiedPosition] == 0:
		camera.setPos(associatedSpaceCom, camPosXCom, camPosYCom, camPosZCom)
	elif isTurnedOut[keyIsTurnedOut] == True and occupiedPosition[keyOccupiedPosition] == 3:
		camera.setPos(associatedSpace, camPosX, camPosY, camPosZ)
	else:
		pass


def binoculars(inBinoculars, lens, regularFOV, binocularZoom, binocularOverlay):
	if inBinoculars == False:
		inBinoculars = True
		lens.setFov(binocularZoom)
		binocularOverlay = OnscreenImage(image = '/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/misc/binocular.png', pos = (0, 0, 0))
		binocularOverlay.reparentTo(render2d)
		binocularOverlay.setTransparency(1)
		returnArray = [inBinoculars, binocularOverlay]

		return returnArray

	elif inBinoculars == True:
		inBinoculars = False
		lens.setFov(regularFOV)
		binocularOverlay.destroy()
		binocularOverlay = None
		returnArray = [inBinoculars, binocularOverlay]

		return returnArray
	else:
		pass



		
       



            

