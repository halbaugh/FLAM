#FlamGUI.py
#Created By: Hunter Albaugh


import sys
from PySide import QtGui
from PySide import QtCore

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



        status = self.statusBar().setStyleSheet("statusBar" + self.appStyle)

        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background-color: rgb(60, 60, 60);
                color: rgb(255,255,255);
                border: 1px solid #000;
            }

            QMenuBar::item {
                background-color: rgb(60, 60, 60);
                color: rgb(255,255,255);
            }

            QMenuBar::item::selected {
                background-color: rgb(100, 100, 100);
            }

            QMenu {
                background-color: rgb(60, 60, 60);
                color: rgb(255,255,255);
                border: 1px solid #000;           
            }

            QMenu::item::selected {

                background-color: rgb(100, 100, 100);
            }
            """)


        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openProjectAction)
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


    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure to quit?", 
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, 
                                            QtGui.QMessageBox.Yes)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    
        

class FLAMWidget(QtGui.QWidget):

    def __init__(self, parent):
        super(FLAMWidget, self).__init__(parent)
        self.__layout()


    def __layout(self):

        #project info  #asset preview
                #asset browser

        #self.test_button = QtGui.QPushButton("Click me")
        

        self.asset_viewer_frame = QtGui.QFrame(self)
        self.asset_viewer_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.asset_viewer_frame.setFrameStyle(QtGui.QFrame.Sunken)
        self.asset_viewer_frame.setStyleSheet("background-color: rgb(50, 50, 50)")

        self.assets_frame = QtGui.QFrame(self)
        self.assets_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        #self.assets_frame.setFrameStyle(QtGui.QFrame.Sunken)
        self.assets_frame.setStyleSheet("background-color: rgb(50, 50, 50)")

        self.rootVbox = QtGui.QVBoxLayout()
        self.topBox = QtGui.QHBoxLayout()
        self.bottomBox = QtGui.QHBoxLayout()

        self.infoPane = ProjectInfoFrame()

        self.topBox.addWidget(self.infoPane)
        self.topBox.addWidget(self.asset_viewer_frame)
        self.bottomBox.addWidget(self.assets_frame)

        #self.rootVbox.addStretch(1)
        self.rootVbox.addLayout(self.topBox)
        self.rootVbox.addLayout(self.bottomBox)

        self.setLayout(self.rootVbox)


class ProjectInfoFrame(QtGui.QFrame):
    def __init__(self, parent = None):
        super(ProjectInfoFrame, self).__init__(parent)

        self.labelTextColor = "rgb(150, 150, 150)"
        self.InfoTextColor = "rgb(220, 220, 220)"

        self.projectName = "Test Project"
        self.shotName = "SHOT NAYEM"
        self.shotFrameRange = "tRange 1-57"

        self.buildFrame()
        self.buildInfoLabels()
        self.buildLayout()


    def buildFrame(self):
        self.setFrameShape(QtGui.QFrame.StyledPanel)
        self.setFrameStyle(QtGui.QFrame.Sunken)
        self.setMaximumSize(400,180)
        self.setStyleSheet("background-color: rgb(50, 50, 50)")

    def buildInfoLabels(self):
        
        self.pNameLabel = QtGui.QLabel('Project Name:')
        self.pNameLabel.setStyleSheet("QLabel {color: %s ; font: bold 16pt Calibri  }"% self.labelTextColor)

        self.pName = QtGui.QLabel(self.projectName)
        self.pName.setStyleSheet("QLabel {color: %s ; font: 16pt Calibri  }"% self.InfoTextColor)
        
        self.pNameLayout = QtGui.QHBoxLayout()
        self.pNameLayout.addWidget(self.pNameLabel)
        self.pNameLayout.addWidget(self.pName)
        self.pNameLayout.addStretch(0)



        self.sNameLabel = QtGui.QLabel('Shot Name:')
        self.sNameLabel.setStyleSheet("QLabel {color: %s ; font: bold 16pt Calibri  }"% self.labelTextColor)

        self.sName = QtGui.QLabel(self.shotName)
        self.sName.setStyleSheet("QLabel {color: %s ; font: 16pt Calibri  }"% self.InfoTextColor)

        self.sNameLayout = QtGui.QHBoxLayout()
        self.sNameLayout.addWidget(self.sNameLabel)
        self.sNameLayout.addWidget(self.sName)
        self.sNameLayout.addStretch(0) 

        self.sFrameRangeLabel = QtGui.QLabel('Frame Range:')
        self.sFrameRangeLabel.setStyleSheet("QLabel {color: %s ; font: bold 16pt Calibri  }"% self.labelTextColor)

        self.sFrameRange = QtGui.QLabel(self.shotFrameRange)
        self.sFrameRange.setStyleSheet("QLabel {color: %s ; font: 16pt Calibri  }"% self.InfoTextColor)

        self.sFrameRangeLayout = QtGui.QHBoxLayout()
        self.sFrameRangeLayout.addWidget(self.sFrameRangeLabel)
        self.sFrameRangeLayout.addWidget(self.sFrameRange)
        self.sFrameRangeLayout.addStretch(0)

    def buildLayout(self):
        self.shot_info_layout = QtGui.QVBoxLayout()
        self.shot_info_layout.addLayout(self.pNameLayout)
        self.shot_info_layout.addLayout(self.sNameLayout)
        self.shot_info_layout.addLayout(self.sFrameRangeLayout)
        self.shot_info_layout.addStretch(0)
        self.setLayout(self.shot_info_layout) 

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        frame = QtGui.QFrame()
        frame.setFrameStyle(QtGui.QFrame.Panel | QtGui.QFrame.Plain)

        label = QtGui.QLabel('This is random text')

        #dockWidget = QtGui.QDockWidget('Stuff', self)
        # set the widget to non-movable, non-floatable and non-closable
        #dockWidget.setFeatures(dockWidget.NoDockWidgetFeatures)
        #dockWidget.setWidget(label)

        # add the QDockWidget to the QLayout
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(label)

        # set the layout of the QFrame
        frame.setLayout(hbox)

        # create another QLayout to add QFrame
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(frame)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Test')



def main():
    
    app = QtGui.QApplication(sys.argv)
    #flam = Example()
    flam = FlamGui()
    flam.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()