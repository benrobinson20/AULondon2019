#############-------------\-------------#############
#My Default Boiler Plate
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPIUI')
from  Autodesk.Revit.UI import Selection

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference('RevitNodes')
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import *

import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)

import math
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application

#############-------------\-------------#############
#UI additional references
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Label

from System.Windows.Drawing import Icon, Color, Font, Point, Size
#############-------------\-------------#############
#INPUTS HERE:

run = IN[0]
message = IN[1]
listInput =tuple(IN[2])     #Combo box requires tuple not list input
url = IN[3]
logoFile = IN[4] 
icon = IN[5]


# create a instance of the form class called DropDownform.
#In WinDrawing, any window or a dialog is a Form. 
class DropDownForm(Form):       
    
    def __init__(self):     #the __init__ method inside a class is its constructor

        self.Text = "AU London"      #text that appears in the GUI titlebar
        self.Icon = Icon.FromHandle(icon.GetHicon())
        self.BackColor = Color.FromArgb(255,255,255)

        self.WindowState = FormWindowState.Normal
        self.CenterToScreen()
        self.BringToFront()
        self.TopMost = True 

        screenSize = Screen.GetWorkingArea(self)
        self.Width = screenSize /4 
        self.Height = screenSize / 4

        uiWidth = self.DisplayRectangle.Width  
        uiHeight = self.DisplayRectangle.Height

        spacing = 10

        userMessage = Label()
        font = Font("Helvetica", 10 )
        userMessage.Text = message
        userMessage.Font = font
        userMessage.Location = Point(spacing,spacing)
        userMessage.Size = Size(uiWidth -(spacing*2), (uiHeight/4))
        self.Controls.Add(userMessage)





ddForm = DropDownForm()

if run:     #if input is true run the application.
    Application.Run(ddForm)