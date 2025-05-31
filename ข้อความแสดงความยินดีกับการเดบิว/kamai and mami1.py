from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


def page1():
    labels["1"].place(relx=0.5, rely=0.5, anchor="center")
    labels["2"].place_forget()
    labels["3"].place_forget()
def page2():
    labels["1"].place_forget()
    labels["2"].place(relx=0.5, rely=0.5, anchor="center")
    labels["3"].place_forget()
def page3():
    labels["1"].place_forget()
    labels["2"].place_forget()
    labels["3"].place(relx=0.5, rely=0.5, anchor="center")

window = tk.Tk()
window.geometry("1000x1000")
background_image = Image.open("debut kamai and mami.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


func = {
    "1": page1,
    "2": page2,
    "3": page3,
}

buttons = {
    "1": tk.Button(window, text="หน้าแรก",font=("Arial",20), command=func["1"]),
    "2": tk.Button(window, text="ถึงพี่มามิ",font=("Arial",20), command=func["2"]),
    "3": tk.Button(window, text="ถึงพี่คาไม",font=("Arial",20), command=func["3"]),
}

labels = {
    "1": tk.Label(window, text="ข้อแสดงความยินดีด้วยกับการเดบิวของพี่คาไมและพี่มามิครับ\n Picture Cr : MamiMumei",font=("Arial",30)),
    "2": tk.Label(window, text="ผมนั้นรู้สึกว่าพี่มามินั้นเก่งมากๆ ทำให้ผมนั้นได้แรงบันดาลใจในเรื่องความพยายามในเรื่องการอ่าหนังสือและการสอบเข้า\n "
                               "ผมจึงพยายามเตรียมตัวสอบเข้ามหาลัยเพื่อให้ตัวเองได้เป็น gamedev จริงๆผมอยากสอบทุนมงแต่ไม่ได้ภาษาอังกฤษ แต่อยากไปเรียนต่อญี่ปุ่นแต่ขอไปตอนเรียนโท"
                               "\nเรื่องที่จะบอกเพียงเท่านี้ แล้วเจอกันในงานmeetingครั้งถัดๆไปะครับ"
                               "\nจะติดตามผลงานเรื่อยๆจากนี้และตลอดไปขอบคุณครับ\nปล.ถ้าอ่านแล้วงงๆเกิดจากการที่ผมลบบางส่วนแล้วแก้ใหม่",font=("Arial",20)),
    "3": tk.Label(window, text="ผมอยากจะบอกพี่คาไมว่าพี่เก่งมากๆ ผมอยากเก่งให้ได้สักครึ่งของพี่เลยในการเขียนโค้ดและการทำตามความฝัน และก็ชอบตอนที่พี่เล่าเรื่องต่างๆทั้งญี่ปุ่น และ เรื่องIT "
                               "\nตอนนี้ผมก็กำลังทำตามฝันตัวเองเช่นกันครับ ในการสอบเข้ามหาลัยคณะวิศวะคอม "
                               "\nผมต้องขอบอกว่าตอนทำสิ่งนี้ผมมีเวลาน้อยมากๆจึงทำให้ไม่ได้ทำเอง100%  เพราะดูตามยูทูป หาโค้ดจากเน็ต "
                               "\n และก็ให้ chat gptช่วยอีกนิด แก้ไปแก้มาจนได้ในรูปแบบที่พอใจแถมยังอาจจะไม่สวยมากแต่ถ้าผมพัฒนาแล้วจะเอามาส่งใหม่ครับ"
                               "\nตอนที่และพบปัญหาแล้วแก้ได้ผมรู้สึกดีใจมากครับที่ได้ลองกลับมาเขียนโค้ดอีกครั้ง \nมีเรื่องที่จะบอกเพียงเท่านี้แล้วเจอกันในงานmeetingครั้งถัดๆไปะครับ"
                               "\nจะติดตามผลงานเรื่อยๆจากนี้และตลอดไปขอบคุณครับ \nปล.ถ้าอ่านแล้วงงๆเกิดจากการที่ผมลบบางส่วนแล้วแก้ใหม่",font=("Arial",20)),

}

buttons["1"].pack()
buttons["2"].pack()
buttons["3"].pack()
labels["1"].place(relx=0.5, rely=0.5, anchor="center")


window.mainloop()