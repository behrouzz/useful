from glob import glob
import tkinter as tk
from PIL import Image, ImageTk



class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.image_files = [i for i in glob('*.*') if (i[-3:]=='png' or i[-3:]=='jpg')]
        self.List_images = [ImageTk.PhotoImage(Image.open(i)) for i in self.image_files]
        self.main_window()


    def main_window(self):
        
        self.n = 0
        self.n_max = len(self.List_images) - 1
        self.title("Image Viewer | " + self.image_files[self.n])
        self.update()

        self.bind('<Escape>', self.close)
        self.bind('<Right>', self.next)
        self.bind('<Left>', self.back)
        
        self.label = tk.Label(self, image=self.List_images[self.n])
        self.label.grid(row=0, column=0)#, columnspan=3)


    def next(self, e):
        if not self.last:
            self.n += 1
            self.draw()


    def back(self, e):
        if not self.first:
            self.n -= 1
            self.draw()


    def update(self):
        if self.n_max == 0:
            self.first = True
            self.last = True
        elif self.n == 0:
            self.first = True
            self.last = False
        elif self.n == self.n_max:
            self.first = False
            self.last = True
        else:
            self.first = False
            self.last = False


    def draw(self):
        self.title("Image Viewer | " + self.image_files[self.n])
        self.label.grid_forget()
        self.update()
        self.label = tk.Label(self, image=self.List_images[self.n])
        self.label.grid(row=0, column=0)#, columnspan=5)


    def close(self, e):
        self.destroy()



if __name__ == "__main__":
    app = App()
    app.mainloop()

