#sqlalchemy Tut project
#https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/


import os
import sys
import ConfigParser

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from getpass import getuser


###
###
###FIGURE OUT HOW TO USE SQLALCHEMY TO CONNECT TO THE PATH CORRECTLY
###
###


def main():
    #retrieve username
    username = getuser()

    #find setting file
    appSettingsFolder = r"C:\\Users\\%s\\AppData\\Local\\FLAM" % username
    appSettingsFile = os.path.join(appSettingsFolder, 'FLAMSettings.ini')

    #retrieve db location
    print "SETTING LOC: %s" % appSettingsFile
    DATABASE_LOCATION = getSetting(appSettingsFile, "Database Path")

    print "DB LOC %s" % DATABASE_LOCATION

    #open sqlite db
    engine = create_engine(DATABASE_LOCATION)
    Base = declarative_base() 
    Base.metadata.create_all(engine)
    print "DONE RUNNING MAIN"



def getSetting(file, setting):
    print "getting setting: %s" % setting
    configReader = ConfigParser.SafeConfigParser()
    configReader.read(file)

    for section_name in configReader.sections():
        for name, value in configReader.items(section_name):
            if setting.lower() == name.lower():
                print "Found %s setting. Value: %s" % (name, value)
                return value
                break
        print "Setting '%s' not found." % setting
                



if __name__ in "dbBase":
    #retrieve username
    username = getuser()

    #find setting file
    appSettingsFolder = r"C:\\Users\\%s\\AppData\\Local\\FLAM" % username
    appSettingsFile = os.path.join(appSettingsFolder, 'FLAMSettings.ini')

    #retrieve db location
    print "SETTING LOC: %s" % appSettingsFile
    DATABASE_LOCATION = getSetting(appSettingsFile, "Database Path")

    print "DB LOC %s" % DATABASE_LOCATION

    #open sqlite db
    engine = create_engine(DATABASE_LOCATION)
    Base = declarative_base() 
    Base.metadata.create_all(engine)
    print "DONE RUNNING MAIN"

class FlamShow(Base):
    ####DB TABLES####
    __tablename__ = 'show'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    path = Column(String(250), nullable=False)
    ####DB TABLES####


    '''
    def __init__(self, name):
        self.name = name
        print "FlamShow: %s  -  init." % self.name
        self.shotList = []
    '''

    #must pass in a session
    def createShot(self, mainSession, tmp):
        #print tmp
        session = mainSession
        new_shot = FlamShot(name=tmp, show=self, show_id=self.getShowID())
        session.add(new_shot)
        session.commit()
        print "Shot - %s - added to show: %s" % (tmp, self.getName())




    '''
    def addToShotList(self, shot):
        self.shotList.append(shot)


    def getShotList(self):
        return self.shotList
    '''

    def getName(self):
        return self.name

    def getShowID(self):
        return self.id


    def __str__(self):
        return self.name


class FlamShot(Base):
    ####DB TABLES####
    __tablename__ = 'shot'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    show_id = Column(Integer, ForeignKey('show.id'))
    show = relationship(FlamShow, backref="shot", cascade="save-update, delete")
    path = Column(String(250), nullable=False)
    ####DB TABLES####


    '''
    def __init__(self, name):
        self.name = name
        print "FlamShot: %s  -  init." % self.name
        self.assetList = []
    '''


    def createAsset(self, name):
        path = os.path.join(self.getShotPath, name)
        tempAsset = FlamShotAsset(name = name, shot_id = self.getShotID(),shot = self.getShotName(), path = path)
        self.addToAssetList(tempAsset)
        return tempAsset


    def addToAssetList(self, shot):
        self.assetList.append(shot)


    def getName(self):
        return self.name

    def getShow_id(self):
        return self.show_id

    def getShotID(self):
        return self.id

    def getShotName(self):
        return self.name

    def getShotPath(self):
        return self.path


    def __str__(self):
        return self.name



class FlamShotAsset(Base):
    ####DB TABLES####
    __tablename__ = 'assets'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    shot_id = Column(Integer, ForeignKey('shot.id'))
    shot = relationship(FlamShot, backref="assets", cascade="save-update, delete")
    path = Column(String(250), nullable=False)
    ####DB TABLES####


    '''
    def __init__(self, name, path):
        self.name = name
        self.path = path
        print "FlamShotAsset: %s  -  init." % self.name
    '''


    def getPath(self):
        return self.path


    def getName(self):
        return self.name


    def __str__(self):
        return self.name




