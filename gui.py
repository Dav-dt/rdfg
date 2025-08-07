import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd
import tkinter.messagebox as msgb

from guiUtils import *
from path import *
from file import * 

class App(tk.Tk):
    """
    Main class.
    """
    def __init__(self):
        super().__init__()

        self.title(GuiUtils.title)
        self.geometry(GuiUtils.size)
        self.configure(bg=GuiUtils.bg)
        self.iconbitmap("icon.ico")

        #Widgets
        self.mainFrame = tk.Frame(self, bg=GuiUtils.bg, padx=20, pady=20)
        self.mainFrame.pack(expand=True)


        self.titleLabel = tk.Label(self.mainFrame, 
                                   text=GuiUtils.title, 
                                   bg=GuiUtils.bg,
                                   fg=GuiUtils.fg,
                                   font=GuiUtils.fontTitle)
        self.titleLabel.pack(pady=(0, 20))


        self.pathFrame = tk.Frame(self.mainFrame, bg=GuiUtils.widgetsBg, pady=10)
        self.pathFrame.pack(fill="x", pady=5)

        self.pathLabel = tk.Label(self.pathFrame, text="Output Path:",
                                  bg=GuiUtils.widgetsBg,
                                  fg=GuiUtils.fg,
                                  font=GuiUtils.font)
        self.pathLabel.pack(side=tk.LEFT, padx=5)

        self.pathEntry = tk.Entry(self.pathFrame,
                                  bg=GuiUtils.widgetsBg,
                                  fg=GuiUtils.fg,
                                  font=GuiUtils.font,
                                  width=20)
        self.pathEntry.pack(side=tk.LEFT, padx=5)
        self.pathEntry.insert(0, getDefaultOutputPath())

        self.browseButton = tk.Button(self.pathFrame, text="Browse",
                                      bg=GuiUtils.widgetsBg,
                                      fg=GuiUtils.fg,
                                      font=GuiUtils.font,
                                      command=self.setOutputPath)
        self.browseButton.pack(side=tk.LEFT, padx=5)


        self.randomFilesFrame = tk.Frame(self.mainFrame, bg=GuiUtils.widgetsBg, pady=10)
        self.randomFilesFrame.pack(fill="x", pady=5)

        self.rdFilesLabel = tk.Label(self.randomFilesFrame, text="Number of Random Files:",
                                     bg=GuiUtils.widgetsBg,
                                     fg=GuiUtils.fg,
                                     font=GuiUtils.font)
        self.rdFilesLabel.pack(side=tk.LEFT, padx=5)

        self.rdFilesEntry = tk.Entry(self.randomFilesFrame,
                                     bg=GuiUtils.widgetsBg,
                                     fg=GuiUtils.fg,
                                     font=GuiUtils.font,
                                     width=10)
        self.rdFilesEntry.pack(side=tk.LEFT, padx=5)


        self.sizeFilesFrame = tk.Frame(self.mainFrame, bg=GuiUtils.widgetsBg, pady=10)
        self.sizeFilesFrame.pack(fill="x", pady=5)

        self.sizeFilesLabel = tk.Label(self.sizeFilesFrame, text="Size of each File:",
                                       bg=GuiUtils.widgetsBg,
                                       fg=GuiUtils.fg,
                                       font=GuiUtils.font)
        self.sizeFilesLabel.pack(side=tk.LEFT, padx=5)

        self.sizeFilesEntry = tk.Entry(self.sizeFilesFrame,
                                       bg=GuiUtils.widgetsBg,
                                       fg=GuiUtils.fg,
                                       font=GuiUtils.font,
                                       width=10)
        self.sizeFilesEntry.pack(side=tk.LEFT, padx=5)

        self.sizeFilesChose = ttk.Combobox(self.sizeFilesFrame,
                                           font=GuiUtils.font,
                                           values=GuiUtils.fileSize,
                                           width=10)
        self.sizeFilesChose.pack(side=tk.LEFT, padx=5)
        self.sizeFilesChose.current(2)

        self.generateButton = tk.Button(self.mainFrame, text="Generate Files",
                                        bg=GuiUtils.widgetsBg,
                                        fg=GuiUtils.fg,
                                        font=GuiUtils.font,
                                        padx=10, pady=5,
                                        command=self.mainGeneration)
        self.generateButton.pack(pady=(20, 0))


    def setOutputPath(self) -> None:
        """
        File Dialog to select the target Path.
        """
        file = fd.askdirectory()
        self.pathEntry.delete(0,tk.END)
        self.pathEntry.insert(0, file)

        return None


    def mainGeneration(self) -> None:
        """
        Main function for generating
        """
        filePath = self.pathEntry.get()
        number = self.rdFilesEntry.get()
        size = self.sizeFilesEntry.get()
        extension = self.sizeFilesChose.get()
        if not number or not size:
            msgb.showwarning(message="You must select valid attributes!")
            return None

        handler = FileHandler(int(number), int(size), extension, filePath)

        handler.generateAllFiles()
        del handler
        msgb.showinfo(message="Files generated successfully!")

        return None