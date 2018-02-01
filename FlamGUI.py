#FlamGUI.py
#Created By: Hunter Albaugh
#git yiiisss


import sys
from PySide import QtGui
from PySide import QtCore

import QTCSS as css

import dbQueries as db
from dbQueries import DATABASE_LOCATION

print "FlamGui - DBLOC - %s" % DATABASE_LOCATION


#MAIN GUI WINDOW
class FlamGui(QtGui.QMainWindow):
    def __init__(self, parent = None):
        super(FlamGui, self).__init__(parent)

        self.appStyle = '{background-color: rgb(60, 60, 60);}'
        self.setStyleSheet("QMainWindow" + self.appStyle)
        self.initUI()
        

        

    def initUI(self):
        ###File/Exit
        exitAction = QtGui.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        ###File/Open
        openProjectAction = QtGui.QAction('&Open project', self)
        openProjectAction.setShortcut('Ctrl+O')
        openProjectAction.setStatusTip('Open a project...')
        openProjectAction.triggered.connect(self.openProject)

        ###File/Test Function 
        testFunctionAction = QtGui.QAction('&Test Function', self)
        testFunctionAction.setShortcut('Ctrl+T')
        testFunctionAction.setStatusTip('Test Function...')
        testFunctionAction.triggered.connect(self.testFunc)



        status = self.statusBar().setStyleSheet("statusBar" + self.appStyle)

        menubar = self.menuBar()

        menubar.setStyleSheet(css.menubarCSS)




        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openProjectAction)
        fileMenu.addAction(testFunctionAction)
        fileMenu.addAction(exitAction)

        self.resize(1200, 700)
        self.center()
        
        self.setWindowTitle('Freelance Asset Manager')
        self.setWindowIcon(QtGui.QIcon('icons/flam_icon.png'))
        

        self.addMainGui()

    def addMainGui(self):
        self.flam_widget = FLAMWidget(self)
        _widget = QtGui.QWidget()
        _layout = QtGui.QVBoxLayout(_widget)
        _layout.addWidget(self.flam_widget)
        self.setCentralWidget(_widget)
 

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def openProject(self):



        QtGui.QMessageBox.question(self, 'Placeholder',
            "This is a placeholder button.", QtGui.QMessageBox.Ok )


    #Used to test anything.......
    def testFunc(self):
        ###HOW DO I GET RID OF THIS MONSTER EFFICIENTLY?!?!?
        ###
        self.flam_widget.infoPane.projectNameLabel.setContent("Pine Apple Express: 7")
        ###
        ###

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", 
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, 
                                            QtGui.QMessageBox.Yes)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    
        
#LAYOUTS FOR WINDOW
class FLAMWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(FLAMWidget, self).__init__(parent)
        self.__layout()


    def __layout(self):

        #project info  #asset preview
                #asset browser

        #self.test_button = QtGui.QPushButton("Click me")
        
        #Top Left Show Selection Panel
        self.showSelectionPane = ShowSelectionPanel()

        #Top Left Pane
        self.infoPane = ProjectInfoFrame()


        #Top Right Pane
        self.assetFrame = AssetViewerFrame()
        


        #Bottom Pane
        self.assets_frame = QtGui.QFrame(self)
        self.assets_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.assets_frame.setStyleSheet("background-color: rgb(50, 50, 50)")
        self.assets_frame.setFrameStyle(QtGui.QFrame.Sunken)

        #Creating Layouts
        self.rootVbox = QtGui.QVBoxLayout()
        self.topBox = QtGui.QHBoxLayout()
        self.bottomBox = QtGui.QHBoxLayout()
        self.splitterLayout = QtGui.QVBoxLayout()

        #splitter testing -- HORIZONTAL
        self.splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.splitter1.addWidget(self.showSelectionPane)
        self.splitter1.addWidget(self.infoPane)
        self.splitter1.addWidget(self.assetFrame)
        self.splitter1.setStretchFactor(1,10)
        
        #self.splitter1.setSizes([1000,200])

        #splitter testing -- VERTICAL
        self.splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.splitter2.addWidget(self.splitter1)
        self.splitter2.addWidget(self.assets_frame)
        self.splitter2.setStretchFactor(1,10)
        self.splitter2.setStyleSheet(css.splitterCSS)

        self.splitterLayout.addWidget(self.splitter2)

        #Adding widgets to layouts
        self.topBox.addWidget(self.infoPane)
        self.topBox.addWidget(self.assetFrame)
        self.bottomBox.addWidget(self.assets_frame)

        #self.rootVbox.addStretch(1)
        self.rootVbox.addLayout(self.topBox)
        self.rootVbox.addLayout(self.bottomBox)

        self.setLayout(self.splitterLayout)


