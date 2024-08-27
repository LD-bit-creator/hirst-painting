# import colorgram
import turtle as turtle_module
import random


##extract color from picture

# rgb_colors = []
# colors = colorgram.extract("th.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(245, 239, 228), (247, 237, 243), (234, 245, 239), (235, 239, 247), (199, 152, 114), (143, 69, 85), (148, 79, 64), (61, 96, 129), (18, 25, 41), (227, 216, 101), (136, 164, 184), (190, 143, 158), (42, 20, 28), (32, 19, 14), (133, 176, 145), (193, 85, 101), (197, 92, 77), (55, 122, 90), (14, 26, 19), (88, 155, 109), (109, 41, 54), (223, 172, 183), (166, 160, 62), (46, 56, 96), (229, 175, 166), (51, 159, 178), (169, 208, 184), (117, 41, 35), (17, 96, 74), (227, 219, 13)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)






screen = turtle_module.Screen()
screen.exitonclick()