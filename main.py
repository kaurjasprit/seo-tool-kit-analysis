import tkinter as tk
import cnt_script as sW
import key_script as kW
import text_script as tW
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("600x400+30+30")

        tk.Button(self, text = "Count Tags", command = self.new_tags).pack()
        tk.Button(self, text="Count keywords",command=self.new_keys).pack()
        tk.Button(self, text="Count text",command=self.new_text).pack()
        
        self._second_window = None
        self._third_window=None
        self._text_window=None
        
        

    def new_tags(self):
        # This prevents multiple clicks opening multiple windows
        if self._second_window is not None:
            return

        self._second_window = sW.SubWindow(self)
   
    def new_keys(self):
        # This prevents multiple clicks opening multiple windows
        if self._third_window is not None:
            return

        self._third_window = kW.SubWindow(self)
    def new_text(self):
        # This prevents multiple clicks opening multiple windows
        if self._text_window is not None:
            return

        self._text_window = tW.SubWindow(self)

    def close(self):
        # Destory the 2nd window and reset the value to None
        if self._second_window is not None:
            self._second_window.destroy()
            self._second_window = None
    def close_key(self):
        # Destory the 2nd window and reset the value to None
        if self._third_window is not None:
           self._third_window.destroy()
           self._third_window = None       
    def close_text(self):
        # Destory the 2nd window and reset the value to None
        if self._text_window is not None:
           self._text_window.destroy()
           self._text_window = None  


if __name__ == '__main__':
    window = MainWindow()
    window.mainloop()