class AssetViewerFrame(QtGui.QFrame):
    def __init__(self, parent = None):
        super(AssetViewerFrame, self).__init__(parent)

        ###
        ###TEMP HARD CODED
        self.tempImage = QtGui.QPixmap("icons/temp.png")
        self.tempImage = self.tempImage.scaled(250, 250, QtCore.Qt.KeepAspectRatio) 
        ###
        ###FRAME STILL NEEDS TO BE RESIZED SO ITS NOT HUGE

        self.buildFrame()
        self.buildContent()
        self.buildLayout()


    def buildFrame(self):
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameStyle(QtGui.QFrame.Sunken)
        #self.setMaximumSize(400,180)
        self.setStyleSheet("background-color: rgb(53, 50, 50)")

    def buildContent(self):
        self.imgLabel = QtGui.QLabel(self)
        self.imgLabel.setPixmap(self.tempImage)


    def buildLayout(self):
        self.asset_info_layout = QtGui.QVBoxLayout()
        self.asset_info_layout.addStretch(0)
        self.asset_info_layout.addWidget(self.imgLabel)
        self.setLayout(self.asset_info_layout)


class AssetBrowserFrame(QtGui.QFrame):
    def __init__(self, parent = None):
        super(AssetBrowserFrame, self).__init__(parent)

        ###
        ###TEMP HARD CODED
        ###

        self.buildFrame()
        self.buildContent()
        self.buildLayout()


    def buildFrame(self):   
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameStyle(QtGui.QFrame.Sunken)
        self.setStyleSheet("background-color: rgb(50, 50, 50)")

    def buildContent(self):
        self.imgLabel = QtGui.QLabel(self)
        self.imgLabel.setPixmap(self.tempImage)


    def buildLayout(self):
        self.asset_info_layout = QtGui.QVBoxLayout()
        self.asset_info_layout.addStretch(0)
        self.asset_info_layout.addWidget(self.imgLabel)
        self.setLayout(self.asset_info_layout)


class ProjectInfoFrame(QtGui.QFrame):
    def __init__(self, parent = None):
        super(ProjectInfoFrame, self).__init__(parent)

        ###
        ###TEMP HARD CODED
        self.labelTextColor = "rgb(150, 150, 150)"
        self.infoTextColor = "rgb(220, 220, 220)"

        self.projectName = "Terminator 20 Billion"
        self.shotName = "Serious Test Shot"
        self.shotFrameRange = "1-57"
        ###
        ###

        self.buildFrame()
        self.buildInfoLabels()
        self.buildLayout()


    def buildFrame(self):
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameStyle(QtGui.QFrame.Sunken)
        #self.setMaximumSize(400,180)
        self.setStyleSheet("background-color: rgb(50, 50, 50)")

    #Would it be faster to edit instead of rebuild? Might be worth making all of this easily accessable.
    def buildInfoLabels(self):

        self.projectNameLabel = ProjectInfoLabel('Project Name:', self.projectName, self.labelTextColor, self.infoTextColor)
        self.shotNameLabel = ProjectInfoLabel('Shot Name:', self.shotName, self.labelTextColor, self.infoTextColor)
        self.shotFrameRangeLabel = ProjectInfoLabel('Frame Range:', self.shotFrameRange, self.labelTextColor, self.infoTextColor)


    def buildLayout(self):
        self.shot_info_layout = QtGui.QVBoxLayout()
        self.shot_info_layout.addLayout(self.projectNameLabel)
        self.shot_info_layout.addLayout(self.shotNameLabel)
        self.shot_info_layout.addLayout(self.shotFrameRangeLabel)
        self.shot_info_layout.addStretch(0)
        self.setLayout(self.shot_info_layout)

