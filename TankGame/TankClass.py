#TankGame
#Tank class
#07/1/2017

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from direct.interval.IntervalGlobal import *

class crewPosition(object):
	def __init__(self, occupiedPosition, associatedComponent, camPosX, camPosY, camPosZ):
		self.occupiedPosition = occupiedPosition
		self.associatedComponent = associatedComponent
		self.camPosX = camPosX
		self.camPosY = camPosY
		self.camPosZ = camPosZ

class visionBlock(object):
	model = None
	texture = None

	associatedComponent = None
	posX = None
	posY = None
	posZ = None

	associatedCamComponent = None
	camPosX = None
	camPosY = None
	camPosZ = None
	camHeading = None
	camPitch = None

	viewportTexture = None

	def lookThroughVisionBlock(self, camera):
		camera.setPos(associatedCamComponent, camPosX, camPosY, camPosZ)
		camera.setH(camHeading)
		camera.setP(camPitch)


	
		











