import os
import sys
import platform
from PyQt5.QtCore import (Qt,
                          QFile,
                          QFileInfo,
                          QTimer,
                          QSettings,
                          QVariant, 
                          PYQT_VERSION_STR, 
                          QT_VERSION_STR)
from PyQt5.QtWidgets import (QMainWindow,
                             QAction,
                             QActionGroup, 
                             QFileDialog,
                             QApplication,
                             QLabel,
                             QDockWidget,
                             QListWidget,
                             QFrame,
                             QSpinBox,
                             QInputDialog,
                             QMessageBox
                             )
from PyQt5.QtGui import (QImage,
                         QKeySequence,
                         QImageReader,
                         QPixmap,
                         QImageWriter, 
                         QPainter, 
                         QIcon)
from PyQt5.QtPrintSupport import (QPrinter, 
                                QPrintDialog)
import newimagedlg
import helpform
import qrc_resources

__version__ = "1.0.0"

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.image = QImage()
        self.filename = None
        self.dirty = False
        self.mirroredvertically = False
        self.mirroredhorizontally = False
        self.printer = None
        
        # main image display (central widget)
        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)

        # log widget (dock widget)
        logDockWidget = QDockWidget("Log", self)
        logDockWidget.setObjectName("LogDockWidget")
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|
                                      Qt.RightDockWidgetArea)
        self.listWidget = QListWidget() # log list (list widget)
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)

        # statusbar
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel|
                                     QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)

        # file actions
        fileNewAction = self.createAction("&New...",
                                          self.fileNew,
                                          QKeySequence.New,
                                          "filenew",
                                          "Create an image file")

        fileOpenAction = self.createAction("&Open...",
                                           self.fileOpen,
                                           QKeySequence.Open,
                                           "fileopen",
                                           "Open and existing image file")

        fileSaveAction = self.createAction("&Save",
                                           self.fileSave,
                                           QKeySequence.Save,
                                           "filesave",
                                           "Save the image")

        fileSaveAsAction = self.createAction("Save &As",
                                           self.fileSaveAs,
                                           icon="filesaveas", 
                                           tip="Save the image using a new name")
        filePrintAction = self.createAction("&Print", 
                                            self.filePrint, 
                                            QKeySequence.Print, 
                                            "fileprint", 
                                            "Print the image")
        fileQuitAction = self.createAction("&Quit",
                                           self.close,
                                           "Ctrl+Q",
                                           "filequit",
                                           "Close the application")

        
        # edit actions
        editZoomAction = self.createAction("&Zoom...",
                                           self.editZoom,
                                           "Alt+Z",
                                           "editzoom",
                                           "Zoom the image")

        editInvertAction = self.createAction("&Invert",
                                             self.editInvert,
                                             "Alt+I",
                                             "editinvert",
                                             "Invert the image", 
                                             "True", 
                                             "toggled")
        
        editSwapRedAndBlueAction = self.createAction("Sw&ap Red and Blue",
                                                    self.editSwapRedAndBlue, 
                                                    "Ctrl+A",
                                                    "editswap", 
                                                    "Swap the image's red and blue color components", 
                                                    True,
                                                    "toggled")
        mirrorGroup = QActionGroup(self)
        editUnMirrorAction = self.createAction("&Unmirror", 
                                                self.editUnMirror, 
                                                "Ctrl+U", 
                                                "editunmirror", 
                                                "Unmirror the image", 
                                                "True", 
                                                "toggled")
        mirrorGroup.addAction(editUnMirrorAction)
        editMirrorHorizontalAction = self.createAction("Mirror &Horizontally",
                                                self.editMirrorHorizontal,
                                                "Ctrl+H", 
                                                "editmirrorhoriz", 
                                                "Horizontally mirror the image", 
                                                True, 
                                                "toggled")
        mirrorGroup.addAction(editMirrorHorizontalAction)
        editMirrorVerticalAction = self.createAction("Mirror &Vertically",
                                                self.editMirrorVertical,
                                                "Ctrl+H", 
                                                "editmirrorvert", 
                                                "Vertically mirror the image", 
                                                True, 
                                                "toggled")
        mirrorGroup.addAction(editMirrorVerticalAction)
        editUnMirrorAction.setChecked(True)
        
        # help actions
        helpAboutAction = self.createAction("&About Image Changer", 
                                            self.helpAbout)
        helpHelpAction = self.createAction("&Help", 
                                            self.helpHelp, 
                                            QKeySequence.HelpContents)
        
        # file menu
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenuActions = (fileNewAction,
                                fileOpenAction,
                                fileSaveAction,
                                fileSaveAsAction,
                                filePrintAction, 
                                fileQuitAction)
        self.fileMenu.aboutToShow.connect(self.updateFileMenu)

        #edit menu
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addActions((editZoomAction,
                                  editInvertAction, 
                                  editSwapRedAndBlueAction, 
                                  editUnMirrorAction, 
                                  editMirrorHorizontalAction, 
                                  editMirrorVerticalAction))

        # help menu
        self.helpMenu = self.menuBar().addMenu("&Help")
        self.helpMenu.addActions((helpAboutAction, 
                                helpHelpAction))
        
        # file toolbar
        fileToolBar = self.addToolBar("File")
        fileToolBar.setObjectName("FileToolBar")
        fileToolBar.addActions((fileNewAction, fileOpenAction,
                                fileSaveAsAction))
        # edit toolbar
        editToolBar = self.addToolBar("Edit")
        editToolBar.setObjectName("EditToolBar")
        editToolBar.addActions((editInvertAction, 
                                editSwapRedAndBlueAction, 
                                editUnMirrorAction, 
                                editMirrorVerticalAction, 
                                editMirrorHorizontalAction))
        self.zoomSpinBox = QSpinBox()
        self.zoomSpinBox.setRange(1, 400)
        self.zoomSpinBox.setSuffix(" %")
        self.zoomSpinBox.setValue(100)
        self.zoomSpinBox.setToolTip("Zoom the image")
        self.zoomSpinBox.setStatusTip(self.zoomSpinBox.toolTip())
        self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
        self.zoomSpinBox.valueChanged.connect(self.showImage)
        editToolBar.addWidget(self.zoomSpinBox)
        # application settings
        settings = QSettings()
        self.recentFiles = settings.value("RecentFiles") or []
        mainWindowGeometry = settings.value("MainWindow/Geometry")
        if mainWindowGeometry is not None:
            self.restoreGeometry(mainWindowGeometry)
        mainWindowState = settings.value("MainWindow/State")
        if mainWindowState is not None:
            self.restoreState(mainWindowState)

        self.setWindowTitle("Image Changer")
        self.updateFileMenu()
        QTimer.singleShot(0, self.loadInitialFile)

    def fileNew(self):
        if not self.okToContinue():
            return
        dialog = newimagedlg.NewImageDlg(self)
        if dialog.exec_():
            self.addRecentFile(self.filename)
            self.image = QImage()
            #for action, check in self.resetableActions:
            #    action.setChecked(check)
            self.image = dialog.image()
            self.filename = None
            self.dirty = True
            self.showImage()
            self.sizeLabel.setText("{0}x{1}".format(self.image.width(),
                                                    self.image.height()))
            self.updateStatus("Created new image")

    def fileOpen(self):
        dir = (os.path.dirname(self.filename)
               if self.filename is not None else ".")
        formats = (["*.{0}".format(format.data().decode("ascii").lower())
                    for format in QImageReader.supportedImageFormats()])
        fname, format_ = QFileDialog.getOpenFileName(
            self,
            "Image Changer - Choose Image",
            dir,
            "Image files ({0})".format(" ".join(formats)))
        if fname:
            self.loadFile(fname, format_)

    def fileSave(self):
        if self.image.isNull():
            return
        if self.filename is None:
            return self.fileSaveAs()
        else:
            if self.image.save(self.filename, None):
                self.updateStatus("Saved as {0}".format(self.filename))
                self.dirty = False
                return True
            else:
                self.updateStatus("Failed to save {0}".format(
                    self.filename))
                return False

    def fileSaveAs(self):
        if self.image.isNull():
            return True
        fname = self.filename if self.filename is not None else "."
        formats = (["*.{0}".format(format.data().decode("ascii").lower())
                    for format in QImageWriter.supportedImageFormats()])
        fname, format_ = QFileDialog.getSaveFileName(
            self,
            "Image Changer - Save Image",
            fname,
            "Image files ({0})".format(" ".join(formats)))
        if fname:
            if "." not in fname:
                fname += ".png"
            self.addRecentFile(fname)
            self.filename = fname
            return self.fileSave()
        return False

    def filePrint(self):
        if self.image.isNull():
            return
        if self.printer is None:
            self.printer = QPrinter(QPrinter.HighResolution)
            self.printer.setPageSize(QPrinter.Letter)
        form = QPrintDialog(self.printer,  self)
        if form.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(),  rect.y(),  size.width(), 
                                size.height())
            painter.drawImage(0, 0, self.image)
            
    def addRecentFile(self, fname):
        if fname is None:
            return
        if not self.recentFiles or not fname in self.recentFiles:
            self.recentFiles.insert(0, fname)
            while len(self.recentFiles) > 9:
                self.recentFiles.takeLast()

    def loadInitialFile(self):
        settings = QSettings()
        fname = str(settings.value("LastFile"))
        if fname and QFile.exists(fname):
            self.loadFile(fname)

    def closeEvent(self, event):
        if self.okToContinue():
            settings = QSettings()
            filename = (QVariant(self.filename)
                        if self.filename is not None else QVariant())
            settings.setValue("LastFile", filename)
            recentFiles = (QVariant(self.recentFiles)
                           if self.recentFiles else QVariant())
            settings.setValue("RecentFiles", recentFiles)
            settings.setValue("MainWindow/Geometry", QVariant(
                self.saveGeometry()))
            settings.setValue("MainWindows/State", QVariant(
                self.saveState()))
        else:
            event.ignore()

    def okToContinue(self):
        if self.dirty:
            reply = QMessageBox.question(
                self,
                "Image Changer - Unsaved Changes",
                "Save unsaved changes?",
                QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                return self.fileSave()
        return True

    def editInvert(self, on):
        if self.image.isNull():
            return
        self.image.invertPixels()
        self.showImage()
        self.dirty = True
        self.updateStatus("Inverted" if on else "Uninverted")

    def editSwapRedAndBlue(self, on):
        if self.image.isNull():
            return
        self.image = self.image.rgbSwapped()
        self.showImage()
        self.dirty = True
        self.updateStatus(("Swapped Red and Blue"
                            if on else "Unswapped Red and Blue"))

    def editUnMirror(self, on):
        if self.image.isNull():
            return None
        if self.mirroredhorizontally:
            self.editMirrorHorizontal(False)
        if self.mirroredvertically:
            self.editMirrorVertical(False)

    def editMirrorHorizontal(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(True, False)
        self.showImage()
        self.dirty = True
        self.mirroredhorizontally = not self.mirroredhorizontally
        self.updateStatus("Mirrored Horizontally" if on else "Unmirrored Horizontally")

    def editMirrorVertical(self, on):
        if self.image.isNull():
            return
        self.image = self.image.mirrored(False, True)
        self.showImage()
        self.dirty = True
        self.mirroredvertically = not self.mirroredvertically
        self.updateStatus("Mirrored Vertically" if on else "Unmirrored Vertically")

    def editZoom(self):
        if self.image.isNull():
            return
        percent, ok = QInputDialog.getInt(
            self,
            "Image Changer - Zoom",
            "Percent:",
            self.zoomSpinBox.value(), 1, 400)
        if ok:
            self.zoomSpinBox.setValue(percent)

    def createAction(self, text, slot=None, shortcut=None, icon=None,
                     tip=None, checkable=False, signal="triggered"):
        action = QAction(text, self)
        if icon is not None:
            action.setIcon(QIcon(":/{0}.png".format(icon)))
        if shortcut is not None:
            action.setShortcut(shortcut)
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        if slot is not None:
            action.triggered.connect(slot)
        if checkable:
            action.setCheckable(True)
        return action

    def helpAbout(self):
        QMessageBox.about(self, "About Image Changer", 
                    """<b>Image Changer</b> v {0}
                    <p>Copyright &copy; 2016-1 Karma Ltd.
                    All rights reserved.
                    <p>This application can be used to perform
                    simple image manipulations.
                    <p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(
                        __version__,  platform.python_version(), 
                        QT_VERSION_STR,  PYQT_VERSION_STR, 
                        platform.system()))

    def helpHelp(self):
        form = helpform.HelpForm("index.html",  self)
        form.show()

    def loadFile(self, fname=None, format_=None):
        if not fname:
            action = self.sender()
            if isinstance(action,  QAction):
                fname = action.data()
                if not self.okToContinue():
                    return
            else:
                return
        if fname:
            self.filename = None
            image = QImage(fname, format_)
            if image.isNull():
                message = "Failed to read {0}".format(fname)
            else:
                self.addRecentFile(fname)
                self.image = image
                self.filename = fname
                self.showImage()
                self.dirty = False
                self.sizeLabel.setText("{0}x{1}".format(
                    image.width(), image.height()))
                message = "Loaded {0}".format(os.path.basename(fname))
            self.updateStatus(message)
            
    def showImage(self, percent=None):
        if self.image.isNull():
            return
        if percent is None:
            percent = 100.0
        factor = percent / 100.0
        width = self.image.width() * factor
        height = self.image.height() * factor
        image = self.image.scaled(width, height, Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(QPixmap.fromImage(image))

    def updateFileMenu(self):
        self.fileMenu.clear()
        self.fileMenu.addActions(self.fileMenuActions[:-1])
        current = self.filename if self.filename is not None else None
        recentFiles = []
        for fname in self.recentFiles:
            if fname != current and QFile.exists(fname):
                recentFiles.append(fname)
        if recentFiles:
            self.fileMenu.addSeparator()
            for i, fname in enumerate(recentFiles):
                action = QAction("&{0} {1}".format(
                    i+1, QFileInfo(fname).fileName()), self)
                action.setData(fname)
                action.triggered.connect(self.loadFile)
                self.fileMenu.addAction(action)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileMenuActions[-1])
                

    def updateStatus(self, message):
        self.statusBar().showMessage(message, 5000)
        self.listWidget.addItem(message)
        if self.filename is not None:
            self.setWindowTitle("Image Changer - {0}[*]".format(
                os.path.basename(self.filename)))
        elif not self.image.isNull():
            self.setWindowTitle("Image Changer - Unnamed[*]")
        else:
            self.setWindowTitle("Image Changer[*]")
        self.setWindowModified(self.dirty)


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("Karma Ltd.")
    app.setOrganizationDomain("karma.au")
    app.setApplicationName("Image Changer")
    form = MainWindow()
    form.show()
    app.exec_()

main()