class ShowSelectionPanel(QtGui.QFrame):
    def __init__(self, parent = None):
        super(ShowSelectionPanel, self).__init__(parent)

        ###
        ###TEMP HARD CODED
        self.labelTextColor = "rgb(150, 150, 150)"
        self.infoTextColor = "rgb(220, 220, 220)"

        self.projectName = "Terminator 20 Billion"
        self.shotName = "Serious Test Shot"
        self.shotFrameRange = "1-57"
        ###
        ###

        self.buildFrame()
        self.buildComboBoxes()
        self.buildLayout()


    def buildFrame(self):
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameStyle(QtGui.QFrame.Sunken)
        #self.setMaximumSize(400,180)
        self.setStyleSheet("background-color: rgb(50, 50, 50)")

    #Would it be faster to edit instead of rebuild? Might be worth making all of this easily accessable.
    def buildComboBoxes(self):

        ####PROJECT LIST COMBO BOX
        #print "INIT SHOW COMBO BOXES."
        showList = db.getAllShows()
        
        self.projectCombo = QtGui.QComboBox(self)
        for s in showList:
            self.projectCombo.addItem(s.getName())
        self.projectCombo.setStyleSheet(css.showComboBoxCSS)

        #NOT THE BEST WAY TO DO THIS
        #WILL HAVE TO ELIMINATE THE POSSIBILITY OF DUPLICATES
        curShowName = self.projectCombo.currentText()
        curShowId = db.getShow(curShowName).getShowID()
        curShotList = db.getAllShots(curShowId)
    
        ####SHOT LIST FOR CURRENT PROJECT
        self.shotCombo = QtGui.QComboBox(self)

        if curShotList:
            for s in curShotList:
                self.shotCombo.addItem(s.getName())
        self.shotCombo.setStyleSheet(css.showComboBoxCSS)

        #print "FINISHED COMBO BOX INIT."




    def buildLayout(self):
        self.shot_info_layout = QtGui.QVBoxLayout()
        self.shot_info_layout.addWidget(self.projectCombo)
        self.shot_info_layout.addWidget(self.shotCombo)
        self.shot_info_layout.addStretch(0)
        self.setLayout(self.shot_info_layout)


class ProjectInfoLabel(QtGui.QHBoxLayout):
    def __init__(self, title, content, titleColor, contentColor):
        super(ProjectInfoLabel, self).__init__()
        self.titleColor = titleColor
        self.contentColor = contentColor
        self.title = title
        self.content = content

        self.initLabel()

    def initLabel(self):
        #Creating title label
        self.titleLabel = QtGui.QLabel(self.title)
        self.titleLabel.setStyleSheet("QLabel {color: %s ; font: bold 16pt Calibri  }" % self.titleColor)

        #Creating content label
        self.contentLabel = QtGui.QLabel(self.content)
        self.contentLabel.setStyleSheet("QLabel {color: %s ; font: 16pt Calibri  }" % self.contentColor)

        #Adding to self.layout
        self.addWidget(self.titleLabel)
        self.addWidget(self.contentLabel)
        self.addStretch(0)


    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        if not self.title == newTitle:
            self.title = newTitle
            self.updateGui()

    def getContent(self):
        return self.content

    def setContent(self, newContent):
        if not self.content == newContent:
            self.content = newContent
            self.updateGui()

    def updateGui(self):
        self.titleLabel.setText(self.title)
        self.contentLabel.setText(self.content)



def main():
    
    app = QtGui.QApplication(sys.argv)
    #flam = Example()
    flam = FlamGui()
    flam.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()