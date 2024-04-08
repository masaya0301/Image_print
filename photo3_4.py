import tkinter as tk
from PIL import Image, ImageTk
import random
import os
import time
import threading
import csv

# ルートウィンドウを作成
root = tk.Tk()
root.title("画像表示")
x=0
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
data= list(range(10))
file_name = "BD.csv"
a = 900

def write_to_csv():
    try:
        # CSVファイルを書き込みモードで開く
        with open(file_name, mode='a', newline='', encoding='utf-8') as file:
            # CSVファイルのwriterオブジェクトを作成
            writer = csv.writer(file)

            # データをCSVファイルに書き込む
            writer.writerow(data)

        print("データがCSVファイルに書き込まれました。")
    except Exception as e:
        print("エラーが発生しました:", e)



def btn1_click():
    global x
    global photo1,photo2,photo3,photo4,photo5,photo6,photo7,photo8
    global photo8
    i = 0
    # 画像フォルダのパス
    image_folder_path = "gazou"
    random_folder_path = "yuma"

    # 画像ファイルのリストを作成
    image_files = os.listdir(image_folder_path)
    random_files = os.listdir(random_folder_path)
    # 画像ファイルをランダムに7つ選択
    random_images = random.sample(random_files, 7)
    random_images.append("yuma.png")
    random_images = random.sample(random_images,8)
    print(random_images)
    white = Image.open("white.png")
    #1つめを表示
    image_path = os.path.join(image_folder_path, random_images[0])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo1 = ImageTk.PhotoImage(image)
    canvas.create_image(a-388,30,image=photo1, anchor=tk.NW)
    print(random_images[0])
    #2つめを表示
    image_path = os.path.join(image_folder_path, random_images[1])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo2 = ImageTk.PhotoImage(image)
    canvas.create_image(a-112,30,image=photo2, anchor=tk.NW)
    print(random_images[1])
    #3つめを表示
    image_path = os.path.join(image_folder_path, random_images[2])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo3 = ImageTk.PhotoImage(image)
    canvas.create_image(a+162,30,image=photo3, anchor=tk.NW)
    print(random_images[2])
    #4つめを表示
    image_path = os.path.join(image_folder_path, random_images[3])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo4 = ImageTk.PhotoImage(image)
    canvas.create_image(162+a,360,image=photo4, anchor=tk.NW)
    print(random_images[3])
    #5つめを表示
    image_path = os.path.join(image_folder_path, random_images[4])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo5 = ImageTk.PhotoImage(image)
    canvas.create_image(162+a,690,image=photo5, anchor=tk.NW)
    print(random_images[4])
    #6つめを表示
    image_path = os.path.join(image_folder_path, random_images[5])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo6 = ImageTk.PhotoImage(image)
    canvas.create_image(a-112,690,image=photo6, anchor=tk.NW)
    print(random_images[5])

    #7つめを表示
    image_path = os.path.join(image_folder_path, random_images[6])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo7 = ImageTk.PhotoImage(image)
    canvas.create_image(a-388,690,image=photo7, anchor=tk.NW)
    print(random_images[6])

    #8つめを表示
    image_path = os.path.join(image_folder_path, random_images[7])
    image = Image.open(image_path)
    image = image.resize((225, 300)) # 画像のリサイズ
    photo8 = ImageTk.PhotoImage(image)
    canvas.create_image(a-388,360,image=photo8, anchor=tk.NW)
    print(random_images[7])
    for i in range(0,8):
        if random_images[i] == "yuma.png":
            data[x] = i+1
    label =tk.Label(canvas,text=x+1,font=("Helvetica",14))
    label.place(x=screen_width-100,y=screen_height/2+100)
    x= x+1
    print(data)
    return

def btn2_click():
    global photo_w
    image = Image.open("white.png")
    image = image.resize((225, 300)) # 画像のリサイズ
    photo_w = ImageTk.PhotoImage(image)
    canvas.create_image(a-388,30,image=photo_w, anchor=tk.NW)
    canvas.create_image(a-112,30,image=photo_w, anchor=tk.NW)
    canvas.create_image(162+a,30,image=photo_w, anchor=tk.NW)
    canvas.create_image(a-388,360,image=photo_w, anchor=tk.NW)
    canvas.create_image(a-388,690,image=photo_w, anchor=tk.NW)
    canvas.create_image(a-112,690,image=photo_w, anchor=tk.NW)
    canvas.create_image(162+a,360,image=photo_w, anchor=tk.NW)
    canvas.create_image(162+a,690,image=photo_w, anchor=tk.NW)
    if x == 10:
        write_to_csv()

def btn3_click():
    timer1_event()

def timer1_event():
    btn1_click()  # 関数を呼び出す
    # ここで次のタイマーイベントを設定する
    # 例えば、5秒後に再度関数を呼び出す場合:
    threading.Timer(5,btn2_click).start()
    timer = threading.Timer(7, timer1_event)
    timer.start()

canvas = tk.Canvas(root,width=1920, height=1080)

canvas.pack()
print(screen_height)
print(screen_width)
#赤い丸を表示
id = canvas.create_oval(880,490, 921, 531, activefill = "red" ,fill = "red",outline = "red" )
#ボタンを作成
button1 =tk.Button(canvas,text ="Run",width=10,height=5,bg ="red",activebackground="blue",command=btn3_click)
button1.place(x=screen_width-100,y=screen_height/2-200)
root.mainloop()










