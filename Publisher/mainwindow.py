from PyQt5.QtWidgets import QMainWindow, QWidget, QTabWidget, QVBoxLayout, QLabel, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from publish import Publish

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.init()

    def init(self):
        font = QFont()
        font.setPointSize(35)
        title = QLabel('   COVID-19数据发布系统   ')
        title.setFont(font)
        line = QFrame(self)
        line.setFrameShape(QFrame.HLine)
        # line.setFrameShadow(QFrame.Plain)
        publish = Publish()
        tab = QTabWidget(self)
        tab.addTab(publish, MainWindow.tr(self,'发布'))
        tab.setStyleSheet("QTabWidget:pane {border-top:0px;background: transparent;}"
                          "QTabWidget::tab-bar{alignment:center;}")

        layout = QVBoxLayout()
        layout.addWidget(title, 0, Qt.AlignHCenter)
        layout.addWidget(line)
        layout.addWidget(tab)

        widget = QWidget(self)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setWindowTitle('   COVID-19数据发布系统   ')
        self.show()
