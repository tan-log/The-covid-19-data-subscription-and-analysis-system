from PyQt5.QtCore import QUrl, Qt, QObject, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView
from pyecharts.charts import Tab

import pandas as pd
class MapAnalyse(QWebEngineView):
    def __init__(self, parent):
        super(MapAnalyse, self).__init__()
        self.parent = parent
        self.setWindowFlag(Qt.Tool)
        self.setMinimumSize(1000, 600)
        self.load(QUrl('file:///./web/map2.html'))
        self.setWindowTitle('分析预测')
        self.predict_days = 30

    def update_map(self):
        area = self.parent.location_select.currentText().split()
        try:
            if len(area) <= 0:
                return
            elif len(area) == 1:
                data = self.parent.model.get_cumulative_info_about_country(area[0])
                data = self.parent.model.interpolating_daily_info_about_province_by_update_time(data)
                tab = Tab()
                predict_range = [i.strftime("%Y-%m-%d") for i in
                                 pd.date_range(start=str(data['updateTime'].max()), periods=self.predict_days + 1,
                                               freq='1D', closed='right').tolist()]

                tab.add(self.parent.model.draw_statistical_line(data['updateTime'].tolist(),data['province_confirmedCount'].tolist(),data['province_deadCount'].tolist(),data['province_curedCount'].tolist()), area[0]+"累计疫情地图")
                tab.add(
                    self.parent.model.draw_statistical_line(data['updateTime'].tolist(),
                                                     data['province_confirmedCount'].diff().tolist(),
                                                     data['province_deadCount'].diff().tolist(),
                                                     data['province_curedCount'].diff().tolist()),
                                                      area[0] + "新增疫情地图")
                tab.add(
                    self.parent.model.draw_predict_line(predict_range,
                                                     self.parent.model.predict_by_exponential_smoothing(data['province_confirmedCount'].tolist(),self.predict_days),
                                                     self.parent.model.predict_by_exponential_smoothing(data['province_deadCount'].tolist(),self.predict_days),
                                                     self.parent.model.predict_by_exponential_smoothing(data['province_curedCount'].tolist(),self.predict_days)), area[0] + "预测疫情地图")
                tab.render('./web/map2.html')
            elif len(area) == 2:
                data = self.parent.model.get_cumulative_info_about_province(area[0], area[1])
                data = self.parent.model.interpolating_daily_info_about_province_by_update_time(data)
                predict_range = [i.strftime("%Y-%m-%d") for i in
                                 pd.date_range(start=str(data['updateTime'].max()), periods=self.predict_days + 1,
                                               freq='1D', closed='right').tolist()]

                tab = Tab()
                tab.add(
                    self.parent.model.draw_statistical_line(data['updateTime'].tolist(), data['province_confirmedCount'].tolist(),
                                                     data['province_deadCount'].tolist(),
                                                     data['province_curedCount'].tolist()), area[1] + "累计疫情地图")
                tab.add(
                    self.parent.model.draw_statistical_line(data['updateTime'].tolist(), data['province_confirmedCount'].diff().tolist(),
                                                     data['province_deadCount'].diff().tolist(),
                                                     data['province_curedCount'].diff().tolist()),area[1] + "新增疫情地图")
                tab.add(
                    self.parent.model.draw_predict_line(predict_range,
                                                     self.parent.model.predict_by_exponential_smoothing(data['province_confirmedCount'].tolist(),self.predict_days),
                                                     self.parent.model.predict_by_exponential_smoothing(data['province_deadCount'].tolist(),self.predict_days),
                                                     self.parent.model.predict_by_exponential_smoothing(data['province_curedCount'].tolist(),self.predict_days)), area[1] + "预测疫情地图")
                tab.render('./web/map2.html')
            elif len(area) == 3:
                data = self.parent.model.get_cumulative_info_about_city(area[0],area[1],area[2])
                data = self.parent.model.interpolating_daily_info_about_city_by_update_time(data)
                predict_range = [i.strftime("%Y-%m-%d") for i in
                                 pd.date_range(start=str(data['updateTime'].max()), periods=self.predict_days + 1,
                                               freq='1D', closed='right').tolist()]

                tab = Tab()
                tab.add(
                    self.parent.model.draw_statistical_line(data['updateTime'].tolist(), data['city_confirmedCount'].tolist(),
                                                     data['city_deadCount'].tolist(),
                                                     data['city_curedCount'].tolist()), area[2] + "累计疫情地图")
                tab.add(
                    self.parent.model.draw_statistical_line(data['updateTime'].tolist(), data['city_confirmedCount'].diff().tolist(),
                                                     data['city_deadCount'].diff().tolist(),
                                                     data['city_curedCount'].diff().tolist()), area[2] + "新增疫情地图")
                tab.add(
                    self.parent.model.draw_predict_line(predict_range,
                                                     self.parent.model.predict_by_exponential_smoothing(data['city_confirmedCount'].tolist(),self.predict_days),
                                                     self.parent.model.predict_by_exponential_smoothing(data['city_deadCount'].tolist(),self.predict_days),
                                                     self.parent.model.predict_by_exponential_smoothing(data['city_curedCount'].tolist(),self.predict_days)), area[2] + "预测疫情地图")
                tab.render('./web/map2.html')

            self.reload()
        except Exception as e:
            print(e)
