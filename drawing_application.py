import sys
import os
import subprocess
import shutil
import io

from PIL import Image, ImageDraw, ImageOps
import tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('DRAWING')

        self.create_canvas_frame()
        self.create_other_frame()
        self.create_buttons_frame()
        self.create_widget_value()

        self.pack()
        self.canvas_setup()

    def create_canvas_frame(self):
        """
        Create a canvas to draw a shape.
        """
        self.canvas_frame = tkinter.Frame(self, relief="raised", bd=2, bg="blue")
        self.canvas_frame.grid(rowspan=2, row=0)

        self.draw_canvas = tkinter.Canvas(self.canvas_frame, bg="white", width=CANVAS_SIZE[0], height=CANVAS_SIZE[1])
        self.draw_canvas.grid(row=0, column=0, columnspan=4)
        self.draw_canvas.bind('<Button-1>', self.paint_start)
        self.draw_canvas.bind('<B1-Motion>', self.paint_move)
        self.draw_canvas.bind('<ButtonRelease-1>', self.paint_end)
    
    def create_buttons_frame(self):
        """
        Create a button for options when drawing a shape.
        """
        self.buttons_frame = tkinter.Frame(self, relief="raised", bd=2)
        self.buttons_frame.grid(row=0, column=1, sticky="snew")

        self.pen_size_button = tkinter.Button(self.buttons_frame, text='ペンサイズ', command=self.canvas_clear, height=2, width=False)
        self.pen_size_button.pack(fill='x', padx=5, pady=5)



    def create_other_frame(self):
        """
        Create a button for this application.
        """
        self.other_frame = tkinter.Frame(self, relief="raised", bd=2, width=700)
        self.other_frame.grid(row=1, column=1, sticky="snew")

        self.clear_button = tkinter.Button(self.other_frame, text='描画をリセット', command=self.canvas_clear, height=2, width=False)
        self.clear_button.pack(fill='x', padx=5, pady=5)

        self.save_button = tkinter.Button(self.other_frame, text='描画情報を出力', command=self.canvas_save, height=2, width=False)
        self.save_button.pack(fill='x', padx=5, pady=5)
        
        self.exit_button = tkinter.Button(self.other_frame, text='終了', command=root.destroy, height=2, width=False)
        self.exit_button.pack(fill='x', padx=5, pady=5)

    def create_widget_value(self):
        """
        アプリ内で動的に書き換わる変数群
        """
        pass

    def export_directory_dialog(self):
        pass

    def canvas_setup(self):
        self.before_x, self.before_y = None, None
        self.color = 'black'
        self.im = Image.new('RGB', CANVAS_SIZE, 'white')
        self.draw = ImageDraw.Draw(self.im)

    def canvas_clear(self):
        self.draw_canvas.delete(tkinter.ALL)

    def canvas_save(self):
        pass

    def paint_start(self, event):
        self.draw_canvas.create_line(event.x, event.y, event.x, event.y, width=10, fill=self.color, capstyle=tkinter.ROUND, smooth=tkinter.TRUE, splinesteps=36)
        self.draw.line((event.x, event.y, event.x, event.y), fill=self.color, width=5)
        self.old_x = event.x
        self.old_y = event.y

    def paint_move(self, event):
        if self.old_x and self.old_y:
            self.draw_canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=10, fill=self.color, capstyle=tkinter.ROUND, smooth=tkinter.TRUE, splinesteps=36)
            self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=self.color, width=5)
              
        self.old_x, self.old_y = event.x, event.y

    def paint_end(self, event):
        self.draw_canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=10, fill=self.color, capstyle=tkinter.ROUND, smooth=tkinter.TRUE, splinesteps=36)
        self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=self.color, width=5)
        self.old_x, self.old_y = None, None
        


if __name__ == "__main__":
    CANVAS_SIZE = (600, 600)
    root = tkinter.Tk()
    app = Application(master=root)

    app.mainloop()
