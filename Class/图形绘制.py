import turtle
'''
turtle.screensize(1024,768)
turtle.write('Hellow天朝', font=('华文琥珀', 80, 'normal'))
turtle.showturtle()
turtle.circle(200, steps=3)

turtle.done()
'''

# 重置
turtle.reset()

# 图像填充
turtle.screensize(3024, 2768)
# 画笔粗细
turtle.pensize(15)
turtle.begin_fill()
turtle.showturtle()
turtle.circle(100, steps=6)
turtle.color('blue')
turtle.end_fill()
# 隐藏箭头
turtle.hideturtle()
turtle.done()


