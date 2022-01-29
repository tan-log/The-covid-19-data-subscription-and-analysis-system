from PyQt5.QtCore import QUrl, Qt, QObject, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWebChannel import QWebChannel
import datetime
from epidemicModel import name_map

class JsInterface(QObject):
    def __init__(self):
        super(JsInterface, self).__init__()
        self.click_map_call_back = None

    @pyqtSlot(str)
    def receive_str_from_js(self, area):
        self.click_map_call_back(area)


class MapSelect(QWebEngineView):
    def __init__(self, parent):
        super(MapSelect, self).__init__()
        self.parent = parent
        self.setWindowFlag(Qt.Tool)
        self.setMinimumSize(910, 540)
        self.area_stack = []
        self.data = {}
        self.search_date = self.parent.end_date_edit.date().toString('yyyy-MM-dd')
        self.data['china'] = self.parent.model.get_daily_info_about_chinese_provinces(self.search_date)
        self.data['world'] = self.parent.model.get_daily_info_about_world(self.search_date)
        self.data['city'] = self.parent.model.get_daily_info_about_chinese_cities(self.search_date)
        self.create_map('world')
        self.js_interface = JsInterface()
        self.load(QUrl('file:///./web/map.html'))
        self.init_channel()
        self.setWindowTitle('选择地点')


        print("new")

    def init_channel(self):
        self.js_interface.click_map_call_back = self.create_map
        channel = QWebChannel(self.page())
        channel.registerObject("obj", self.js_interface)
        self.page().setWebChannel(channel)

    def update_data(self):
        print("update")
        self.search_date = self.parent.end_date_edit.date().toString('yyyy-MM-dd')
        self.data['china']=self.parent.model.get_daily_info_about_chinese_provinces(self.search_date)
        self.data['world']=self.parent.model.get_daily_info_about_world(self.search_date)
        self.data['city']=self.parent.model.get_daily_info_about_chinese_cities(self.search_date)
        return

    def create_map(self, area):
        if len(area) == 0:
            if len(self.area_stack) < 2:
                return
            else:
                self.area_stack.pop()
        else:
            if len(self.area_stack) > 2 or (len(self.area_stack) == 1 and area != '中国'):
                return
            else:
                self.area_stack.append(area)
        area = self.area_stack[-1].lower()
        search_bar = area
        if area == '中国':
            result = self.parent.model.draw_statistical_map_of_china(self.data['china'],datetime.datetime.strptime(self.search_date,'%Y-%m-%d').date())

        elif area == 'world' or area in name_map.values():
            result = self.parent.model.draw_statistical_map_of_world(self.data['world'],
                                                              datetime.datetime.strptime(self.search_date,'%Y-%m-%d').date())[0]
            search_bar = ''
        else:
            result = self.parent.model.draw_statistical_map_of_chinese_provinces(
                self.data['city'], area, datetime.datetime.strptime(self.search_date, '%Y-%m-%d').date())
            search_bar = '中国 ' + search_bar

        area_map = result
        self.parent.location_select.setCurrentText(search_bar)
        area_map.add_js_funcs(
            '''
            </script>
            <script src="./QWebChannel.js"></script>
            <script>
                document.addEventListener("DOMContentLoaded", function () {
                    new QWebChannel(qt.webChannelTransport, function (channel) {
                        window.obj = channel.objects.obj;
                    });
                });
            </script>
            <script>
                chart_map.on('click', function (params) {
                    var option = chart_map.getOption();
                    if(window.obj){
                        window.obj.receive_str_from_js(params.name)
                    }
                });
                chart_map.getZr().on('click', params => {
                    if(!params.target && window.obj){
                        window.obj.receive_str_from_js('')
                    }
            });
            '''
        )
        area_map.render("./web/map.html")
        self.reload()

