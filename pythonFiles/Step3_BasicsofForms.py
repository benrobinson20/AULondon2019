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

#from System.Windows.Forms import *
from System.Windows.Forms import Application, Form, FormWindowState, Screen, Label, PictureBox, PictureBoxSizeMode, AnchorStyles, BorderStyle

from System.Drawing import Icon, Color, Font, Point, Size

#############-------------\-------------#############
#INPUTS HERE:

run = IN[0]
message = IN[1]
listInput =tuple(IN[2])     #Combo box requires tuple not list input
url = IN[3]
logoFile = IN[4] 
icon = IN[5]

userOutputDefaultStr = "No selection made, Re-run, and select an item from the dropdown menu" #set default output values for the GUI, that assume form has not run. 

# create a instance of the form class called DropDownform.
#In Winforms, any window or a dialog is a Form. 
class DropDownForm(Form):       

    def __init__(self):     #the __init__ method inside a class is its constructor

        self.Text = "AU London"      #text that appears in the GUI titlebar
        self.Icon = Icon.FromHandle(icon.GetHicon()) #takes a bitmap image and converts to a file that can be used as a Icon for the titlebar
        self.BackColor = Color.FromArgb(255, 255, 255) 
        
        self.WindowState = FormWindowState.Normal # set maximised minimised or normal size GUI
        self.CenterToScreen()   # centres GUI to the middle of your screen 
        self.BringToFront()     #brings the GUI to the front of all opens windows.
        self.Topmost = True    # true to display the GUI infront of any other active forms

        screenSize = Screen.GetWorkingArea(self)  #get the size of the computers main screen, as the form will scale differently to different sized screens
        self.Width = screenSize.Width / 4  #set the size of the form based on the size of the users screen. this helps to ensure consistant look across different res screens.
        self.Height = screenSize.Height / 4
        uiWidth = self.DisplayRectangle.Width    #get the size of the form to use to scale form elements
        uiHeight = self.DisplayRectangle.Height
    
        #self.FormBorderStyle = FormBorderStyle.FixedDialog      # fixed dialog stops the user from adjusting the form size. Recomended disabling this when testing to see if elements are in the wrong place.

        self.userOutput = userOutputDefaultStr  #create a container to store the output from the form
        self.runNextOutput =  False  #set these default values


#############-------------\-------------#############
        spacing = 10    #spacing size for GUI elements to form a consistent border
       
        # creates the text box for a info message
        userMessage = Label()   #label displays texts
        font = Font("Helvetica ", 10)
        userMessage.Text = message
        userMessage.Font = font
        userMessage.Location = Point(spacing, spacing)  #all location require a point object from system.Drawing to set the location.
        userMessage.Size = Size(uiWidth-(spacing*2),(uiHeight/4))   #size the control with the width of the GUI to ensure it scales with different screen
        self.Controls.Add(userMessage)       #this adds control element to the GUI

#############-------------\-------------#############
        

#############-------------\-------------#############


ddForm = DropDownForm()

if run:     #if input is true run the application.
    Application.Run(ddForm)






    
    