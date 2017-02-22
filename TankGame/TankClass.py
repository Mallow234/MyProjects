#TankGame
#Tank class
#07/1/2017

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from direct.interval.IntervalGlobal import *
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import WindowProperties
import GameFunctionLibrary

class Player_Tank_Pat41(object):
	def __init__(self, scene, posX, posY, posZ):
		self.scene = scene
		self.posX = posX
		self.posY = posY
		self.posZ = posZ

		self.hullModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/tankhull.egg"
		self.hullTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/hulluv.png" 

		self.turretModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/tankturret.egg"
		self.turretTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretuv.png"

		self.gunModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/tankgun.egg"
		self.gunTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/gunuv.png"

		self.hullInteriorModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/hullinterior.egg"
		self.hullInteriorTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/hullinteriorcolour.png"

		self.turretInteriorModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretinterior.egg"
		self.turretInteriorTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretinteriorcolour.png"

		self.breechAssemblyModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechassembly.egg"
		self.breechAssemblyTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechcolour.png"

		self.breechBar1ModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldbar1.egg"
		self.breechBar2ModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldbar2.egg"
		self.breechBarTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldbar2uv.png"

		self.breechMeshModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldmesh.egg"
		self.breechMeshTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldmeshuv.png"

		self.driverSeatModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverseat.egg"
		self.driverSeatTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverseatuv.png"

		self.controlBarLeftModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/leftcontrolbar.egg"
		self.controlBarRightModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/rightcontrolbar.egg"
		self.controlBarTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverstickuv.png"

		self.pedalLeftModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/acceleratorleft.egg"
		self.pedalRightModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/acceleratorright.egg"
		self.pedalTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverpedaluv.png"

		self.controlPanelModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverinfopanel.egg"
		self.controlPanelTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverControlPanelUV.png"

		self.seatsModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretseats.egg"
		self.seatsTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretseatuv.png"

		self.turretPowerTraverseModelData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretpowertraverse.egg"
		self.turretPowerTraverseTextureData = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretpowertraversecolour.png"










class crewPosition(object):
	def __init__(self, occupiedPosition, associatedComponent, camPosX, camPosY, camPosZ):
		self.occupiedPosition = occupiedPosition
		self.associatedComponent = associatedComponent
		self.camPosX = camPosX
		self.camPosY = camPosY
		self.camPosZ = camPosZ

class visionBlock(object):
	def __init__(self, associatedComponent, posX, posY, posZ, model, texture, associatedCamComponent, camPosX, camPosY, camPosZ, camHeading, camPitch, visionBlockTexture, visionBlockFOV, regularFOV, lens):
		self.associatedComponent = associatedComponent
		self.posX = posX
		self.posY = posY
		self.posZ = posZ

		self.model = model
		self.texture = texture

		self.associatedCamComponent = associatedCamComponent
		self.camPosX = camPosX
		self.camPosY = camPosY
		self.camPosZ = camPosZ
		self.camHeading = camHeading
		self.camPitch = camPitch

		self.visionBlockTexture = visionBlockTexture
		self.visionBlockFOV = visionBlockFOV
		self.regularFOV = regularFOV

		self.lens = lens



	def initialiseVisionBlock(self):
		visionBlockName = loader.loadModel(self.model)
		visionBlockName.reparentTo(render)

		visionBlockTexture = loader.loadTexture(self.texture)
		visionBlockName.setTexture(visionBlockTexture)

		visionBlockName.setPos(self.associatedComponent, self.posX, self.posY, self.posZ)

		return visionBlockName

	def lookInVisionBlock(self, inViewport, visionBlockOverlay):
		if inViewport == False:
			camera.setPos(self.associatedCamComponent, self.camPosX, self.camPosY, self.camPosZ)
			camera.setHpr(0, 0, 0)
			visionBlockOverlay = OnscreenImage(self.visionBlockTexture, pos = (0, 0, 0))
			visionBlockOverlay.setTransparency(1)
			visionBlockOverlay.reparentTo(render2d)
			self.lens.setFov(self.visionBlockFOV)
			return visionBlockOverlay

		elif inViewport == True:
			visionBlockOverlay.destroy()
			self.lens.setFov(self.regularFOV)
			return visionBlockOverlay





class AI_Tank_Type37(object):
	def __init__(self, terrain, spawnPosX, spawnPosY, spawnPosZ, spawnDir, vehicleID):
		self.hullModel = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/Type37/Type37Hull.egg"
		self.hullTexture = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/Type37/HullUV.png"

		self.turretModel = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/Type37/Type37Turret.egg"
		self.turretTexture = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/Type37/TurretUV.png"

		self.gunModel = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/Type37/Type37Gun.egg"
		self.gunTexture = "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/Type37/GunUV.png"

		self.vehicleID = vehicleID

		self.terrainSpawn = terrain
		self.spawnPosX = spawnPosX
		self.spawnPosY = spawnPosY
		self.spawnPosZ = spawnPosZ
		self.spawnDir = spawnDir

	def spawnTank(self):
		tankHull = loader.loadModel(self.hullModel)
		tankHull.reparentTo(render)
		tankHullTexture = loader.loadTexture(self.hullTexture)
		tankHull.setTexture(tankHullTexture)

		tankTurret = loader.loadModel(self.turretModel)
		tankTurret.reparentTo(render)
		tankTurretTexture = loader.loadTexture(self.turretTexture)
		tankTurret.setTexture(tankTurretTexture)
		tankTurret.setPos(tankHull, 0, 0, 0)

		tankGun = loader.loadModel(self.gunModel)
		tankGun.reparentTo(render)
		tankGunTexture = loader.loadTexture(self.gunTexture)
		tankGun.setTexture(tankGunTexture)
		tankGun.setPos(tankTurret, 0, 0, 0)

		tankComponentArray = [tankHull, tankTurret, tankGun]

		for x in tankComponentArray:
			x.setPos(self.terrainSpawn, self.spawnPosX, self.spawnPosY, self.spawnPosZ)
			x.setH(self.spawnDir)

		return tankComponentArray









	
		











