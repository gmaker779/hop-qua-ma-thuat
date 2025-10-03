from guizero import Picture, App, Text

cuaso = App(title="Thiệp chúc mừng", width=1920, height=1024, bg="lightgray")
chu = Text(cuaso, "Chúc mừng sinh nhật", size=16, color = 'black')
hinhanh = Picture(cuaso, image="birthday.png")
chu = Text(cuaso, "Từ: Thăng", size=16)

cuaso.display()