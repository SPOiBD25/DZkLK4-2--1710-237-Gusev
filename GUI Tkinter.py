import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x400+50+50')
        self.title("User Profile GUI Tkinter")
        self.setUpMainWindow()

    def createImageLabels(self):
        images = ["images/skyblue.png", "images/p.png"]
        for image in images:
            try:
                img = Image.open(image)
                tk_img = ImageTk.PhotoImage(img)
                label = tk.Label(self, image=tk_img)
                label.image = tk_img
                if image == 'images/p.png':
                    label.place(x=80, y=20)
                else:
                    label.place(x=0, y=0)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self):
        self.createImageLabels()

        arial_20 = font.Font(family='Arial', size=20)
        arial_17 = font.Font(family='Arial', size=17)
        arial_10 = font.Font(family='Arial', size=10)

        user_label = tk.Label(self, text='Никита Гусев', font=arial_20)
        user_label.place(x=85, y=140)

        bio_label = tk.Label(self, text='Биография', font=arial_17)
        bio_label.place(x=15, y=170)

        about_label = tk.Label(self, text='Я студент 2-го курса БВО МАИ/Инноватика', wraplength=200)
        about_label.place(x=15, y=190)

        skills_label = tk.Label(self, text='Умения', font=arial_17)
        skills_label.place(x=15, y=240)

        languages_label = tk.Label(self, text="Python | SQL")
        languages_label.place(x=15, y=260)

        experience_label = tk.Label(self, text="Опыт работы", font=arial_17)
        experience_label.place(x=15, y=290)

        developer_label = tk.Label(self, text="Python Developer")
        developer_label.place(x=15, y=310)

        dev_dates_label = tk.Label(self, text="May 2022 - Present", font=arial_10)
        dev_dates_label.place(x=15, y=330)

        driver_label = tk.Label(self, text="Самокат")
        driver_label.place(x=15, y=350)

        driver_dates_label = tk.Label(self, text="Jun 2025 - Aug 2025", font=arial_10)
        driver_dates_label.place(x=15, y=370)

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()





