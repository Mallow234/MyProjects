#TankGame Iteration 0.0.3
#10/01/2016

#Please see changelog for changes

from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import PandaNode, NodePath, Camera, TextNode
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionHandlerEvent, CollisionRay, CollisionPolygon, CollisionSphere, Point3
from panda3d.core import LPoint3, LVector3, BitMask32
from panda3d.core import WindowProperties
from direct.showbase.DirectObject import DirectObject
from direct.task.Task import Task
from direct.gui.OnscreenImage import OnscreenImage
import math
import TankClass
import GameFunctionLibrary

tankHullLoader = 0
tankTurretLoader = 0
tankGunLoader = 0
interiorTurretLoader = 0
interiorHullLoader = 0
breechAssemblyLoader = 0
breechBar1Loader = 0
breechBar2Loader = 0
breechMeshLoader = 0
gunnerPrimarySightLoader = 0
gunnerSecondarySightLoader = 0
driverSeatLoader = 0
driverVisionBlockLoader = 0
driverPedal1Loader = 0
driverLeftBarLoader = 0
driverRightBarLoader = 0

hullData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/tankhull.egg", "/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/hulluv.png"]
turretData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/tankturret.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretuv.png"]
gunData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/tankgun.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/gunuv.png"]
turretInteriorData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretinterior.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretinteriorcolour.png"]
hullInteriorData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/hullinterior.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/hullinteriorcolour.png"]

breechAssemblyData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechassembly.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechcolour.png"]
breechBar1Data = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldbar1.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldbar1uv.png"]
breechBar2Data = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldbar2.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldbar2uv.png"]
breechMeshData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldmesh.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/breechshieldmeshuv.png"]
gunnerPrimarySightData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/gunnerprimarysight.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/gunnerprimarysightcolour.png"]
gunnerSecondarySightData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/gunnersecondarysight.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/gunnersecondarysightcolour.png"]
turretSeatsData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretseats.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretseatuv.png"]
turretPowerTraverseData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretpowertraverse.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/turretpowertraversecolour.png"]
commanderVisionBlockFrontData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/cupolavisionblockfront.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/commandervisionblockcolour.png"]
commanderVisionBlockLeftData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/cupolavisionblockleft.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/commandervisionblockcolour.png"]
commanderVisionBlockRightData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/cupolavisionblockright.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/commandervisionblockcolour.png"]
commanderVisionBlockBackData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/cupolavisionblockrear.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/commandervisionblockcolour.png"]

driverSeatData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverseat.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverseatuv.png"]
driverVisionBlockData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/drivervisionblock.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/drivervisionblockuv.png"] 
driverPedal1Data = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/acceleratorright.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverpedaluv.png"]
driverPedal2Data = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/acceleratorleft.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverpedaluv.png"]
driverLeftBarData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/leftcontrolbar.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverstickuv.png"]
driverRightBarData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/rightcontrolbar.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverstickuv.png"]
driverControlPanelData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverinfopanel.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/driverControlPanelUV.png"]
driverIgnitionSwitchData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/ignitionswitch.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/buttonUVs.png"]
driverAuxPowerSwitchData = ["/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/auxpowerswitch.egg","/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/buttonUVs.png"]


class TankGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #loading basic scene
        self.scene = self.loader.loadModel("/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/scene.egg")

        self.scene.reparentTo(self.render)

        self.scene.setScale(3, 3, 3)
        self.scene.setPos(0, 0, 0)

        #make ground model twosided
        self.scene.set_two_sided(True)

        base.disableMouse()

        #loading environment texture
        envTexture = loader.loadTexture("/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/groundtexture.png")

        self.scene.setTexture(envTexture)

        commanderText = {'textPos': 0.1, 'posString': "Commander"}
        self.gunnerText = {'textPos': 0.15, 'posString': "Gunner"}
        loaderText = {'textPos': 0.2, 'posString': "Loader"}
        driverText = {'textPos': 0.25, 'posString': "Driver"}

        self.positionUIElements = [commanderText, self.gunnerText, loaderText, driverText]

        self.positionUIElementsActive = []

        self.lens = self.cam.node().getLens()

        global props
        props = WindowProperties()

        GameFunctionLibrary.configureCamera(self.lens, 105, 0.1, 3000)

        base.messenger.toggleVerbose()

        self.keyMap = {"rotateCamera": 0}

        self.occupiedPosition = {"occupiedPosition": 0}

        self.turnedOut = {"isTurnedOut": False}

        self.isInViewport = {"isLookingOut": False}

        self.inBinoculars = False

        self.binocularOverlay = None

        self.inViewport = False

        self.viewportOverlay = None

        self.lookingEnabled = True

        self.turretLeft = {"turretLeft": False}

        self.turretRight = {"turretRight": False}

        self.gunElevate = {"gunUp": False}

        self.gunDepress = {"gunDown": False}




        #load models and texture (FOR EXTERIOR)
        tankHull = GameFunctionLibrary.loadVehicleComponent(hullData[0] , hullData[1], tankHullLoader, None, 0, 0, 0)

        tankHull.setPos(0,0,0)

        self.tankTurret = GameFunctionLibrary.loadVehicleComponent(turretData[0], turretData[1], tankTurretLoader, tankHull, 0, 0.15, 2.64)

        self.tankGun = GameFunctionLibrary.loadVehicleComponent(gunData[0], gunData[1], tankGunLoader, self.tankTurret, 0, 1.3, 0)

        #load models and texture (FOR INTERIOR)
        self.turretInteriorSpace = GameFunctionLibrary.loadVehicleComponent(turretInteriorData[0], turretInteriorData[1], interiorTurretLoader, self.tankTurret, 0, 0, 0)

        hullInteriorSpace = GameFunctionLibrary.loadVehicleComponent(hullInteriorData[0], hullInteriorData[1], interiorHullLoader, tankHull, 0, 0, 0)

        breech = GameFunctionLibrary.loadVehicleComponent(breechAssemblyData[0], breechAssemblyData[1], breechAssemblyLoader, self.tankGun, 0, 0, 0)

        breechBar1 = GameFunctionLibrary.loadVehicleComponent(breechBar1Data[0], breechBar1Data[1], breechBar1Loader, self.tankGun, 0, 0, 0)

        breechBar2 = GameFunctionLibrary.loadVehicleComponent(breechBar2Data[0], breechBar2Data[1], breechBar2Loader, self.tankGun, 0, 0, 0)

        breechMesh = GameFunctionLibrary.loadVehicleComponent(breechMeshData[0], breechMeshData[1], breechMeshLoader, self.tankGun, 0, 0, 0)

        gunnerSecondarySight = GameFunctionLibrary.loadVehicleComponent(gunnerSecondarySightData[0], gunnerSecondarySightData[1], gunnerSecondarySightLoader, self.turretInteriorSpace, 0, 0, 0)

        turretPowerTraverse = GameFunctionLibrary.loadVehicleComponent(turretPowerTraverseData[0], turretPowerTraverseData[1], gunnerSecondarySightLoader, self.turretInteriorSpace, 0, 0, 0)

        turretSeats = GameFunctionLibrary.loadVehicleComponent(turretSeatsData[0], turretSeatsData[1], gunnerSecondarySightLoader, self.turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockFront = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockFrontData[0], commanderVisionBlockFrontData[1], gunnerSecondarySightLoader, self.turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockLeft = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockLeftData[0], commanderVisionBlockLeftData[1], gunnerSecondarySightLoader, self.turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockRight = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockRightData[0], commanderVisionBlockRightData[1], gunnerSecondarySightLoader, self.turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockRear = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockBackData[0], commanderVisionBlockBackData[1], gunnerSecondarySightLoader, self.turretInteriorSpace, 0, 0, 0)


        driverSeat = GameFunctionLibrary.loadVehicleComponent(driverSeatData[0], driverSeatData[1], driverSeatLoader, hullInteriorSpace, 0, 0, 0)

        driverVisionBlock = GameFunctionLibrary.loadVehicleComponent(driverVisionBlockData[0], driverVisionBlockData[1], driverVisionBlockLoader, hullInteriorSpace, 0, 0, 0)

        driverRightPedal = GameFunctionLibrary.loadVehicleComponent(driverPedal1Data[0], driverPedal1Data[1], driverPedal1Loader, hullInteriorSpace, 0, 0, 0)

        driverLeftPedal = GameFunctionLibrary.loadVehicleComponent(driverPedal2Data[0], driverPedal2Data[1], driverPedal1Loader, hullInteriorSpace, 0, 0, 0)

        driverLeftSteeringBar = GameFunctionLibrary.loadVehicleComponent(driverLeftBarData[0], driverLeftBarData[1], driverLeftBarLoader, hullInteriorSpace, 0, 0, 0)

        driverRightSteeringBar = GameFunctionLibrary.loadVehicleComponent(driverRightBarData[0], driverRightBarData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)

        driverControlPanel = GameFunctionLibrary.loadVehicleComponent(driverControlPanelData[0], driverControlPanelData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)

        ignitionSwitch = GameFunctionLibrary.loadVehicleComponent(driverIgnitionSwitchData[0], driverIgnitionSwitchData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)

        auxPowerSwitch = GameFunctionLibrary.loadVehicleComponent(driverAuxPowerSwitchData[0], driverAuxPowerSwitchData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)

        self.gunnerPrimarySight = TankClass.visionBlock(self.tankGun, 0, 0, 0, gunnerPrimarySightData[0], gunnerPrimarySightData[1], self.tankGun, 0.4, 0.2, 0.5, 0, 0, '/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/misc/primgunsight.png', 10, 105, self.lens)
        self.gunnerPrimarySightModel = self.gunnerPrimarySight.initialiseVisionBlock()
        self.gunnerPrimarySightModel.setName('gunnerPrimarySight')

        self.turretObjects = [self.tankTurret, self.tankGun, self.turretInteriorSpace, breech, breechBar1, breechBar2, breechMesh, gunnerSecondarySight, self.gunnerPrimarySightModel, turretPowerTraverse, turretSeats, commanderVisionBlockFront, commanderVisionBlockLeft, commanderVisionBlockRight, commanderVisionBlockRear]

        self.gunObjects = [self.tankGun, breech, breechBar1, breechBar2, breechMesh, self.gunnerPrimarySightModel]




        #setting position and scale of tank
        self.turretInteriorSpace.set_two_sided(True)
        hullInteriorSpace.set_two_sided(True)
        breechMesh.set_two_sided(True)

        #setting beginning camera position
        camera.setPos(self.turretInteriorSpace, 0, 0, 3)
        camera.setHpr(self.turretInteriorSpace, 0, 0, 0)

        self.commanderPosition = TankClass.crewPosition(0, self.turretInteriorSpace, 0.6, -0.6, 0.63)
        self.gunnerPosition = TankClass.crewPosition(1, self.turretInteriorSpace, 0.8, 0.2, 0.3)
        self.loaderPosition = TankClass.crewPosition(2, self.turretInteriorSpace, -0.45, -0.3, 0.3)
        self.driverPosition = TankClass.crewPosition(3, hullInteriorSpace, -0.81, 1.94, 1.86)

        GameFunctionLibrary.changePosition(self.occupiedPosition, 0, self.commanderPosition.associatedComponent, self.commanderPosition.camPosX, self.commanderPosition.camPosY, self.commanderPosition.camPosZ, self.positionUIElements, commanderText, self.positionUIElementsActive, self.turnedOut, 'isTurnedOut')

        self.accept("1",GameFunctionLibrary.changePosition, [self.occupiedPosition, 0, self.commanderPosition.associatedComponent, self.commanderPosition.camPosX, self.commanderPosition.camPosY, self.commanderPosition.camPosZ, self.positionUIElements, commanderText, self.positionUIElementsActive, self.turnedOut, 'isTurnedOut'])
        self.accept("1-up", self.changeOccupiedPosition, ["occupiedPosition", 0, self.turnedOut, 'isTurnedOut'])

        self.accept("2",GameFunctionLibrary.changePosition, [self.occupiedPosition, 1, self.gunnerPosition.associatedComponent, self.gunnerPosition.camPosX, self.gunnerPosition.camPosY, self.gunnerPosition.camPosZ, self.positionUIElements, self.gunnerText, self.positionUIElementsActive, self.turnedOut, 'isTurnedOut'])
        self.accept("2-up", self.changeOccupiedPosition, ["occupiedPosition", 1, self.turnedOut, 'isTurnedOut'])

        self.accept("3",GameFunctionLibrary.changePosition, [self.occupiedPosition, 2, self.loaderPosition.associatedComponent, self.loaderPosition.camPosX, self.loaderPosition.camPosY, self.loaderPosition.camPosZ, self.positionUIElements, loaderText, self.positionUIElementsActive, self.turnedOut, 'isTurnedOut'])
        self.accept("3-up", self.changeOccupiedPosition, ["occupiedPosition", 2, self.turnedOut, 'isTurnedOut'])

        self.accept("4",GameFunctionLibrary.changePosition, [self.occupiedPosition, 3, self.driverPosition.associatedComponent, self.driverPosition.camPosX, self.driverPosition.camPosY, self.driverPosition.camPosZ, self.positionUIElements, driverText, self.positionUIElementsActive, self.turnedOut, 'isTurnedOut'])
        self.accept("4-up", self.changeOccupiedPosition, ["occupiedPosition", 3, self.turnedOut, 'isTurnedOut'])


        self.accept("mouse3", self.setKey, ["rotateCamera", True])
        self.accept("mouse3-up", self.setKey, ["rotateCamera", False])

        self.accept("a", self.setTurretRotationLeft, ["turretLeft", True])
        self.accept("a-up", self.setTurretRotationLeft, ["turretLeft", False])

        self.accept("d", self.setTurretRotationRight, ["turretRight", True])
        self.accept("d-up", self.setTurretRotationRight, ["turretRight", False])

        self.accept("w", self.setGunUp, ["gunUp", True])
        self.accept("w-up", self.setGunUp, ["gunUp", False])

        self.accept("s", self.setGunDown, ["gunDown", True])
        self.accept("s-up", self.setGunDown, ["gunDown", False])

        self.accept("t", GameFunctionLibrary.turnOut, [self.occupiedPosition, self.driverPosition.associatedComponent, self.commanderPosition.associatedComponent, self.driverPosition.camPosX, self.driverPosition.camPosY, self.driverPosition.camPosZ, self.commanderPosition.camPosX, self.commanderPosition.camPosY, self.commanderPosition.camPosZ, 2.5, 1.3, self.turnedOut, 'isTurnedOut', 'occupiedPosition'])
        self.accept("t-up", self.setTurnedOut, ["isTurnedOut", "occupiedPosition"])

        self.accept("b", self.binoculars, ["isTurnedOut", "occupiedPosition"])

        self.accept("escape", self.lookDownPrimarySight, [True, "occupiedPosition"])

        taskMgr.add(self.rotateCamera, "rotateCameraTask")
        taskMgr.add(self.turnTurret, "turnTurretTask")
        taskMgr.add(self.slewGun, "slewGunTask")

        self.accept("space", self.fireGun)

        self.heading = 180
        self.pitch = 0
        self.mousex = 0
        self.mousey = 0
        self.last = 0
        self.mousebtn = [0, 0, 0]

        #Turret interior collision system
        self.pickingEnabledObject = None

        base.cTrav = CollisionTraverser()
        collisionHandler = CollisionHandlerEvent()

        pickerNode = CollisionNode('mouseraycnode')
        pickerNP = base.camera.attachNewNode(pickerNode)
        self.pickerRay = CollisionRay()
        pickerNode.addSolid(self.pickerRay)

        pickerNode.setTag('rays','ray1')
        base.cTrav.addCollider(pickerNP, collisionHandler)

        gunnerPrimarySightCollider = self.gunnerPrimarySightModel.attachNewNode(CollisionNode('gunnerPrimarySightCNode'))
        gunnerPrimarySightCollider.node().addSolid(CollisionSphere(0.65, -0.88, 0.03, 0.08))

        #gunnerPrimarySightCollider.show()

        gunnerPrimarySightCollider.setTag('viewport', 'gunnerPrimarySight')
        self.gunnerPrimarySightModel.setTag('viewport', 'gunnerPrimarySight')

        collisionHandler.addInPattern("%(rays)ft-into-%(viewport)it")
        collisionHandler.addOutPattern("%(rays)ft-out-%(viewport)it")

        collisionHandler.addAgainPattern("ray_again_all%(""rays"")fh%(""viewport"")ih")       

        DO = DirectObject()

        DO.accept('ray1-into-gunnerPrimarySight', self.collideInObject)
        DO.accept('ray1-out-gunnerPrimarySight', self.collideOutObject)
        DO.accept('ray_again_all', self.ObjectCollide)

        DO.accept('mouse1', self.mouseClick, ['down'])

        taskMgr.add(self.rayUpdate, "updatePicker")


        AI_Tank_1 = TankClass.AI_Tank_Type37(self.scene, 40, -40, 0, 30, 1)
        AI_Tank_1_Model = AI_Tank_1.spawnTank()

        AI_Tank_2 = TankClass.AI_Tank_Type37(self.scene, -10, 50, 0, 170, 2)
        AI_Tank_2_Model = AI_Tank_2.spawnTank()

        AI_Tank_3 = TankClass.AI_Tank_Type37(self.scene, -30, 20, 0, 180, 3)
        AI_Tank_3_Model = AI_Tank_3.spawnTank()

    def collideInObject(self, entry):
        np_into = entry.getIntoNodePath()

    def collideOutObject(self, entry):
        np_into = entry.getIntoNodePath()
        self.pickingEnabledObject = None 

    def ObjectCollide(self, entry):
        if entry.getIntoNodePath().getParent() <> self.pickingEnabledObject:
            np_from = entry.getFromNodePath()
            np_into = entry.getIntoNodePath()

            self.pickingEnabledObject = np_into.getParent()


    def mouseClick(self, status):
        if self.pickingEnabledObject != None:
            if status == 'down' and self.pickingEnabledObject.hasTag('viewport'):
                self.lookDownPrimarySight(False, "occupiedPosition")
            else:
                pass

        else:
            pass

    def rayUpdate(self, task):
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())

        return task.cont

    def setKey(self, key, value):
        self.keyMap[key] = value

    def setTurretRotationLeft(self, key, value):
        self.turretLeft[key] = value

    def setTurretRotationRight(self, key, value):
        self.turretRight[key] = value

    def setGunUp(self, key, value):
        self.gunElevate[key] = value

    def setGunDown(self, key, value):
        self.gunDepress[key] = value

    def changeOccupiedPosition(self, key, value, isTurnedOut, keyIsTurnedOut):
        if isTurnedOut[keyIsTurnedOut] == False:
            self.occupiedPosition[key] = value
        else:
            pass

    def setTurnedOut(self, key, keyOccupiedPosition):
        if self.turnedOut[key] == False and (self.occupiedPosition[keyOccupiedPosition] != 1 and self.occupiedPosition[keyOccupiedPosition] != 2):
            self.turnedOut[key] = True
        else:
            self.turnedOut[key] = False

    def binoculars(self, key, keyOccupiedPosition):
        if self.turnedOut[key] == True and self.occupiedPosition[keyOccupiedPosition] == 0 and self.inBinoculars == False:
            binocularsOutput = GameFunctionLibrary.binoculars(self.inBinoculars, self.lens, 105, 15, self.binocularOverlay)
            self.inBinoculars = binocularsOutput[0]
            self.binocularOverlay = binocularsOutput[1]

        elif self.turnedOut[key] == True and self.occupiedPosition[keyOccupiedPosition] == 0 and self.inBinoculars == True:
            binocularsOutput = GameFunctionLibrary.binoculars(self.inBinoculars, self.lens, 105, 15, self.binocularOverlay)
            self.inBinoculars = binocularsOutput[0]
            self.binocularOverlay = binocularsOutput[1]
        else:
            pass

    def rotateCamera(self, task):
        if self.keyMap["rotateCamera"] and self.lookingEnabled == True:
            props.setCursorHidden(True)
            base.win.requestProperties(props)

            md = self.win.getPointer(0)
            x = md.getX()
            y = md.getY()
            if self.win.movePointer(0, 960, 540):
                self.heading = self.heading - (x - 960) * 0.2
                self.pitch = self.pitch - (y - 540) * 0.2
            if self.pitch < -90:
                self.pitch = -90
            if self.pitch > 90:
                self.pitch = 90
            self.camera.setHpr(self.heading, self.pitch, 0)
            elapsed = task.time - self.last
            if self.last == 0:
                elapsed = 0
            self.last = task.time
            
        if self.keyMap["rotateCamera"] == False:
            props.setCursorHidden(False)
            base.win.requestProperties(props)

        return task.cont

    def lookDownPrimarySight(self, externalSightActivation, keyOccupiedPosition):
        if self.inViewport == False and externalSightActivation == False and self.occupiedPosition[keyOccupiedPosition] == 1:
            self.viewportOverlay = self.gunnerPrimarySight.lookInVisionBlock(self.inViewport, self.viewportOverlay)
            self.inViewport = True
            self.lookingEnabled = False

        elif self.inViewport == True and externalSightActivation == True:
            self.viewportOverlay = self.gunnerPrimarySight.lookInVisionBlock(self.inViewport, self.viewportOverlay)
            self.inViewport = False
            self.lookingEnabled = True
            GameFunctionLibrary.changePosition(self.occupiedPosition, 5, self.turretInteriorSpace, 0.8, 0.2, 0.3, self.positionUIElements, self.gunnerText, self.positionUIElementsActive, self.turnedOut, 'isTurnedOut')

    def turnTurret(self, task):
        if self.turretLeft["turretLeft"] == True and self.occupiedPosition["occupiedPosition"] == 1 and self.inViewport == True:
            for x in self.turretObjects:
                objectHeading = x.getH()
                newHeading = objectHeading + 0.1
                x.setH(newHeading)
            self.tankGun.setPos(self.tankTurret, 0, 1.3, 0)
            for x in self.gunObjects:
                x.setPos(self.tankGun, 0, 0, 0)
            GameFunctionLibrary.updateCameraPosition(self.gunnerPrimarySight.associatedComponent, self.gunnerPrimarySight.camPosX, self.gunnerPrimarySight.camPosY, self.gunnerPrimarySight.camPosZ, newHeading, camera.getP())
            elapsed = task.time - self.last
            if self.last == 0:
                elapsed = 0
            self.last = task.time

        elif self.turretRight["turretRight"] == True and self.occupiedPosition["occupiedPosition"] == 1 and self.inViewport == True:
            for x in self.turretObjects:
                objectHeading = x.getH()
                newHeading = objectHeading - 0.1
                x.setH(newHeading)
            self.tankGun.setPos(self.tankTurret, 0, 1.3, 0)
            for x in self.gunObjects:
                x.setPos(self.tankGun, 0, 0, 0)
            GameFunctionLibrary.updateCameraPosition(self.gunnerPrimarySight.associatedCamComponent, self.gunnerPrimarySight.camPosX, self.gunnerPrimarySight.camPosY, self.gunnerPrimarySight.camPosZ, newHeading, camera.getP())
            elapsed = task.time - self.last
            if self.last == 0:
                elapsed = 0
            self.last = task.time

        return task.cont

    def slewGun(self, task):
        if self.gunElevate["gunUp"] == True and self.occupiedPosition["occupiedPosition"] == 1 and self.inViewport == True:
            for x in self.gunObjects:
                elevation = x.getP()
                newElevation = elevation + 0.05
                if newElevation > 16:
                    newElevation = 16
                x.setP(newElevation)
                GameFunctionLibrary.updateCameraPosition(self.gunnerPrimarySight.associatedComponent, self.gunnerPrimarySight.camPosX, self.gunnerPrimarySight.camPosY, self.gunnerPrimarySight.camPosZ, x.getH(), newElevation)
            elapsed = task.time - self.last
            if self.last == 0:
                elapsed = 0
            self.last = task.time

        if self.gunDepress["gunDown"] == True and self.occupiedPosition["occupiedPosition"] == 1 and self.inViewport == True:
            for x in self.gunObjects:
                depression = x.getP()
                newDepression = depression - 0.05
                if newDepression < -8:
                    newDepression = -8
                x.setP(newDepression)
                GameFunctionLibrary.updateCameraPosition(self.gunnerPrimarySight.associatedComponent, self.gunnerPrimarySight.camPosX, self.gunnerPrimarySight.camPosY, self.gunnerPrimarySight.camPosZ, x.getH(), newDepression)
            elapsed = task.time - self.last
            if self.last == 0:
                elapsed = 0
            self.last = task.time

        return task.cont

    def fireGun(self):
        shell1 = TankClass.Shell_AP_75_Pat40()
        shell1.spawnShell(self.tankGun.getX(), self.tankGun.getY(), self.tankGun.getZ(), self.tankGun.getH(), self.tankGun.getP())


    



app = TankGame()
app.run()



