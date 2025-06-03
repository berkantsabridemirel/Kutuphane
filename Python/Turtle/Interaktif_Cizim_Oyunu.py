import turtle

cizim_tahtasi = turtle.Screen()
cizim_tahtasi.bgcolor("#CACA5D")
cizim_tahtasi.title("Python Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def saga_cevir():
    turtle_instance.right(30)
def sola_cevir():
    turtle_instance.left(30)
def ekran_temizleme():
    turtle_instance.clear()
def baslangica_don():
    turtle_instance.home()
def baslangica_donerkencizme():
    turtle_instance.penup()
def baslangica_donerkenciz():
    turtle_instance.pendown()

cizim_tahtasi.listen()
cizim_tahtasi.onkey(fun=turtle_forward, key="space")
cizim_tahtasi.onkey(fun=saga_cevir, key="Down")
cizim_tahtasi.onkey(fun=sola_cevir, key="Up")
cizim_tahtasi.onkey(fun=ekran_temizleme,key="c")
cizim_tahtasi.onkey(fun=baslangica_don, key="a")
cizim_tahtasi.onkey(fun=baslangica_donerkencizme,key="q")
cizim_tahtasi.onkey(fun=baslangica_donerkenciz,key="w")
turtle.mainloop()
