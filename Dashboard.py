from Window import *
from Constants import *
from tkinter.filedialog import askopenfile 

class Dashboard(Window):
    def __init__(self, root, parent = None):
        super().__init__(root, parent=parent) 
        self.root = root
        self.__initMenu()
        self.__fileContent = Text(self._frame)
        self.__fileContent.insert(INSERT, "CSV File Content")

        self.__fileContent.grid(row=0, padx=34, pady=(MIN_PADDING, 50), sticky="ew")
        self.__calculateButton = Button(self._frame, text="CALCULATE", command=self._calculate)
        self.__calculateButton.grid(row=1, padx=14, pady=(MIN_PADDING, 50), sticky="e")
    
    def __initMenu(self):
        self.__menubar = Menu(self._master)
        self._master.config(menu=self.__menubar)

        fileMenu = Menu(self.__menubar)
        toolsMenu = Menu(self.__menubar)
        indicesMenu = Menu(self.__menubar)

        fileMenu.add_command(label=FILES_OPTION_ONE, command=self.__onOpen)
        fileMenu.add_command(label=FILES_OPTION_TWO, command=self.__onExit)

        toolsMenu.add_command(label=TOOLS_OPTION_ONE, command=self.__conventionalMcs)
        toolsMenu.add_command(label=TOOLS_OPTION_TWO, command=self.__mlAlgorithm)


        indicesSubMenuOne = Menu(indicesMenu)
        indicesSubMenuOne.add_command(label=INDICES_SUB_OPTION_ONE)
        indicesSubMenuOne.add_command(label=INDICES_SUB_OPTION_TWO)

        indicesMenu.add_cascade(label=INDICES_OPTION_ONE, menu=indicesSubMenuOne, underline=0)

        indicesSubMenuTwo = Menu(indicesMenu)
        indicesSubMenuTwo.add_command(label=INDICES_SUB_OPTION_ONE)
        indicesSubMenuTwo.add_command(label=INDICES_SUB_OPTION_TWO)

        indicesMenu.add_cascade(label=INDICES_OPTION_TWO, menu=indicesSubMenuTwo, underline=0)



        self.__menubar.add_cascade(label="File", menu=fileMenu) 
        self.__menubar.add_cascade(label="Tools", menu=toolsMenu) 
        self.__menubar.add_cascade(label="Indices", menu=indicesMenu) 


    def __onExit(self):
        self.root.quit()
    
    def __onOpen(self):
        self.__file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')]) 
        if self.__file is not None: 
            content = self.__file.read() 
            self.__fileContent.delete('1.0', END)

            self.__fileContent.insert(INSERT, content)

            print(content) 

    def __conventionalMcs(self):
        print("conventional mcs")
    
    def __mlAlgorithm(self):
        print("ML Algorithm")

    def __hlOne(self, e):
        print("HL-1")

    def __hlTwo(self):
        print("HL-2")

    def __tools(self):
        pass
    def _calculate(self):
        print("calculate")
        pass
