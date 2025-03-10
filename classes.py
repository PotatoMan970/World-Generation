import ursina
from ursina.prefabs.first_person_controller import FirstPersonController
import UI
class Player:
    def __init__(self,main=True):
        self.invitory =[0,0,0,0,0,0,0,0]
        self.cam=False
        self.stamina=100
        self.health=100
        self.maxHealth=100
        self.recording=False
        self.maxStamina=100
        self.sprinting=False
        self.screen="mainMenu"
        self.playing=False
        self.world="home"
        self.settings={"RenderDistance":100, "Fov":90}
        if main:
            player = FirstPersonController(model='cube', z=-10, color=ursina.color.rgba(1, 0, 0, 0), speed=8, position=(0,0.1,0))
            #v
            self.player=player
            #self.playerBox=playerbox
        else:
            playerbox=ursina.Entity(model='cube', collider='box', scale = (1,2,1), visible=True)
            self.playerBox=playerbox

    def sprint(self):
        if self.stamina > 0:
            if self.player.height==2:
                self.player.speed = 20
                self.stamina-=0.353
            if self.player.height==1:
                self.player.speed = 10
                self.stamina-=0.353

    def toggleCrouch(self):
        if self.player.height==2:
            self.player.height=1
            self.player.speed=4
            ursina.camera.position = ursina.camera.position - (0,1,0)
        elif self.player.height==1:
            self.player.height=2
            self.player.speed=8
            ursina.camera.position = ursina.camera.position + (0,1,0)

    def updates(self):
        if self.stamina <0:
            self.stamina=0
            self.sprinting=False
            self.player.speed=8
        if self.stamina <self.maxStamina:
            self.stamina+=0.15
        #ursina.camera.clip_plane_far=100
        ursina.camera.fov=self.settings["Fov"]
        if self.sprinting:
           self.sprint()
        if self.player.Y < -30:
            self.player.set_position((0,30,0))
    def addToInv(self, itemNum):
        if self.cam:
            return False
        for i in self.invitory:
            if i == 0:
                self.invitory[self.invitory.index(i)]=itemNum
                break

class HealthBar:
    def __init__(self):
        self.healthBar1=UI.Image(color=ursina.color.rgba(0,0,0,1), scale=(0.025,0.5), position=(0.86,0,0))
        self.healthBar=UI.Image(color=ursina.color.rgba(1,0,0,1), scale=(0.025,0.5), position=(0.86,0,-1))
    def setBar(self, ammount):
        self.healthBar.scale=(0.025,ammount/200)
        self.healthBar.position=(0.86,(ammount/40/100/0.05/10+(0.2*((ammount-100)/100))-0.05))

class StaminaBar:
    def __init__(self):
        self.staminaBar1=UI.Image(color=ursina.color.rgba(0,0,0,1), scale=(0.025,0.5), position=(0.83,0,0))
        self.staminaBar=UI.Image(color=ursina.color.rgba(0,0,1,1), scale=(0.025,0.5), position=(0.83,0,-1))
    def setBar(self, ammount):
        self.staminaBar.scale=(0.025,ammount/200)
        self.staminaBar.position=(0.83,(ammount/40/100/0.05/10+(0.2*((ammount-100)/100))-0.05))

class PauseMenu:
    def __init__(self,player):
        QUIT=ursina.Button("QUIT GAME", potato=1, scale=0.05, scale_x=0.25, text_position=(-0.35,-0.47,-2),position=(-0.35,-0.47,-1),enabled=False)
        CONTINUE=ursina.Button("CONTINUE",  potato=1,scale=0.05, scale_x=0.25, position=(0.35,-0.47,-1), enabled=False)
        RENDERDISTANCE = ursina.Slider(potato=1,min=100, max=1000, value=player.settings["RenderDistance"], position=(0, 0,-1), scale=(0.5,0.5), enabled=False, default=100)
        FOV = ursina.Slider(potato=1,min=10, max=100, value=player.settings["Fov"], position=(-0.35, 0), scale=(0.5,0.5), enabled=False)
        FOVTEXT=ursina.Text("FOV: "+str(int(player.settings["Fov"])), potato=1,position=(-0.35,-0.05,-1), color= ursina.color.black, enabled=False)
        RENDERDISTANCETEXT=ursina.Text("Render Distance: "+str(int(player.settings["RenderDistance"])), potato=1,position=(0,-0.05,-1), color= ursina.color.black, enabled=False)
        pauseScreen=[UI.Image(potato=1,position=(0,0,0)), UI.Image(potato=1,color=ursina.color.rgb(255,255,255),scale=1, position=(0,0,1))]
        pauseScreen[0].enabled=False
        pauseScreen[1].enabled=False
        self.buttons=[QUIT,CONTINUE,RENDERDISTANCE,FOV,FOVTEXT,RENDERDISTANCETEXT, pauseScreen[0], pauseScreen[1]]

class mainMenu:
    def __init__(self, start,app):
        self.start=ursina.Button("Start", on_click=self.startGame,scale=.25, position=(.5,0))
        self.quit=ursina.Button("Quit", on_click=quit, scale=.25, position=(-.5,0))
        self.startfunc=start
        self.items=[self.start, self.quit]
        self.app=app

    def startGame(self):
        for item in self.items:
            ursina.destroy(item)
        self.startfunc()