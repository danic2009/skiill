import simple_draw as sd

sd.resolution = (1200, 600)
point = sd.get_point(300, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)
