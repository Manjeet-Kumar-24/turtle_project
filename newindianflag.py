import turtle

flag = turtle.Turtle()

flag.speed(5)
flag.pensize(5)
flag.color('#000080')
 
def draw(x, y):
     flag.penup()
     flag.goto(x,y)
     flag.pendown()

     for i in range(24):
         flag.forward(80)
         flag.backward(80)
         flag.left(15)
     #flag.backward(80)

     #draw(0, -80)
     flag.goto(-100,20)
     flag.circle(80, 360)    
     flag.goto(-460,20)
     flag.begin_fill()
     flag.color('#138808')
     flag.forward(720)
     flag.right(90)
     flag.forward(160)
     flag.right(90)
     flag.forward(720)
     flag.right(90)
     flag.forward(160)
     flag.end_fill()
     flag.color('#FFFFFF')
     flag.goto(-460,180)
     flag.color('#FF9933')
     #draw(-350,80)

     flag.begin_fill()
     flag.color('#FF9933')
     flag.right(90)
     flag.forward(720)
     flag.left(90)
     flag.forward(160)
     flag.left(90)
     flag.forward(720)
     flag.left(90)
     flag.forward(160)

     flag.end_fill()

     turtle.done()


# def main():
#     print("Hello World!")

if __name__ == "__main__":
    # main() 
    draw(-100,100)










                





