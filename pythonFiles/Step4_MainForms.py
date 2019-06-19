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

import webbrowser

#from System.Windows.Forms import *
from System.Windows.Forms import Application, Form, FormWindowState, Screen, Label, PictureBox, PictureBoxSizeMode, AnchorStyles, BorderStyle, ComboBox, ComboBoxStyle
from System.Windows.Forms import Button
from System.Drawing import Icon, Color, Font, Point, Size

import System.IO
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
        #logo file
        logo =PictureBox()
        logo.Image = logoFile 
        ratio =  float(logo.Height)/ float(logo.Width)  #needs to be a float as int will round to the nearest whole number
        logo.Size = Size(uiWidth/4, (uiHeight/4)*ratio) #scale the image by the ratio between the images height & width
        logo.Location = Point(spacing, (uiHeight- logo.Height)-spacing)
        logo.SizeMode = PictureBoxSizeMode.Zoom     # zooms the image to fit the extent
        logo.Anchor = (AnchorStyles.Bottom | AnchorStyles.Left)      #anchor styles lock elements to a given corner of the GUI if you allow users change size
        self.Controls.Add(logo) 
        #logo.BorderStyle = BorderStyle.Fixed3D    #gives a border to the panel to test its location

#############-------------\-------------#############

        #combox drop down
        cBox = ComboBox()   #dropdown control form
        cBox.Location = Point(spacing,uiHeight/3)       
        cBox.Width = uiWidth -(spacing*2)
        cBox.Items.AddRange(listInput)    # Adds an array of items to the list of items for a ComboBox.
        cBox.DropDownStyle = ComboBoxStyle.DropDownList     #setting to dropdown list prevents users from being able to add aditional text values
        cBox.SelectedIndexChanged += self.dropDownOutput  #.Click+= registers the press of the button to register the event handler and determine what action takes place when button clicked
        self.Controls.Add(cBox)   

#############-------------\-------------#############

        #Create ok button
        btnOk = Button()    #create a button control
        btnOk.Text = "Next"
        btnOk.Location = Point(uiWidth - ((btnOk.Width * 2) + spacing ), uiHeight - (btnOk.Height + spacing ))
        btnOk.Anchor = (AnchorStyles.Bottom | AnchorStyles.Right)
        btnOk.Click += self.okButtonPressed    #Register the event on the button bress to trigger the def okButtonPressed
        self.Controls.Add(btnOk)
    
        #Create Cancel Button
        btnCancel = Button()
        #btnCancel.Parent = self
        btnCancel.Text = "Cancel"
        btnCancel.Location = Point(uiWidth - (btnOk.Width + spacing), uiHeight - (btnOk.Height + spacing ))
        btnCancel.Anchor = (AnchorStyles.Bottom | AnchorStyles.Right)
        btnCancel.Click += self.CnlButtonPressed
        self.Controls.Add(btnCancel)      


#############-------------\---------------------------------------------------------------------------------------#############
        #when a user selects a item in the drop down the dropDownOutput method is called.
    def dropDownOutput(self, sender, args):     #self is the instance of the GUI form. Sender is the control/widget. args is the argument/event provided from the control
        self.userOutput = sender.SelectedItem   #output the selected item.
    
    def okButtonPressed(self, sender, args):
        self.Close()    #trigger to close the GUI when button is pressed
        self.runNextOutput = True #if the ok button is pressed set runNextOutput as True

    def CnlButtonPressed(self, sender, args):
        self.Close()
        self.runNextOutput = False #if the ok button is pressed set runNextOutput as False
   


ddForm = DropDownForm()

if run:     #if input is true run the application.
    Application.Run(ddForm)
    
    if ddForm.userOutput == userOutputDefaultStr:       #if the user does not select a item So the userOutput value is still the default text
        results = ddForm.userOutput, False      #output the default string and runNextOutput
    else:
        results = ddForm.userOutput, ddForm.runNextOutput       #else if someone has selected a item output it and the runNextOutput

    OUT = results