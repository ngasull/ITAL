'''
Created on 3 janv. 2012

@author: Nicolas Gasull
'''

import pickle
import sys

from common.struct import Dictionnary
from game.PythonndJeu import PythonndJeu
from gui.PythonndITALUi import Ui_PythonndITAL
from gui.AboutDialogUi import Ui_AboutDialog
from gui.CorpusParallelesDialog import CorpusParallelesDialog

from PySide import QtGui

class PythonndITAL(Ui_PythonndITAL):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.dico = Dictionnary()
        self.dicoFileName = None
        
        self.app = QtGui.QApplication(sys.argv)
        self.mainWindow = QtGui.QMainWindow()
        self.setupUi(self.mainWindow)
        
        self.actionDicoOpen.triggered.connect(self.loadDico)
        self.actionDicoNew.triggered.connect(self.newDico)
        self.actionDicoSave.triggered.connect(self.saveDico)
        
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionBiCorpusMonolingue.triggered.connect(self.showCorpusParalleles)
        
        self.startGameButton.clicked.connect(self.showJeu)
        
    def show(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())
        
    def showAbout(self):
        self.about = QtGui.QDialog()
        aboutUi = Ui_AboutDialog()
        aboutUi.setupUi(self.about)
        self.about.show()

    def showCorpusParalleles(self):
        self.corpusParalleles = CorpusParallelesDialog(self)
        
    def showJeu(self):
        self.jeu = PythonndJeu()
        
    def loadDico(self):
        dicFileName, _ = QtGui.QFileDialog.getOpenFileName()
        
        if dicFileName != '':
            self.statusbar.showMessage("Chargement du dictionnaire...")
            with open(dicFileName, 'rb') as dicFile:
                dicoUnpickler = pickle.Unpickler(dicFile)
                self.dico = dicoUnpickler.load()
                self.statusbar.showMessage("Chargement du dictionnaire... Termine.")
                self.dicoFileName = dicFileName

    def newDico(self):
        del self.dico
        self.dico = Dictionnary()
        self.dicoFileName = None
        self.statusbar.showMessage("Nouveau dictionnaire utilise")
        #
                
    def saveDico(self):
        
        # Dialogue seulement si on ne l'a pas encore sauvegarde
        if self.dicoFileName != None:
            dicFileName = self.dicoFileName
        else:
            dicFileName, _ = QtGui.QFileDialog.getSaveFileName()
        
        if dicFileName != '':
            self.statusbar.showMessage("Savegarde du dictionnaire...")
            with open(dicFileName, 'wb') as dicFile:
                dicoPickler = pickle.Pickler(dicFile)
                dicoPickler.dump(self.dico)
                self.statusbar.showMessage("Savegarde du dictionnaire... Terminee")
                self.dicoFileName = dicFileName
        #
        
            
        
        




