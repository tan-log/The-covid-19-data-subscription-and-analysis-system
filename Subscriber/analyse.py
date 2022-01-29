from PyQt5.QtWidgets import QWidget, QLabel, QDateEdit, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, \
    QFileDialog, QTableWidget, QTableWidgetItem, QAbstractItemView, QCompleter
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QDate, Qt
from map_select import MapSelect
from map_analyse import MapAnalyse
import time
import csv
from epidemicModel import EpidemicModel

class Analyse(QWidget):
    def __init__(self):
        super(Analyse, self).__init__()
        self.data_file_names = ['./data/dataFile.csv']
        self.model = EpidemicModel()
        self.start_date_label = QLabel()
        self.start_date_edit = QDateEdit(QDate(2020, 1, 20), self)
        self.end_date_label = QLabel()
        self.end_date_edit = QDateEdit(QDate.currentDate(), self)
        self.location_select = QComboBox()
        self.location_select_map = {}
        self.select_map = MapSelect(self)
        self.analyse_map = MapAnalyse(self)
        self.import_btn = QPushButton()
        self.export_btn = QPushButton()
        self.location_btn = QPushButton()
        self.analyse_btn = QPushButton()
        self.refresh_btn = QPushButton()
        self.tabel = QTableWidget()
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        self.start_date_label.setPixmap(QPixmap('pic/startDate.png'))
        self.end_date_label.setPixmap(QPixmap('pic/endDate.png'))
        self.location_btn.setIcon(QIcon('pic/location.png'))
        self.import_btn.setIcon(QIcon('pic/import.png'))
        self.import_btn.setStyleSheet('QPushButton{border:none;} '
                                      'QPushButton:hover{background-color: rgb(224,224,224);}')
        self.export_btn.setIcon(QIcon('pic/export.png'))
        self.export_btn.setStyleSheet('QPushButton{border:none;} '
                                      'QPushButton:hover{background-color: rgb(224,224,224);}')
        self.location_btn.setStyleSheet('QPushButton{border:none;} '
                                        'QPushButton:hover{background-color: rgb(224,224,224);}')
        self.analyse_btn.setIcon(QIcon('pic/analyse.png'))
        self.analyse_btn.setStyleSheet('QPushButton{border:none;} '
                                       'QPushButton:hover{background-color: rgb(224,224,224);}')
        self.refresh_btn.setIcon(QIcon('pic/refresh.png'))
        self.refresh_btn.setStyleSheet('QPushButton{border:none;} '
                                       'QPushButton:hover{background-color: rgb(224,224,224);}')
        self.location_select.setFixedWidth(400)
        self.update_location_select()
        self.location_select.setEditable(True)
        self.location_select.setEditText('中国')
        completer = QCompleter(self.location_select.model(), self)
        completer.setFilterMode(Qt.MatchContains)
        completer.setModelSorting(QCompleter.CaseSensitivelySortedModel)
        self.location_select.setCompleter(completer)
        self.start_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.start_date_edit.setMinimumDate(self.start_date_edit.date())
        self.start_date_edit.setMaximumDate(self.end_date_edit.date())
        self.start_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.end_date_edit.setMinimumDate(self.start_date_edit.date())
        self.end_date_edit.setMaximumDate(self.end_date_edit.date())
        self.end_date_edit.setCalendarPopup(True)
        tabel_headers = ['地区', '邮政编码', '确诊人数', '疑似人数', '治愈人数', '死亡人数', '时间']
        self.tabel.setColumnCount(len(tabel_headers))
        self.tabel.horizontalHeader().setStretchLastSection(True)
        self.tabel.setHorizontalHeaderLabels(tabel_headers)
        self.tabel.setEditTriggers(QAbstractItemView.NoEditTriggers)
        control_layout = QHBoxLayout()
        control_layout.addWidget(self.import_btn)
        control_layout.addWidget(self.export_btn)
        control_layout.addStretch()
        control_layout.addWidget(self.start_date_label)
        control_layout.addWidget(self.start_date_edit)
        control_layout.addWidget(self.end_date_label)
        control_layout.addWidget(self.end_date_edit)
        control_layout.addWidget(self.location_select)
        control_layout.addWidget(self.location_btn)
        control_layout.addStretch()
        control_layout.addWidget(self.refresh_btn)
        control_layout.addWidget(self.analyse_btn)
        layout = QVBoxLayout()
        layout.addLayout(control_layout)
        layout.addWidget(self.tabel)
        self.setLayout(layout)

    def init_slot(self):
        self.location_btn.clicked.connect(self.location_btn_clicked)
        self.export_btn.clicked.connect(self.export_btn_clicked)
        self.import_btn.clicked.connect(self.import_btn_clicked)
        self.refresh_btn.clicked.connect(self.update_tabel)
        self.analyse_btn.clicked.connect(self.analyse_btn_clicked)

    def location_btn_clicked(self):
        self.select_map.update_data()
        self.select_map.show()

    def export_btn_clicked(self):
        path = './data/' + time.strftime("%Y-%m-%d")
        path = QFileDialog.getSaveFileName(self, '导出文件', path, '(*.csv)')
        file_name = path[0]
        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['地区', '邮政编码', '确诊人数', '疑似人数', '治愈人数', '死亡人数', '时间'])
            for i in range(0, self.tabel.rowCount()):
                row = []
                for j in range(0, self.tabel.columnCount()):
                    row.append(self.tabel.item(i, j).text())
                writer.writerow(row)

    def import_btn_clicked(self):
        path = QFileDialog.getOpenFileNames(self, '导入文件', './data/', '(*.csv)')
        self.data_file_names = path[0]
        self.model.updata_data_path(self.data_file_names[0])   # 传感器获取的数据

    def analyse_btn_clicked(self):
        self.analyse_map.update_map()
        self.analyse_map.show()
    def update_location_select(self):
        for file_name in self.data_file_names:
            with open(file_name, 'r', encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    area_name = row[2] if row[2] == row[4] else \
                        (row[2] + ' ' + row[4] if row[12] == '' else
                         row[2] + ' ' + row[4] + ' ' + row[12])
                    if area_name not in self.location_select_map:
                        self.location_select_map[area_name] = True
                        index = sorted(self.location_select_map).index(area_name)
                        self.location_select.insertItem(index, area_name)

    def update_tabel(self):
        self.update_location_select()
        self.tabel.setUpdatesEnabled(False)
        while self.tabel.rowCount() != 0:
            self.tabel.removeRow(0)
        select_name = self.location_select.currentText().split()
        name_map = [2, 4, 12]
        start_date = self.start_date_edit.date().toString('yyyy-MM-dd')
        end_date = self.end_date_edit.date().toString('yyyy-MM-dd')
        for file_name in self.data_file_names:
            with open(file_name, encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    row_date = row[11][0:10]
                    if row_date < start_date or row_date > end_date:
                        continue
                    for i in range(0, len(select_name)):
                        if select_name[i] != row[name_map[i]]:
                            break
                    else:
                        row_number = self.tabel.rowCount()
                        self.tabel.insertRow(row_number)
                        area_cow = 2 if row[2] == row[4] else (4 if row[12] == '' else 12)
                        info_map = [area_cow] + ([6, 7, 8, 9, 10, 11] if area_cow < 12 else [14, 15, 16, 17, 18, 11])
                        for j in range(0, len(info_map)):
                            self.tabel.setItem(row_number, j, QTableWidgetItem(row[info_map[j]]))
                        area_name = self.tabel.item(row_number, 0).text()
                        if len(area_name) > 3 and \
                                (area_name[0:3] == '境外输' or (area_name[0:3] == '外地来' or area_name[0:3] == '待明确')):
                            self.tabel.setItem(row_number, 0, QTableWidgetItem(row[4] + area_name))
        self.tabel.setUpdatesEnabled(True)
