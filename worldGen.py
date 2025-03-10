import ursina,gen
def world():
    width=20
    height=20
    multi=40
    rooms=[[0,0]]
    rooms2=[6]
    ursina.Entity(model='cube', collider="box", scale = (width*multi,1,height*multi), texture="grass", uv_scale=(50,50))
    ursina.Entity(model='cube', color=ursina.color.hex("160E00"), collider="box", scale=(width*multi+(2*width), 20, 1), position=(width, 0, height*multi/2-20))
    ursina.Entity(model='cube', color=ursina.color.hex("160E00"), collider="box", scale=(width*multi+(2*width), 20, 1), position=(-width, 0, -height*multi/2+20))
    ursina.Entity(model='cube', color=ursina.color.hex("160E00"), collider="box", scale=(1, 20, height*multi+(2*height)), position=(-width*multi/2+20, 0, -height))
    ursina.Entity(model='cube', color=ursina.color.hex("160E00"), collider="box", scale=(1, 20, height*multi+(2*height)), position=(width*multi/2-20, 0, height))
    for i2 in rooms:
        gen.checkAvaible(width,height,i2[0], i2[1],rooms,rooms2)
    models=[]
    for i in rooms:
        if rooms2[rooms.index(i)] == 1:
            model = "assets/models/bedRoom.obj"
        elif rooms2[rooms.index(i)] == 2:
            model="assets/models/Hall.obj"
        elif rooms2[rooms.index(i)] == 3:
            model = None
        elif rooms2[rooms.index(i)] == 4:
            model = "assets/models/KitchenObj.obj"
            ursina.Entity(model = "assets/models/Kitchen.obj", color=ursina.color.rgba(0,0,0,0), position=(i[0]*multi-width*height, 0, i[1]*multi-width*height))
        elif rooms2[rooms.index(i)] == 5:
            model = None
        else:
            model = None
        ursina.Entity(model="assets/models/Ceiling.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height))
        models.append([ursina.Entity(model=model, rotation=(0,90*ursina.random.randint(1,4),0), collider="mesh", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height))])
        if rooms2[rooms.index(i)]!=0:
            if rooms2[rooms.index(i)]==2:
                pass
            else:
                models[-1].append(ursina.Entity(model="assets/models/Wall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height+20),collider="mesh"))
                models[-1].append(ursina.Entity(model="assets/models/Wall.obj", position=(i[0]*multi-width*height+20, 0, i[1]*multi-width*height),collider="mesh",rotation=(0,90,0)))
                models[-1].append(ursina.Entity(model="assets/models/Wall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height-20),collider="mesh"))
                models[-1].append(ursina.Entity(model="assets/models/Wall.obj", position=(i[0]*multi-width*height-20, 0, i[1]*multi-width*height),collider="mesh",rotation=(0,90,0)))


                models[-1].append(ursina.Entity(model="assets/models/Door.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height+20),collider=None))
                models[-1].append(ursina.Entity(model="assets/models/Door.obj", position=(i[0]*multi-width*height+20, 0, i[1]*multi-width*height),collider=None,rotation=(0,90,0)))
                models[-1].append(ursina.Entity(model="assets/models/Door.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height-20),collider=None))
                models[-1].append(ursina.Entity(model="assets/models/Door.obj", position=(i[0]*multi-width*height-20, 0, i[1]*multi-width*height),collider=None,rotation=(0,90,0)))
            
            
                models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height+20)))
                models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height+20, 0, i[1]*multi-width*height),rotation=(0,90,0)))
                models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height-20)))
                models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height-20, 0, i[1]*multi-width*height),rotation=(0,90,0)))

        else:
            models[-1].append(ursina.Entity(model="assets/models/fullWall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height+20),collider="mesh"))
            models[-1].append(ursina.Entity(model="assets/models/fullWall.obj", position=(i[0]*multi-width*height+20, 0, i[1]*multi-width*height),collider="mesh",rotation=(0,90,0)))
            models[-1].append(ursina.Entity(model="assets/models/fullWall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height-20),collider="mesh"))
            models[-1].append(ursina.Entity(model="assets/models/fullWall.obj", position=(i[0]*multi-width*height-20, 0, i[1]*multi-width*height),collider="mesh",rotation=(0,90,0)))
            
            
            models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height+20)))
            models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height+20, 0, i[1]*multi-width*height),rotation=(0,90,0)))
            models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height, 0, i[1]*multi-width*height-20)))
            models[-1].append(ursina.Entity(model="assets/models/CandleForWall.obj", position=(i[0]*multi-width*height-20, 0, i[1]*multi-width*height),rotation=(0,90,0)))
    return models
def hub():
    House=ursina.Entity(model="assets/models/SpawnHouse.obj", position=(40,0,20), collider="mesh", scale=1.2)
    Ground=ursina.Entity(model='cube', collider="box", scale = (100,1,100), texture="grass", uv_scale=(50,50))
    sky=ursina.Sky()
    light1=ursina.DirectionalLight(position=(-40,20,-40), strength=10)
    light2=ursina.AmbientLight()
    truck=ursina.Entity(model="assets/models/Truck.obj", position=(-20,0,20))
    models=[House,truck,Ground,sky,light1,light2]
    return models
if __name__ == "__main__":
    a=ursina.Ursina()
    world()
    a.run()