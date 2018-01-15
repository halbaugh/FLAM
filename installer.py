import ConfigParser
import os

import tkMessageBox
from Tkinter import Tk
from tkFileDialog import askdirectory


########################
testing = True
########################




def unifiySlash(slashPath):
    return slashPath.replace("/", os.sep)


class FlamInstall(object):
    def __init__(self):
        self.settingsPath = ""
        self.installDir = ""
        self.config = ConfigParser.RawConfigParser()

    def setInstallDirectory(self):
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        tkMessageBox.showinfo("FLAM Install","Please select a directory to install FLAM to...")    
        self.installDir = unifiySlash(askdirectory(initialdir = "Z:\Code\FLAManager")) # show an "Open" dialog box and return the path to the selected file
        
        self.settingsPath = os.path.join(self.installDir,'FLAMSettings.ini')
        print "Install Dir: %s" % self.installDir




    def makeSettings(self):
        ###
        ###Creates FLAMSettings.ini based off of colected path if it does not exist
        ###
        if os.path.isfile(self.settingsPath):
            print "Settings file has already been created. --> %s" % self.settingsPath
            
        else:
            print "Creating FLAMSettings.ini at %s" % self.settingsPath

            # When adding sections or items, add them in the reverse order of
            # how you want them to be displayed in the actual file.
            # In addition, please note that using RawConfigParser's and the raw
            # mode of ConfigParser's respective set functions, you can assign
            # non-string values to keys internally, but will receive an error
            # when attempting to write to a file or when you get it in non-raw
            # mode. SafeConfigParser does not allow such assignments to take place.
            self.config.add_section('Location')
            self.config.set('Location', 'Server Path', '')
            self.config.set('Location', 'Local Path', '')
            self.config.set('Location', 'Settings', self.settingsPath)

            # Writing our configuration file to 'example.cfg'
            with open(self.settingsPath, 'wb') as configfile:
                self.config.write(configfile)




if __name__ == '__main__':
    print "\n\n"
    if testing:
        install = FlamInstall()
        install.setInstallDirectory()
        install.makeSettings()
