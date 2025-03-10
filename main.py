import ursina, worldGen, classes, camera, os
os.system("pip install ursina")

app = ursina.Ursina(multithreaded=True)
player=classes.Player(app)
playerController=player.player
playerController.enabled=False

class Global_Variables:
    def __init__(self):
        self.players=1
        self.playersInTruck=0

globalVars=Global_Variables()
def start():
    global cam, Health, Stamina,menuButtons,models
    cam=camera.rec(999999999)
    Health=classes.HealthBar()
    Stamina=classes.StaminaBar()
    player.screen='normal'
    menuButtons=classes.PauseMenu(player)
    menuButtons.buttons[1].on_click = lambda: input("escape")
    menuButtons.buttons[0].on_click=quit
    models = worldGen.hub()
    playerController.enabled=True
    playerController.position=(0,1,0)

def load_world():
    global models
    models = worldGen.world()
    player.screen='normal'
    player.world="game"
    ursina.Audio("assets/sounds/hum1.wav", volume=1, loop=True, loops=-1).play()

classes.mainMenu(start,app)


def iterate(models, playerController):
    for modelss in models:
        for h in range(len(modelss)):
            try:
                if ursina.distance_2d((playerController.position[0],playerController.position[2]), (modelss[h].position[0],modelss[h].position[2])) > player.settings["RenderDistance"]:
                    modelss[h].enabled=False
                else:
                    modelss[h].enabled = True
            except:
                pass
def input(key):
    #GETTING IN THE TRUCK
    if key == 'e' and ursina.distance_2d(playerController.position, models[1].position)<=40:
        playerController.enabled=False
        globalVars.playersInTruck+=1

    #SPRINTING
    if key == "shift" or key =="shift hold":
        player.sprinting=True
    elif key == "shift up":
        player.sprinting=False
        playerController.speed = 8

    #Menu
    if key == "escape" and player.screen=="normal":
        ursina.mouse.locked=False
        ursina.mouse.visible=True
        playerController.mouse_sensitivity=(0,0)
        player.screen="menu"
        for i in menuButtons.buttons:
            i.enabled=True
    elif key == "escape" and player.screen=="menu":
        ursina.mouse.locked=True
        ursina.mouse.visible=False
        playerController.mouse_sensitivity=(40,40)
        player.screen="normal"
        for i in menuButtons.buttons:
            i.enabled=False
    
    #recording
    if key == "left mouse down" and player.screen=="normal" and player.cam and player.recording==False:
        cam.start_Recording()
        player.recording=True
    elif key == "left mouse down" and player.screen=="normal" and player.cam and player.recording:
        cam.stop_Recording()
        player.recording=False
    
    #Crouching
    if key == 'c':
        player.toggleCrouch()


def update():
    #TRUCK TESTING AND WORLD LOADING
    if globalVars.playersInTruck == globalVars.players:
        globalVars.playersInTruck = 0
        for model in models:
            ursina.destroy(model)
        load_world()
        playerController.position == (0,0,0)
        playerController.enabled=True
    ##########################################
    ###########CLASS UPDATES##################
    ##########################################
    player.updates()
    if player.screen=="mainMenu":
        return
    if player.world=="game":
        iterate(models, playerController)
    
    
    #########FOV##########
    player.settings["Fov"]=menuButtons.buttons[3].value
    menuButtons.buttons[4].text="Fov: "+str(int(menuButtons.buttons[3].value))
    player.settings["RenderDistance"]=menuButtons.buttons[2].value
    menuButtons.buttons[5].text="Render Distance: "+str(int(menuButtons.buttons[2].value))

    Health.setBar(player.health)
    Stamina.setBar(player.stamina)
app.run()