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
        self.scene = self.loader.loadModel("/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/basicscene.egg")

        self.scene.reparentTo(self.render)

        self.scene.setScale(3, 3, 3)
        self.scene.setPos(0, 0, 0)

        #make ground model twosided
        self.scene.set_two_sided(True)

        base.disableMouse()

        #loading environment texture
        envTexture = loader.loadTexture("/c/Panda3D-1.9.2/MyProjects/TankGame/Assets/envskin.png")

        self.scene.setTexture(envTexture)

        commanderText = {'textPos': 0.1, 'posString': "Commander"}
        gunnerText = {'textPos': 0.15, 'posString': "Gunner"}
        loaderText = {'textPos': 0.2, 'posString': "Loader"}
        driverText = {'textPos': 0.25, 'posString': "Driver"}

        positionUIElements = [commanderText, gunnerText, loaderText, driverText]

        self.positionUIElementsActive = []

        lens = self.cam.node().getLens()

        global props
        props = WindowProperties()

        GameFunctionLibrary.configureCamera(lens, 105, 0.1, 3000)

        base.messenger.toggleVerbose()

        self.keyMap = {"rotateCamera": 0}

        self.occupiedPosition = {"occupiedPosition": 0}



        #load models and texture (FOR EXTERIOR)
        tankHull = GameFunctionLibrary.loadVehicleComponent(hullData[0] , hullData[1], tankHullLoader, None, 0, 0, 0)

        tankHull.setPos(0,0,1)

        tankTurret = GameFunctionLibrary.loadVehicleComponent(turretData[0], turretData[1], tankTurretLoader, tankHull, 0, 0, 0)

        tankGun = GameFunctionLibrary.loadVehicleComponent(gunData[0], gunData[1], tankGunLoader, tankTurret, 0, 0, 0)

        #load models and texture (FOR INTERIOR)
        turretInteriorSpace = GameFunctionLibrary.loadVehicleComponent(turretInteriorData[0], turretInteriorData[1], interiorTurretLoader, tankTurret, 0, 0, 0)

        hullInteriorSpace = GameFunctionLibrary.loadVehicleComponent(hullInteriorData[0], hullInteriorData[1], interiorHullLoader, tankHull, 0, 0, 0)

        breech = GameFunctionLibrary.loadVehicleComponent(breechAssemblyData[0], breechAssemblyData[1], breechAssemblyLoader, turretInteriorSpace, 0, 0, 0)

        breechBar1 = GameFunctionLibrary.loadVehicleComponent(breechBar1Data[0], breechBar1Data[1], breechBar1Loader, turretInteriorSpace, 0, 0, 0)

        breechBar2 = GameFunctionLibrary.loadVehicleComponent(breechBar2Data[0], breechBar2Data[1], breechBar2Loader, turretInteriorSpace, 0, 0, 0)

        breechMesh = GameFunctionLibrary.loadVehicleComponent(breechMeshData[0], breechMeshData[1], breechMeshLoader, turretInteriorSpace, 0, 0, 0)

        gunnerPrimarySight = GameFunctionLibrary.loadVehicleComponent(gunnerPrimarySightData[0], gunnerPrimarySightData[1], gunnerPrimarySightLoader, turretInteriorSpace, 0, 0, 0)

        gunnerSecondarySight = GameFunctionLibrary.loadVehicleComponent(gunnerSecondarySightData[0], gunnerSecondarySightData[1], gunnerSecondarySightLoader, turretInteriorSpace, 0, 0, 0)

        turretPowerTraverse = GameFunctionLibrary.loadVehicleComponent(turretPowerTraverseData[0], turretPowerTraverseData[1], gunnerSecondarySightLoader, turretInteriorSpace, 0, 0, 0)

        turretSeats = GameFunctionLibrary.loadVehicleComponent(turretSeatsData[0], turretSeatsData[1], gunnerSecondarySightLoader, turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockFront = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockFrontData[0], commanderVisionBlockFrontData[1], gunnerSecondarySightLoader, turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockLeft = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockLeftData[0], commanderVisionBlockLeftData[1], gunnerSecondarySightLoader, turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockRight = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockRightData[0], commanderVisionBlockRightData[1], gunnerSecondarySightLoader, turretInteriorSpace, 0, 0, 0)

        commanderVisionBlockRear = GameFunctionLibrary.loadVehicleComponent(commanderVisionBlockBackData[0], commanderVisionBlockBackData[1], gunnerSecondarySightLoader, turretInteriorSpace, 0, 0, 0)


        driverSeat = GameFunctionLibrary.loadVehicleComponent(driverSeatData[0], driverSeatData[1], driverSeatLoader, hullInteriorSpace, 0, 0, 0)

        driverVisionBlock = GameFunctionLibrary.loadVehicleComponent(driverVisionBlockData[0], driverVisionBlockData[1], driverVisionBlockLoader, hullInteriorSpace, 0, 0, 0)

        driverRightPedal = GameFunctionLibrary.loadVehicleComponent(driverPedal1Data[0], driverPedal1Data[1], driverPedal1Loader, hullInteriorSpace, 0, 0, 0)

        driverLeftPedal = GameFunctionLibrary.loadVehicleComponent(driverPedal2Data[0], driverPedal2Data[1], driverPedal1Loader, hullInteriorSpace, 0, 0, 0)

        driverLeftSteeringBar = GameFunctionLibrary.loadVehicleComponent(driverLeftBarData[0], driverLeftBarData[1], driverLeftBarLoader, hullInteriorSpace, 0, 0, 0)

        driverRightSteeringBar = GameFunctionLibrary.loadVehicleComponent(driverRightBarData[0], driverRightBarData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)

        driverControlPanel = GameFunctionLibrary.loadVehicleComponent(driverControlPanelData[0], driverControlPanelData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)

        ignitionSwitch = GameFunctionLibrary.loadVehicleComponent(driverIgnitionSwitchData[0], driverIgnitionSwitchData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)

        auxPowerSwitch = GameFunctionLibrary.loadVehicleComponent(driverAuxPowerSwitchData[0], driverAuxPowerSwitchData[1], driverRightBarLoader, hullInteriorSpace, 0, 0, 0)


        #setting position and scale of tank
        turretInteriorSpace.set_two_sided(True)
        hullInteriorSpace.set_two_sided(True)
        breechMesh.set_two_sided(True)

        #setting beginning camera position
        camera.setPos(turretInteriorSpace, 0, 0, 3)
        camera.setHpr(turretInteriorSpace, 0, 0, 0)

        commanderPosition = TankClass.crewPosition(0, turretInteriorSpace, 0.6, -0.5, 3.2)
        gunnerPosition = TankClass.crewPosition(1, turretInteriorSpace, 0.8, 0.4, 2.9)
        loaderPosition = TankClass.crewPosition(2, turretInteriorSpace, -0.45, -0.3, 2.9)
        driverPosition = TankClass.crewPosition(3, hullInteriorSpace, -0.85, 1.94, 1.9)

        GameFunctionLibrary.changePosition(self.occupiedPosition, 0, commanderPosition.associatedComponent, commanderPosition.camPosX, commanderPosition.camPosY, commanderPosition.camPosZ, positionUIElements, commanderText, self.positionUIElementsActive)

        self.accept("1",GameFunctionLibrary.changePosition, [self.occupiedPosition, 0, commanderPosition.associatedComponent, commanderPosition.camPosX, commanderPosition.camPosY, commanderPosition.camPosZ, positionUIElements, commanderText, self.positionUIElementsActive])
        self.accept("1-up", self.changeOccupiedPosition, ["occupiedPosition", 0])

        self.accept("2",GameFunctionLibrary.changePosition, [self.occupiedPosition, 1, gunnerPosition.associatedComponent, gunnerPosition.camPosX, gunnerPosition.camPosY, gunnerPosition.camPosZ, positionUIElements, gunnerText, self.positionUIElementsActive])
        self.accept("2-up", self.changeOccupiedPosition, ["occupiedPosition", 1])

        self.accept("3",GameFunctionLibrary.changePosition, [self.occupiedPosition, 2, loaderPosition.associatedComponent, loaderPosition.camPosX, loaderPosition.camPosY, loaderPosition.camPosZ, positionUIElements, loaderText, self.positionUIElementsActive])
        self.accept("3-up", self.changeOccupiedPosition, ["occupiedPosition", 2])

        self.accept("4",GameFunctionLibrary.changePosition, [self.occupiedPosition, 3, driverPosition.associatedComponent, driverPosition.camPosX, driverPosition.camPosY, driverPosition.camPosZ, positionUIElements, driverText, self.positionUIElementsActive])
        self.accept("4-up", self.changeOccupiedPosition, ["occupiedPosition", 3])


        def appendItemToList(item, list):
            for i in list:
                list.append(item)

                return list


        self.accept("mouse3", self.setKey, ["rotateCamera", True])
        self.accept("mouse3-up", self.setKey, ["rotateCamera", False])

        taskMgr.add(self.rotateCamera, "rotateCameraTask")

        self.heading = 180
        self.pitch = 0
        self.mousex = 0
        self.mousey = 0
        self.last = 0
        self.mousebtn = [0, 0, 0]

        global pickingEnabled
        pickingEnabled = False
        global screenHint
        screenHint = 0

        def collideEventIn(entry):
            global pickingEnabled

            np_from=entry.getFromNodePath()
            np_into=entry.getIntoNodePath()
            np_into.getParent().setColor(.6, 0.5, 1.0, 1)
            pickingEnabled=True

        def collideEventOut(entry):
            global pickingEnabled

            pickingEnabled=False

            np_into=entry.getIntoNodePath()
            np_into.getParent().setColor(1.0, 1.0, 1.0, 1)


        def rayupdate(task):
            if base.mouseWatcherNode.hasMouse():
                mpos=base.mouseWatcherNode.getMouse()
                pickerRay.setFromLens(base.camNode, mpos.getX(),mpos.getY())
            return task.cont

        def mousePick(status):
            if pickingEnabled:
                if status == 'down':
                    gunnerPrimarySight.setScale(.9)
                
                if status == 'up':
                    gunnerPrimarySight.setScale(2)

        base.cTrav = CollisionTraverser()
        collisionHandler = CollisionHandlerEvent()

        pickerNode=CollisionNode('mouseraycnode')
        pickerNP=base.camera.attachNewNode(pickerNode)
        pickerRay=CollisionRay()
        pickerNode.addSolid(pickerRay)
        base.cTrav.addCollider(pickerNP, collisionHandler)

        gunnerPrimarySightCollider = gunnerPrimarySight.attachNewNode(CollisionNode('gunnerPrimarySightcnode'))
        gunnerPrimarySightCollider.node().addSolid(CollisionSphere(-1.155, 0.9, 2.55, 0.1))

        gunnerPrimarySightCollider.show()

        collisionHandler.addInPattern('%fn-into-%in')
        collisionHandler.addOutPattern('%fn-out-%in')

        DO=DirectObject()

        DO.accept('mouseraycnode-into-gunnerPrimarySightcnode', collideEventIn)
        DO.accept('mouseraycnode-out-gunnerPrimarySightcnode', collideEventOut)

        DO.accept('mouse1', mousePick, ['down'])
        DO.accept('mouse1-up', mousePick, ['up'])

        taskMgr.add(rayupdate, "updatePicker")

    def setKey(self, key, value):
        self.keyMap[key] = value

    def changeOccupiedPosition(self, key, value):
        self.occupiedPosition[key] = value

    def rotateCamera(self, task):
        if self.keyMap["rotateCamera"]:
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




app = TankGame()
app.run()



