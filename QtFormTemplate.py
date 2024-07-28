''' User interface for connect some attribute with the selected Arduino pinout
    IMPORTANT: For older versions of Maya 2025, you may want to change the version
    from PySide to Pyside2
'''

from PySide6 import QtCore
from PySide6 import QtWidgets
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui


def mayaMainWindow():
    """
    Return the Maya main window widget as a Python object
    """
    mainWindowPtr = omui.MQtUtil.mainWindow()

    return wrapInstance(int(mainWindowPtr), QtWidgets.QWidget)



class QtForm(QtWidgets.QDialog):
    '''User interface for connect some attribute with the selected Arduino pinout'''

    def __init__(self, parent = mayaMainWindow()):
        super(QtForm, self).__init__(parent)

        self.setWindowTitle("QT Template")
        self.setFixedWidth(220)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.createWidgets()
        self.createLayout()
        self.createConnections()


    def createWidgets(self):
        '''Widgets setup'''

        self.closeBtn = QtWidgets.QPushButton("Close")


    def createLayout(self):
        '''Layout setup'''

        buttonLayout = QtWidgets.QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.closeBtn)

        mainLayout = QtWidgets.QVBoxLayout(self)
        mainLayout.addStretch()
        mainLayout.addLayout(buttonLayout)


    def createConnections(self):
        '''Connections setup'''

        self.closeBtn.clicked.connect(self.close)


    @classmethod
    def showUI(cls):
        '''Shows the UI'''

        try:
            qtTemplateDialog.close() # pylint: disable=E0601
            qtTemplateDialog.deleteLater()

        except NameError:
            pass

        qtTemplateDialog = QtForm()
        qtTemplateDialog.show()

QtForm.showUI()
