# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewdict_gui.ui'
#
# Created: Wed Mar 19 12:40:11 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DictWindow(object):
    def setupUi(self, DictWindow):
        DictWindow.setObjectName(_fromUtf8("DictWindow"))
        DictWindow.resize(950, 714)
        self.centralwidget = QtGui.QWidget(DictWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.dictviewbb = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.dictviewbb.sizePolicy().hasHeightForWidth())
        self.dictviewbb.setSizePolicy(sizePolicy)
        self.dictviewbb.setMaximumSize(QtCore.QSize(16777215, 50))
        self.dictviewbb.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dictviewbb.setFrameShadow(QtGui.QFrame.Raised)
        self.dictviewbb.setObjectName(_fromUtf8("dictviewbb"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dictviewbb)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.DVnode_var = QtGui.QComboBox(self.dictviewbb)
        self.DVnode_var.setObjectName(_fromUtf8("DVnode_var"))
        self.DVnode_var.addItem(_fromUtf8(""))
        self.DVnode_var.addItem(_fromUtf8(""))
        self.DVnode_var.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.DVnode_var)
        self.DVall = QtGui.QPushButton(self.dictviewbb)
        self.DVall.setObjectName(_fromUtf8("DVall"))
        self.horizontalLayout.addWidget(self.DVall)
        self.DVClose = QtGui.QPushButton(self.dictviewbb)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.DVClose.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DVClose.setFont(font)
        self.DVClose.setObjectName(_fromUtf8("DVClose"))
        self.horizontalLayout.addWidget(self.DVClose)
        self.DVHelp = QtGui.QPushButton(self.dictviewbb)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.DVHelp.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DVHelp.setFont(font)
        self.DVHelp.setObjectName(_fromUtf8("DVHelp"))
        self.horizontalLayout.addWidget(self.DVHelp)
        self.gridLayout.addWidget(self.dictviewbb, 0, 0, 1, 1)
        self.VDframe = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VDframe.sizePolicy().hasHeightForWidth())
        self.VDframe.setSizePolicy(sizePolicy)
        self.VDframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.VDframe.setFrameShadow(QtGui.QFrame.Raised)
        self.VDframe.setObjectName(_fromUtf8("VDframe"))
        self.verticalLayout = QtGui.QVBoxLayout(self.VDframe)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addWidget(self.VDframe, 1, 0, 1, 1)
        DictWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DictWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        DictWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DictWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DictWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DictWindow)
        QtCore.QMetaObject.connectSlotsByName(DictWindow)

    def retranslateUi(self, DictWindow):
        DictWindow.setWindowTitle(QtGui.QApplication.translate("DictWindow", "Dictionary Window", None, QtGui.QApplication.UnicodeUTF8))
        self.DVnode_var.setToolTip(QtGui.QApplication.translate("DictWindow", "modes to display dictionary structure or columns", None, QtGui.QApplication.UnicodeUTF8))
        self.DVnode_var.setItemText(0, QtGui.QApplication.translate("DictWindow", "Show nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.DVnode_var.setItemText(1, QtGui.QApplication.translate("DictWindow", "Show variables", None, QtGui.QApplication.UnicodeUTF8))
        self.DVnode_var.setItemText(2, QtGui.QApplication.translate("DictWindow", "Dict columns", None, QtGui.QApplication.UnicodeUTF8))
        self.DVall.setToolTip(QtGui.QApplication.translate("DictWindow", "show main words for all dictionary columns", None, QtGui.QApplication.UnicodeUTF8))
        self.DVall.setText(QtGui.QApplication.translate("DictWindow", "Show/Hide all words", None, QtGui.QApplication.UnicodeUTF8))
        self.DVClose.setText(QtGui.QApplication.translate("DictWindow", "CLOSE", None, QtGui.QApplication.UnicodeUTF8))
        self.DVHelp.setText(QtGui.QApplication.translate("DictWindow", "HELP", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DictWindow = QtGui.QMainWindow()
    ui = Ui_DictWindow()
    ui.setupUi(DictWindow)
    DictWindow.show()
    sys.exit(app.exec_())

