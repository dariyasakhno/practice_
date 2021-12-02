from PIL import Image, ImageDraw
from tkinter import Tk, PhotoImage, Canvas, NW


def rotate(A, B, C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])


def jarvis_algoritm(data):
    count_points = len(data)
    num_points = list(range(count_points))
    for i in range(1,count_points):
        if data[num_points[i]][0]<data[num_points[0]][0]:
            num_points[i], num_points[0] = num_points[0], num_points[i]
    result = [num_points[0]]
    del num_points[0]
    num_points.append(result[0])
    while True:
        right = 0
        for i in range(1, len(num_points)):
            if rotate(data[result[-1]], data[num_points[right]], data[num_points[i]]) < 0:
                right = i
        if num_points[right] == result[0]:
            break
        else:
            result.append(num_points[right])
            del num_points[right]
    return result


def algoritm (txtname, imagename, size = (960,540)):
    img = Image.new("RGB", size, "white")
    f = open(txtname,"r")
    data = f.read().split("\n")
    for i in range(len(data)-1):
        data[i] = data[i].split(" ")
        data[i][0]=int(data[i][0])
        data[i][1] = int(data[i][1])
        img.putpixel((int(data[i][1]), 540 - int(data[i][0])), (0, 0, 0))
    points = jarvis_algoritm(data[:-1])
    draw = ImageDraw.Draw(img)
    for point in points:
        draw.line([data[points[points.index(point)-1]][1], 540 - int(data[points[points.index(point)-1]][0]),
                   data[point][1], 540 - int(data[point][0])], fill="blue")
    img.save(f"{imagename}.png")
    return size

def program ():
    txt = input("Введіть назву файлу с датасетом. Приклад: Name.txt\n")
    image = input("Введіть назву зображення:\n")
    size = algoritm(txt, image)
    image_input = input("Хочете продивитися фотографію? (Введіть 'Так' щоб відкрити вікно):\n")
    if image_input == "Так":
        windowMain = Tk()
        windowMain.geometry(f'{size[0]}x{size[1]}+50+50')
        ph_im = PhotoImage(file=f'{image}.png')
        canv = Canvas(windowMain, width=size[0], height=size[1])
        canv.create_image(1, 1, anchor=NW, image=ph_im)
        canv.place(x=10, y=10)
        windowMain.mainloop()
    restart = input("Хочете відобразити ще один датасет? (Введіть 'Так' щоб почати заново):\n")
    if restart == "Так":
        program()

program()
