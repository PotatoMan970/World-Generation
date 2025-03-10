import ursina
class Image(ursina.Entity):
    def __init__(self,texture=None,pressed=False,color=ursina.color.rgba(0, 0, 0, 0.25),scale=3, position=(0,0),enabled=True,potato=1,**kwargs):
        super().__init__(
            parent=ursina.camera.ui,
            model='quad',
            scale=scale,
            color=color,
            texture = texture,
            position=position,
            enabled=enabled,
            pressed=pressed,
            potato=potato,
            **kwargs)
class Button(ursina.Button):
    def __init__(self, e, sid, pressed=False, **kwargs):
        super().__init__(e, on_click=self.run, **kwargs)
        self.id=sid
        self.pressed=pressed

    def run(self):
        self.pressed=True

class InputBox:
    def __init__(self,parent=ursina.camera.ui, input=True, x=0, y=0, scale=1, text=">", font_size=20,active=True,screen=True,original=False):
        self.text = text
        self.font_size = font_size
        self.position=(x,y,0)
        self.text_position=(x-0.45,0.45-y,-1)
        self.scale=scale
        self.active=active
        self.part_of_ui=True
        self.parent=parent
        if original:
            self.text_render2=ursina.Text('Use the "help" command to find out how to use other commands', part_of_ui=True, position=(x-0.45,0.45-y+0.05,-1), color=ursina.color.white, scale=scale,parent=self.parent)
        if screen:
            self.screen = ursina.Entity(model='quad', original=original, part_of_ui=True, color=ursina.color.rgb(0,0,0), position=self.position,scale=self.scale,parent=self.parent)
        if input:
            self.text_render=ursina.Text(text, part_of_ui=True, position=self.text_position, color=ursina.color.white, scale=scale,parent=self.parent)

    def input(self,key):
        if self.active==True:
            if key == 'backspace':
                self.text = self.text[:-1]
            elif key == 'enter':
                self.active=False
            elif key == 'space':
                self.text += ' '
            else:
                self.text += key
            self.text_render.text=self.text
    
    def destroy(self):
        try:
            ursina.destroy(self.screen)
        except:
            pass
        try:
            ursina.destroy(self.text_render)
        except:
            pass
        try:
            ursina.destroy(self.text_render2)
        except:
            pass