from tkinter import *


class Dialog:


    def __init__(self,prompt):

        self.string = ""        

        self.root = Tk()
        self.text = Label(self.root,text=prompt)
        self.input = Entry(self.root)

        self.ok = Button(self.root,text="OK",width=10,command=self.quit)
        self.root.bind("<Return>",self.quit)

        self.text.pack(side=TOP,padx=20,pady=20)
        self.input.pack(side=TOP,padx=50,pady=20)
        self.ok.pack(side=BOTTOM,padx=20,pady=20)

        
        self.root.mainloop()


    def quit(self,*other):
        
        self.string = self.input.get()
        if self.string.isdigit():
            self.root.destroy()
        else:
            self.text.config(text="You idiot...")

class Palette:

    def __init__(self):

        self.colors = ["red","darkred","orange","darkorange","yellow","lightyellow","brown","darkgoldenrod","blue","darkblue","green","darkgreen","purple","pink","white","grey","cornsilk3","black"]
        self.items = []
    
    def addElem(self,name,color):

        self.items.append([name,self.colors[color]])
        



class Graphics:

    def __init__(self,width,height,bSize,palList):

        self.grid = []
        self.elems = []

        self.fill = ""

        

        def m1PalClick(event):

            palClicked = self.palette.find_overlapping(event.x,event.y,event.x,event.y)

            if palClicked:
                col = self.palette.itemcget(palClicked[0], "fill")

                self.fill = col

                print(col)

        def m2Click(event):

            clicked = self.canvas.find_overlapping(event.x,event.y,event.x,event.y)
            if clicked:
                self.canvas.itemconfig(clicked[0],fill="grey")

        def m1Click(event):

            clicked = self.canvas.find_overlapping(event.x,event.y,event.x,event.y)
            if clicked:
                self.canvas.itemconfig(clicked[0],fill=self.fill)


        self.root = Tk()
        self.canvas = Canvas(self.root,width=width,height=height,background="darkgrey")
        self.canvas.bind("<Button-1>",m1Click)
        self.canvas.bind("<B3-Motion>",m1Click)
        self.canvas.bind("<B2-Motion>",m2Click)
        self.canvas.pack(side = TOP)
        self.palette = Canvas(self.root,width=width*2,height=50,background="white")
        self.palette.bind("<Button-1>",m1PalClick)
        self.palette.pack(side = BOTTOM)

        row = int(width/bSize)
        col = int(height/bSize)

        for y in range(col):

            for x in range(row):

                xPos = bSize*x
                yPos = bSize*y
                
                self.grid.append(self.canvas.create_rectangle(xPos,yPos,xPos+bSize,yPos+bSize,fill="grey"))

        for c in range(len(palList.items)):

            self.elems.append(self.palette.create_rectangle(c*30,10,c*30+20,10+20,fill=palList.items[c][1]))
                

        #print(self.grid)
        self.root.mainloop()

#Calls Generic Dialog box for user entry

pSize = Dialog("Enter Map Size in px:")

gridSize = int(pSize.string)

recSizes = []

#Finds all divisables based on user size

for x in range(gridSize):
    if x != 0 and x != 800:
        if gridSize%x == 0:
            recSizes.append(x)

#Calls Generic Dialog box for user entry

bSize = Dialog("Enter Cell Size in px:\n!Will be scaled to closet divisable!")

celSize = int(bSize.string)

closest = None

diff = None

#Finds the closest divisable to the users requested cell size

for x in range(len(recSizes)):
    if x == 0:
        closest = recSizes[x]
        diff = abs(celSize - recSizes[x])
    else:
        if abs(celSize - recSizes[x]) < diff:
           diff = abs(celSize - recSizes[x])
           closest = recSizes[x]

#Creates Palette object for storing "Brushes"

palList = Palette()

for x in range(len(palList.colors)):
    palList.addElem("Generic",x)


if len(pSize.string)>0 and len(bSize.string)>0:
    app = Graphics(gridSize,gridSize,closest,palList)