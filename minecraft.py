from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()
player = FirstPersonController()

# Himmel
Sky(texture='sky_sunset')

# Roboter
for i in range(4):
  for j in range(4):
    robot = FrameAnimation3d(
      'assets/robot',
      position=(2*i,0,2*j),
      fps=18,
      scale=0.015,
      color=color.black66
    )

# Schwert
sword = Entity(model='assets/blade', 
               texture='assets/sword', 
               rotation=(30,-40),
               position=(0.6,-0.6), 
               parent=camera.ui, 
               scale=(0.2,0.15))

# Schwert bewegen
def update():
  if held_keys['left mouse']:
    sword.position = (0.6,-0.5)
  elif held_keys['right mouse']:
    sword.position = (0.6,-0.5)
  else:
    sword.position = (0.7,-0.6)
  
# Boden
boxes = []

def random_color():
    red = random.Random().random() * 255
    green = random.Random().random() * 255
    blue = random.Random().random() * 255
    return color.rgb(red, green, blue)

def add_box(position):
    boxes.append(
        Button(
        parent=scene,
        model='cube',
        origin=0.5,
        color=random_color(),
        position=position,
        texture='grass'
      )
    )


for x in range(20):
  for y in range(20):
    add_box( (x, 0, y) )

# ground = Entity(
#   model='plane',
#   texture='grass',
#   collider='mesh',
#   scale=(100,1,100)
# )

# Boxen bauen und abbauen
def input(key):
    for box in boxes:
        if box.hovered:
            if key == "left mouse down":
                add_box(box.position + mouse.normal)
            if key == "right mouse down":
                boxes.remove(box)
                destroy(box)

app.run()
