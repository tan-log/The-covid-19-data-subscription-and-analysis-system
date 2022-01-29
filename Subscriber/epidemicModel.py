import numpy as np
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Line
from pyecharts.faker import Faker
from statsmodels.tsa.api import ExponentialSmoothing
import datetime

# from sklearn.ensemble import RandomForestRegressor
# from sklearn.model_selection import RandomizedSearchCV, train_test_split
# from sklearn.svm import SVR
# from sklearn.metrics import mean_squared_error, mean_absolute_error
# from sklearn.preprocessing import  PolynomialFeatures
# from sklearn.linear_model import Ridge


name_map = {
    'Singapore Rep.': '新加坡',
    'Dominican Rep.': '多米尼加',
    'Palestine': '巴勒斯坦',
    'Bahamas': '巴哈马',
    'Timor-Leste': '东帝汶',
    'Afghanistan': '阿富汗',
    'Guinea-Bissau': '几内亚比绍',
    "Côte d'Ivoire": '科特迪瓦',
    'Siachen Glacier': '锡亚琴冰川',
    "Br. Indian Ocean Ter.": '英属印度洋领土',
    'Angola': '安哥拉',
    'Albania': '阿尔巴尼亚',
    'United Arab Emirates': '阿联酋',
    'Argentina': '阿根廷',
    'Armenia': '亚美尼亚',
    'French Southern and Antarctic Lands': '法属南半球和南极领地',
    'Australia': '澳大利亚',
    'Austria': '奥地利',
    'Azerbaijan': '阿塞拜疆',
    'Burundi': '布隆迪',
    'Belgium': '比利时',
    'Benin': '贝宁',
    'Burkina Faso': '布基纳法索',
    'Bangladesh': '孟加拉国',
    'Bulgaria': '保加利亚',
    'The Bahamas': '巴哈马',
    'Bosnia and Herz.': '波斯尼亚和黑塞哥维那',
    'Belarus': '白俄罗斯',
    'Belize': '伯利兹',
    'Bermuda': '百慕大',
    'Bolivia': '玻利维亚',
    'Brazil': '巴西',
    'Brunei': '文莱',
    'Bhutan': '不丹',
    'Botswana': '博茨瓦纳',
    'Central African Rep.': '中非共和国',
    'Canada': '加拿大',
    'Switzerland': '瑞士',
    'Chile': '智利',
    'China': '中国',
    'Ivory Coast': '象牙海岸',
    'Cameroon': '喀麦隆',
    'Dem. Rep. Congo': '刚果（金）',
    'Congo': '刚果（布）',
    'Colombia': '哥伦比亚',
    'Costa Rica': '哥斯达黎加',
    'Cuba': '古巴',
    'N. Cyprus': '北塞浦路斯',
    'Cyprus': '塞浦路斯',
    'Czech Rep.': '捷克',
    'Germany': '德国',
    'Djibouti': '吉布提',
    'Denmark': '丹麦',
    'Algeria': '阿尔及利亚',
    'Ecuador': '厄瓜多尔',
    'Egypt': '埃及',
    'Eritrea': '厄立特里亚',
    'Spain': '西班牙',
    'Estonia': '爱沙尼亚',
    'Ethiopia': '埃塞俄比亚',
    'Finland': '芬兰',
    'Fiji': '斐',
    'Falkland Islands': '福克兰群岛',
    'France': '法国',
    'Gabon': '加蓬',
    'United Kingdom': '英国',
    'Georgia': '格鲁吉亚',
    'Ghana': '加纳',
    'Guinea': '几内亚',
    'Gambia': '冈比亚',
    'Guinea Bissau': '几内亚比绍',
    'Eq. Guinea': '赤道几内亚',
    'Greece': '希腊',
    'Greenland': '格陵兰',
    'Guatemala': '危地马拉',
    'French Guiana': '法属圭亚那',
    'Guyana': '圭亚那',
    'Honduras': '洪都拉斯',
    'Croatia': '克罗地亚',
    'Haiti': '海地',
    'Hungary': '匈牙利',
    'Indonesia': '印度尼西亚',
    'India': '印度',
    'Ireland': '爱尔兰',
    'Iran': '伊朗',
    'Iraq': '伊拉克',
    'Iceland': '冰岛',
    'Israel': '以色列',
    'Italy': '意大利',
    'Jamaica': '牙买加',
    'Jordan': '约旦',
    'Japan': '日本',
    'Kazakhstan': '哈萨克斯坦',
    'Kenya': '肯尼亚',
    'Kyrgyzstan': '吉尔吉斯斯坦',
    'Cambodia': '柬埔寨',
    'Korea': '韩国',
    'Kosovo': '科索沃',
    'Kuwait': '科威特',
    'Lao PDR': '老挝',
    'Lebanon': '黎巴嫩',
    'Liberia': '利比里亚',
    'Libya': '利比亚',
    'Sri Lanka': '斯里兰卡',
    'Lesotho': '莱索托',
    'Lithuania': '立陶宛',
    'Luxembourg': '卢森堡',
    'Latvia': '拉脱维亚',
    'Morocco': '摩洛哥',
    'Moldova': '摩尔多瓦',
    'Madagascar': '马达加斯加',
    'Mexico': '墨西哥',
    'Macedonia': '马其顿',
    'Mali': '马里',
    'Myanmar': '缅甸',
    'Montenegro': '黑山',
    'Mongolia': '蒙古',
    'Mozambique': '莫桑比克',
    'Mauritania': '毛里塔尼亚',
    'Malawi': '马拉维',
    'Malaysia': '马来西亚',
    'Namibia': '纳米比亚',
    'New Caledonia': '新喀里多尼亚',
    'Niger': '尼日尔',
    'Nigeria': '尼日利亚',
    'Nicaragua': '尼加拉瓜',
    'Netherlands': '荷兰',
    'Norway': '挪威',
    'Nepal': '尼泊尔',
    'New Zealand': '新西兰',
    'Oman': '阿曼',
    'Pakistan': '巴基斯坦',
    'Panama': '巴拿马',
    'Peru': '秘鲁',
    'Philippines': '菲律宾',
    'Papua New Guinea': '巴布亚新几内亚',
    'Poland': '波兰',
    'Puerto Rico': '波多黎各',
    'Dem. Rep. Korea': '朝鲜',
    'Portugal': '葡萄牙',
    'Paraguay': '巴拉圭',
    'Qatar': '卡塔尔',
    'Romania': '罗马尼亚',
    'Russia': '俄罗斯',
    'Rwanda': '卢旺达',
    'W. Sahara': '西撒哈拉',
    'Saudi Arabia': '沙特阿拉伯',
    'Sudan': '苏丹',
    'S. Sudan': '南苏丹',
    'Senegal': '塞内加尔',
    'Solomon Is.': '所罗门群岛',
    'Sierra Leone': '塞拉利昂',
    'El Salvador': '萨尔瓦多',
    'Somaliland': '索马里兰',
    'Somalia': '索马里',
    'Serbia': '塞尔维亚',
    'Suriname': '苏里南',
    'Slovakia': '斯洛伐克',
    'Slovenia': '斯洛文尼亚',
    'Sweden': '瑞典',
    'Swaziland': '斯威士兰',
    'Syria': '叙利亚',
    'Chad': '乍得',
    'Togo': '多哥',
    'Thailand': '泰国',
    'Tajikistan': '塔吉克斯坦',
    'Turkmenistan': '土库曼斯坦',
    'East Timor': '东帝汶',
    'Trinidad and Tobago': '特里尼达和多巴哥',
    'Tunisia': '突尼斯',
    'Turkey': '土耳其',
    'Tanzania': '坦桑尼亚',
    'Uganda': '乌干达',
    'Ukraine': '乌克兰',
    'Uruguay': '乌拉圭',
    'United States': '美国',
    'Uzbekistan': '乌兹别克斯坦',
    'Venezuela': '委内瑞拉',
    'Vietnam': '越南',
    'Vanuatu': '瓦努阿图',
    'West Bank': '西岸',
    'Yemen': '也门',
    'South Africa': '南非',
    'Zambia': '赞比亚',
    'Zimbabwe': '津巴布韦',
    'Comoros': '科摩罗'
}


class EpidemicModel:
    def __init__(self):
        self.path = './data/dataFile.csv'
        self.data = pd.read_csv(self.path)  # 传感器获取的数据

    def updata_data_path(self,path):
        self.path = path
        self.data = pd.read_csv(path)

    def updata_data(self,dict):
        data = pd.DataFrame(dict, index=[0])  # data需要是字典格式
        data.to_csv(self.path, mode='a', index=None, header=False, encoding="utf_8", )

    def get_cumulative_info_about_chinese_cities(self):
        try:
            # 数据清洗
            # 国内疫情数据选取
            CHINA = self.data.loc[self.data['countryName'] == '中国']
            CHINA = CHINA.dropna(subset=['cityName'], how='any')
            # 取出含所有中国城市的列表,遍历取出每一个城市的子dataframe，然后用sort对updateTime进行时间排序
            cities = list(set(CHINA['cityName']))
            for city in cities:
                CHINA.loc[CHINA['cityName'] == city].sort_values(by='updateTime')
            # 去除空值所在行
            CHINA.dropna(subset=['cityName'], inplace=True)
            # CHINA中的updateTime列进行格式化处理
            CHINA.updateTime = pd.to_datetime(CHINA.updateTime, format="%Y-%m-%d", errors='coerce').dt.date
            # 遍历每个城市dataframe进行每日数据的去重,每日数据的去重只保留第一个数据，因为前面已经对时间进行排序，第一个数据即为当天最新数据
            real = CHINA.loc[CHINA['cityName'] == cities[0]]
            real = real.drop_duplicates(subset='updateTime', keep='first')
            china = real
            for city in cities[1:]:
                real_data = CHINA.loc[CHINA['cityName'] == city]
                real_data = real_data.drop_duplicates(subset='updateTime', keep='first')
                china = pd.concat([real_data, china], sort=False)
            return china
        except Exception as e:
            print(e)
            return None

    def get_daily_info_about_chinese_cities(self,search_time):
        try:
            # 数据清洗
            # 国内疫情数据选取
            CHINA = self.data.loc[self.data['countryName'] == '中国']
            CHINA = CHINA.loc[CHINA['updateTime'].str.startswith(search_time)]
            CHINA = CHINA.dropna(subset=['cityName'], how='any')
            # 取出含所有中国城市的列表,遍历取出每一个城市的子dataframe，然后用sort对updateTime进行时间排序
            cities = list(set(CHINA['cityName']))
            for city in cities:
                CHINA.loc[CHINA['cityName'] == city].sort_values(by='updateTime')
            # 去除空值所在行
            CHINA.dropna(subset=['cityName'], inplace=True)
            # CHINA中的updateTime列进行格式化处理
            CHINA.updateTime = pd.to_datetime(CHINA.updateTime, format="%Y-%m-%d", errors='coerce').dt.date
            # 遍历每个城市dataframe进行每日数据的去重,每日数据的去重只保留第一个数据，因为前面已经对时间进行排序，第一个数据即为当天最新数据
            real = CHINA.loc[CHINA['cityName'] == cities[0]]
            real = real.drop_duplicates(subset='updateTime', keep='first')
            china = real
            for city in cities[1:]:
                real_data = CHINA.loc[CHINA['cityName'] == city]
                real_data = real_data.drop_duplicates(subset='updateTime', keep='first')
                china = pd.concat([real_data, china], sort=False)
            return china
        except Exception as e:
            print(e)
            return None

    def get_daily_info_about_world(self,search_time):
        try:
            # 数据清洗
            world = self.data.copy()
            search_time = datetime.datetime.strptime(search_time, '%Y-%m-%d').strftime("%Y-%m-%d")
            world = world.loc[world['updateTime'].str.startswith(search_time)]
            # 数据去除空值
            world = world.dropna(subset=['provinceName', 'updateTime'])
            # 遍历国家列表对world中的updateTime进行处理并去重。
            country = list(set(world['provinceName']))
            for c in country:
                world.loc[world['provinceName'] == c].sort_values(by='updateTime')

            world.updateTime = pd.to_datetime(world.updateTime, format="%Y-%m-%d", errors='coerce').dt.date
            world = world.drop_duplicates(subset=['updateTime', 'provinceName'], keep='first')
            return world
        except Exception as e:
            print(e)
            return None
    def get_cumulative_info_about_city(self,country_name,province_name,city_name):
        try:
            # 数据清洗
            # 疫情数据选取
            cumulative_data = self.data.loc[(self.data['countryName']==country_name) & (self.data['provinceName']==province_name) & (self.data['cityName'] == city_name)]
            # 数据去除空值
            cumulative_data = cumulative_data.dropna(subset=['cityName', 'updateTime'], how='any')
            # 用sort对updateTime进行时间排序
            cumulative_data.sort_values(by='updateTime')

            # updateTime列进行格式化处理
            cumulative_data.updateTime = pd.to_datetime(cumulative_data.updateTime, format="%Y-%m-%d", errors='coerce').dt.date
            # 去重获得城市每日信息
            cumulative_data.drop_duplicates(subset=['updateTime'], keep='first', inplace=True)
            return cumulative_data
        except Exception as e:
            print(e)
            return None

    def get_cumulative_info_about_country(self,country_name):
        try:
            # 数据清洗
            # 疫情数据选取
            cumulative_data = self.data.loc[(self.data['countryName'] == country_name)&(self.data['countryName']==self.data['provinceName'])]
            # 数据去除空值
            cumulative_data = cumulative_data.dropna(subset=['countryName', 'updateTime'], how='any')
            # 国家发布没有市名
            cumulative_data = cumulative_data.loc[cumulative_data['cityName'].isna() == True]
            # 用sort对updateTime进行时间排序
            cumulative_data.sort_values(by='updateTime')

            # updateTime列进行格式化处理
            cumulative_data.updateTime = pd.to_datetime(cumulative_data.updateTime, format="%Y-%m-%d", errors='coerce').dt.date
            # 去重获得省份每日信息
            cumulative_data.drop_duplicates(subset=['provinceName','updateTime'], keep='first', inplace=True)
            return cumulative_data
        except Exception as e:
            print(e)
            return None

    def get_cumulative_info_about_province(self,country_name,province_name):
        try:
            # 数据清洗
            # 疫情数据选取
            cumulative_data = self.data.loc[(self.data['countryName'] == country_name)&(self.data['provinceName']==province_name)]
            # 数据去除空值
            cumulative_data = cumulative_data.dropna(subset=['countryName', 'updateTime'], how='any')
            # 用sort对updateTime进行时间排序
            cumulative_data.sort_values(by='updateTime')

            # updateTime列进行格式化处理
            cumulative_data.updateTime = pd.to_datetime(cumulative_data.updateTime, format="%Y-%m-%d", errors='coerce').dt.date
            # 去重获得省份每日信息
            cumulative_data.drop_duplicates(subset=['provinceName','updateTime'], keep='first', inplace=True)
            return cumulative_data
        except Exception as e:
            print(e)
            return None

    def get_daily_info_about_chinese_provinces(self,search_time):
        try:
            # 数据清洗
            # 国内疫情数据选取
            search_time= datetime.datetime.strptime(search_time, '%Y-%m-%d').strftime("%Y-%m-%d")
            CHINA = self.data.loc[self.data['countryName'] == '中国']
            CHINA = CHINA.loc[CHINA['updateTime'].str.startswith(search_time)]
            # 数据去除空值
            CHINA = CHINA.dropna(subset=['provinceName', 'updateTime'], how='any')
            # 取出省份列表,然后用sort对updateTime进行时间排序
            provinces = list(set(CHINA['provinceName']))
            for province in provinces:
                CHINA.loc[CHINA['provinceName'] == province].sort_values(by='updateTime')

            # CHINA中的updateTime列进行格式化处理
            CHINA.updateTime = pd.to_datetime(CHINA.updateTime, format="%Y-%m-%d", errors='coerce').dt.date
            # 去重获得省份每日信息
            CHINA.drop_duplicates(subset=['updateTime', 'provinceName'], keep='first', inplace=True)
            return CHINA
        except Exception as e:
            print(e)
            return None

    # 指数平滑法
    @staticmethod
    def predict_by_exponential_smoothing(data,predicted_days):
        confirmedCount = np.array(data).reshape(-1, 1)  # 确诊数
        try:
            fit1 = ExponentialSmoothing(confirmedCount,seasonal_periods=7,trend='add',seasonal='add',).fit()
        except Exception as e:
            print(e)
            fit1 = ExponentialSmoothing(confirmedCount,trend='add').fit()
        pred = fit1.forecast(predicted_days)
        return [int(x) for x in pred]
    '''
    # 向量机
    @staticmethod
    def predict_by_SVM(data,predicted_days):
        confirmedCount = np.array(data).reshape(-1, 1)  # 确诊数
        days_since_1_1 = np.array([i for i in range(len(confirmedCount))]).reshape(-1, 1)
        future_forcast = np.array([i for i in range(len(confirmedCount)+1,len(confirmedCount)+1+predicted_days)]).reshape(-1, 1)
        X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(days_since_1_1,
                                                                                                    confirmedCount,
                                                                                                    test_size=0.02,
                                                                                                    shuffle=False)
        y_train_confirmed = y_train_confirmed.reshape(-1, 1)
        X_train_confirmed = X_train_confirmed.reshape(-1, 1)

        kernel = ['linear', 'rbf']
        # c是错误的惩罚参数C.默认1
        c = [0.01, 0.1, 1, 10]
        # gamma是'rbf'，'poly'和'sigmoid'的核系数。默认是'auto'
        gamma = [0.01, 0.1, 1]
        # Epsilon在epsilon-SVR模型中。它指定了epsilon-tube，其中训练损失函数中没有惩罚与在实际值的距离epsilon内预测的点。默认值是0.1
        epsilon = [0.01, 0.1, 1]
        # shrinking指明是否使用收缩启发式。默认为True
        shrinking = [True, False]
        svm_grid = {'kernel': kernel, 'C': c, 'gamma': gamma, 'epsilon': epsilon, 'shrinking': shrinking}
        # 建立支持向量回归模型
        svm = SVR()
        # 使用随机搜索进行超参优化
        svm_search = RandomizedSearchCV(svm, svm_grid, scoring='neg_mean_squared_error', cv=3, return_train_score=True,
                                        n_jobs=-1, n_iter=30, verbose=1)
        svm_search.fit(X_train_confirmed, y_train_confirmed.ravel())
        # 使用刚刚优化的参数进行建模，然后预测，并输出均方误差
        svm_confirmed = svm_search.best_estimator_
        svm_pred = svm_confirmed.predict(future_forcast)
        return [int(x[0]) for x in svm_pred]



    # 岭回归
    @staticmethod
    def predict_by_CLF(data,predicted_days):
        confirmedCount = np.array(data).reshape(-1, 1)  # 确诊数
        days_since_1_1 = np.array([i for i in range(len(confirmedCount))]).reshape(-1, 1)
        future_forcast = np.array([i for i in range(len(confirmedCount)+1,len(confirmedCount)+1+predicted_days)]).reshape(-1, 1)
        X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(days_since_1_1,
                                                                                                    confirmedCount,
                                                                                                    test_size=0.02,
                                                                                                    shuffle=False)
        y_train_confirmed = y_train_confirmed.reshape(-1, 1)
        X_train_confirmed = X_train_confirmed.reshape(-1, 1)
        # 岭回归
        ridge = PolynomialFeatures(degree=7)
        X_ridge = ridge.fit_transform(X_train_confirmed)
        clf = Ridge(alpha=0.001, fit_intercept=True)
        clf.fit(X_ridge, y_train_confirmed)
        ridge_pred = clf.predict(ridge.fit_transform(future_forcast))
        return [int(x[0]) for x in ridge_pred]

    # 随机森林
    @staticmethod
    def predict_by_random_forest(data,predicted_days):
        confirmedCount = np.array(data).reshape(-1, 1)  # 确诊数
        days_since_1_1 = np.array([i for i in range(len(confirmedCount))]).reshape(-1, 1)
        future_forcast = np.array([i for i in range(len(confirmedCount)+1,len(confirmedCount)+1+predicted_days)]).reshape(-1, 1)
        X_train_confirmed, X_test_confirmed, y_train_confirmed, y_test_confirmed = train_test_split(days_since_1_1,
                                                                                                    confirmedCount,
                                                                                                    test_size=0.02,
                                                                                                    shuffle=False)
        y_train_confirmed = y_train_confirmed.reshape(-1, 1)
        X_train_confirmed = X_train_confirmed.reshape(-1, 1)
        ensemble_grid = {'n_estimators': [(i + 1) * 10 for i in range(20)],
                         'criterion': ['mse', 'mae'],
                         'bootstrap': [True, False],
                         }
        ensemble = RandomForestRegressor()
        ensemble_search = RandomizedSearchCV(ensemble, ensemble_grid, scoring='neg_mean_squared_error', cv=3,
                                             return_train_score=True, n_jobs=-1, n_iter=10, verbose=1)
        ensemble_search.fit(X_train_confirmed, y_train_confirmed.ravel())
        ensemble_confirmed = ensemble_search.best_estimator_
        ensemble_pred = ensemble_confirmed.predict(future_forcast)
        return [int(x[0]) for x in ensemble_pred]
    '''
    @staticmethod
    def interpolating_daily_info_about_province_by_update_time(data):
        # 插值处理
        # 先创建省份列表和日期列表，并初始化一个draft
        province = list(set(data['provinceName']))  # 每个省份
        start = data.loc[data['provinceName'] == province[0]]['updateTime'].min()
        end = data['updateTime'].max()

        # 插值日期
        interpolatingDate = pd.date_range(start=str(start), end=str(end))

        aid_frame = pd.DataFrame(
            {'updateTime': interpolatingDate, 'provinceName': [province[0]] * len(interpolatingDate)})
        aid_frame.updateTime = pd.to_datetime(aid_frame.updateTime, format="%Y-%m-%d", errors='coerce').dt.date

        # 第一个省份插值
        interpolatingDailyInfo = pd.concat([data.loc[data['provinceName'] == province[0]], aid_frame],
                                           join='outer').sort_values(
            ['updateTime', 'province_confirmedCount'], na_position='last')

        interpolatingDailyInfo.province_confirmedCount.fillna(method="ffill", inplace=True)
        interpolatingDailyInfo.province_suspectedCount.fillna(method="ffill", inplace=True)
        interpolatingDailyInfo.province_curedCount.fillna(method="ffill", inplace=True)
        interpolatingDailyInfo.province_deadCount.fillna(method="ffill", inplace=True)

        # 所有省份插值，日期格式化
        for p in range(1, len(province)):
            date_d = []
            for dt in data.loc[data['provinceName'] == province[p]]['updateTime']:
                date_d.append(dt)
            date_d = list(set(date_d))
            date_d.sort()
            start = data.loc[data['provinceName'] == province[p]]['updateTime'].min()
            interpolatingDate = pd.date_range(start=str(start), end=str(end))
            aid_frame = pd.DataFrame(
                {'updateTime': interpolatingDate, 'provinceName': [province[p]] * len(interpolatingDate)})
            aid_frame.updateTime = pd.to_datetime(aid_frame.updateTime, format="%Y-%m-%d", errors='coerce').dt.date

            draft_d = pd.concat([data.loc[data['provinceName'] == province[p]], aid_frame], join='outer').sort_values(
                ['updateTime', 'province_confirmedCount'], na_position='last')
            draft_d.province_confirmedCount.fillna(method="ffill", inplace=True)
            draft_d.province_suspectedCount.fillna(method="ffill", inplace=True)
            draft_d.province_curedCount.fillna(method="ffill", inplace=True)
            draft_d.province_deadCount.fillna(method="ffill", inplace=True)
            interpolatingDailyInfo = pd.concat([interpolatingDailyInfo, draft_d])

        # 去重
        interpolatingDailyInfo = interpolatingDailyInfo.drop_duplicates(subset=['provinceName', 'updateTime'],
                                                                        keep='first')
        return interpolatingDailyInfo

    @staticmethod
    def interpolating_daily_info_about_city_by_update_time(data):
        # 插值处理
        # 先创建城市列表和日期列表，并初始化一个draft
        city = list(set(data['cityName']))  # 每个城市
        start = data.loc[data['cityName'] == city[0]]['updateTime'].min()
        end = data['updateTime'].max()

        # 插值日期
        interpolatingDate = pd.date_range(start=str(start), end=str(end))

        aid_frame = pd.DataFrame(
            {'updateTime': interpolatingDate, 'cityName': [city[0]] * len(interpolatingDate)})
        aid_frame.updateTime = pd.to_datetime(aid_frame.updateTime, format="%Y-%m-%d", errors='coerce').dt.date

        # 第一个城市插值
        interpolatingDailyInfo = pd.concat([data.loc[data['cityName'] == city[0]], aid_frame],
                                           join='outer').sort_values(
            ['updateTime', 'city_confirmedCount'], na_position='last')

        interpolatingDailyInfo.city_confirmedCount.fillna(method="ffill", inplace=True)
        interpolatingDailyInfo.city_suspectedCount.fillna(method="ffill", inplace=True)
        interpolatingDailyInfo.city_curedCount.fillna(method="ffill", inplace=True)
        interpolatingDailyInfo.city_deadCount.fillna(method="ffill", inplace=True)

        # 所有城市插值，日期格式化
        for p in range(1, len(city)):
            date_d = []
            for dt in data.loc[data['cityName'] == city[p]]['updateTime']:
                date_d.append(dt)
            date_d = list(set(date_d))
            date_d.sort()
            start = data.loc[data['cityName'] == city[p]]['updateTime'].min()
            interpolatingDate = pd.date_range(start=str(start), end=str(end))
            aid_frame = pd.DataFrame(
                {'updateTime': interpolatingDate, 'cityName': [city[p]] * len(interpolatingDate)})
            aid_frame.updateTime = pd.to_datetime(aid_frame.updateTime, format="%Y-%m-%d", errors='coerce').dt.date

            draft_d = pd.concat([data.loc[data['cityName'] == city[p]], aid_frame], join='outer').sort_values(
                ['updateTime', 'city_confirmedCount'], na_position='last')
            draft_d.city_confirmedCount.fillna(method="ffill", inplace=True)
            draft_d.city_suspectedCount.fillna(method="ffill", inplace=True)
            draft_d.city_curedCount.fillna(method="ffill", inplace=True)
            draft_d.city_deadCount.fillna(method="ffill", inplace=True)
            interpolatingDailyInfo = pd.concat([interpolatingDailyInfo, draft_d])

        # 去重
        interpolatingDailyInfo = interpolatingDailyInfo.drop_duplicates(subset=['cityName', 'updateTime'],
                                                                        keep='first')
        return interpolatingDailyInfo


    @staticmethod
    def draw_statistical_map_of_china(data, search_time) -> Map:
        data_list_province_confirmedCount = None
        data_list_province_curedCount = None
        data_list_province_deadCount = None
        try:
            data['provinceName'] = data['provinceName'].str[0:2]
            data.loc[data['provinceName'] == '内蒙', ['provinceName']] = '内蒙古'
            data.loc[data['provinceName'] == '黑龙', ['provinceName']] = '黑龙江'
            data = data.loc[data['updateTime'] == search_time]
            # 1.根据绘制国内总疫情图
            data_list_province_confirmedCount = list(
                zip(data['provinceName'].values.tolist(), data['province_confirmedCount'].values.tolist()))
            data_list_province_curedCount = list(
                zip(data['provinceName'].values.tolist(), data['province_curedCount'].values.tolist()))
            data_list_province_deadCount = list(
                zip(data['provinceName'].values.tolist(), data['province_deadCount'].values.tolist()))
            data_list_province_confirmedCount.append(tuple(["null", 0]))
            data_list_province_curedCount.append(tuple(["null", 0]))
            data_list_province_deadCount.append(tuple(["null", 0]))
            # 数据格式[(黑龙江,200),(吉林,300),...]
        except Exception as e:
            print(e)
        c = (
            Map(init_opts=opts.InitOpts(chart_id='map'))
                .add(series_name="确诊病例", data_pair=data_list_province_confirmedCount, maptype='china',
                     is_map_symbol_show=False)
                .add(series_name="治愈病例", data_pair=data_list_province_curedCount, is_map_symbol_show=False,
                     maptype='china', )
                .add(series_name="死亡病例", data_pair=data_list_province_deadCount, is_map_symbol_show=False,
                     maptype='china')
                .set_global_opts(
                title_opts=opts.TitleOpts(title='累计疫情地图',
                                          subtitle="日期：{}".format(search_time)),
                visualmap_opts=opts.VisualMapOpts(is_piecewise=False,
                                                  max_=data['province_confirmedCount'].max() / 10,
                                                  pieces=[
                                                      {"max": 0, "label": "0人", "color": "#FFFFFF"},
                                                      {"min": 1, "max": 9, "label": "1-10人", "color": "#FFEBCD"},
                                                      {"min": 10, "max": 99, "label": "10-99人", "color": "#FFA07A"},
                                                      {"min": 100, "max": 499, "label": "100-499人", "color": "#FF4040"},
                                                      {"min": 500, "max": 999, "label": "500-999人", "color": "#CD2626"},
                                                      {"min": 1000, "max": 10000, "label": "1000-10000人",
                                                       "color": "#B22222"},
                                                      {'min': 10000, "label": ">10000人", "color": "#8B1A1A"}])
                # 不指定 max，表示 max 为无限大
            )
        )
        return c
    @staticmethod
    def draw_statistical_map_of_chinese_provinces(data, province_name,search_time) -> Map:
        data_list_province_confirmedCount = []
        data_list_province_curedCount = []
        data_list_province_deadCount = []
        try:
            data['provinceName'] = data['provinceName'].str[0:2]
            data.loc[data['provinceName'] == '内蒙', ['provinceName']] = '内蒙古'
            data.loc[data['provinceName'] == '黑龙', ['provinceName']] = '黑龙江'
            data = data.loc[data['updateTime'] == search_time]
            data = data.loc[data['provinceName'] == province_name]
            data['cityName'] = data['cityName']+"市"
            # 1.根据绘制国内总疫情图
            data_list_province_confirmedCount = list(
                zip(data['cityName'].values.tolist(), data['city_confirmedCount'].values.tolist()))
            data_list_province_curedCount = list(
                zip(data['cityName'].values.tolist(), data['city_curedCount'].values.tolist()))
            data_list_province_deadCount = list(
                zip(data['cityName'].values.tolist(), data['city_deadCount'].values.tolist()))
            # 数据格式[(黑龙江,200),(吉林,300),...]
        except Exception as e:
            print(e)
        finally:
            data_list_province_confirmedCount.append(tuple(["null", 0]))
            data_list_province_curedCount.append(tuple(["null", 0]))
            data_list_province_deadCount.append(tuple(["null", 0]))
        c = (
            Map(init_opts=opts.InitOpts(chart_id='map'))
                .add(series_name="确诊病例", data_pair=data_list_province_confirmedCount, maptype=province_name,
                     is_map_symbol_show=False)
                .add(series_name="治愈病例", data_pair=data_list_province_curedCount, is_map_symbol_show=False,
                     maptype=province_name, )
                .add(series_name="死亡病例", data_pair=data_list_province_deadCount, is_map_symbol_show=False,
                     maptype=province_name)
                .set_global_opts(
                title_opts=opts.TitleOpts(title='累计疫情地图',
                                          subtitle="日期：{}".format(search_time)),
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                  pieces=[
                                                      {"max": 0, "label": "0人", "color": "#FFFFFF"},
                                                      {"min": 1, "max": 9, "label": "1-10人", "color": "#FFEBCD"},
                                                      {"min": 10, "max": 99, "label": "10-99人", "color": "#FFA07A"},
                                                      {"min": 100, "max": 499, "label": "100-499人", "color": "#FF4040"},
                                                      {"min": 500, "max": 999, "label": "500-999人", "color": "#CD2626"},
                                                      {"min": 1000, "max": 10000, "label": "1000-10000人",
                                                       "color": "#B22222"},
                                                      {'min': 10000, "label": ">10000人", "color": "#8B1A1A"}])
                # 不指定 max，表示 max 为无限大
            )
        )
        return c

    @staticmethod
    def draw_statistical_map_of_world(data, search_time) -> Map:
        try:
            world = data.loc[data['updateTime'] == search_time]
            data_list_province_confirmedCount = list(zip(world['provinceName'], world['province_confirmedCount']))
            data_list_province_curedCount = list(zip(world['provinceName'], world['province_curedCount']))
            data_list_province_deadCount = list(zip(world['provinceName'], world['province_deadCount']))
            data_list_province_confirmedCount.append(tuple(["null", 0]))
            data_list_province_curedCount.append(tuple(["null", 0]))
            data_list_province_deadCount.append(tuple(["null", 0]))
            c = (
                Map(init_opts=opts.InitOpts(chart_id='map'))
                    .add("累计确诊人数", data_pair=data_list_province_confirmedCount, maptype="world", is_map_symbol_show=False,
                         name_map=name_map)
                    .add("累计治愈人数", data_pair=data_list_province_curedCount, maptype="world", is_map_symbol_show=False,
                         name_map=name_map)
                    .add("累计死亡人数", data_pair=data_list_province_deadCount, maptype="world", is_map_symbol_show=False,
                         name_map=name_map)
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title='世界累计疫情地图',
                                              subtitle="日期：{}".format(search_time)),
                    visualmap_opts=opts.VisualMapOpts(max_=world['province_confirmedCount'].max() / 10,
                                                      is_piecewise=False,
                                                      pieces=[
                                                          {"max": 0, "label": "0人", "color": "#FFFFFF"},
                                                          {"min": 1, "max": 9, "label": "1-9人", "color": "#FFEBCD"},
                                                          {"min": 10, "max": 99, "label": "10-99人", "color": "#FFA07A"},
                                                          {"min": 100, "max": 999, "label": "100-999人", "color": "#FF7F50"},
                                                          {"min": 1000, "max": 9999, "label": "1000-9999人",
                                                           "color": "#CD4F39"},
                                                          {'min': 10000, "max": 99999, "label": "10000-100000人",
                                                           "color": "#CD3333"},
                                                          {'min': 100000, "label": ">100000人", "color": "#8B0000"}
                                                      ])
                ),

            )
        except Exception as e:
            c = (
                Map(init_opts=opts.InitOpts(chart_id='map'))
                    .add("累计确诊人数", [list(z) for z in zip(Faker.provinces, Faker.values())],maptype="world",is_map_symbol_show=False,name_map=name_map)
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                    title_opts=opts.TitleOpts(title='世界累计疫情地图',
                                              subtitle="日期：{}".format(search_time)),
                    visualmap_opts=opts.VisualMapOpts()
                ),
            )
            print(e)
        return c

    @staticmethod
    def draw_statistical_line(date_list,confirm_list,dead_list,heal_list) -> Line:
        line = Line()
        line.set_global_opts(title_opts=opts.TitleOpts(title="疫情曲线"),toolbox_opts=opts.ToolboxOpts(is_show=True),)
        line.add_xaxis(date_list)
        line.add_yaxis('确诊人数', confirm_list)
        line.add_yaxis('死亡人数', dead_list)
        line.add_yaxis('治愈人数', heal_list)
        line.render("./web/statistical_line.html")
        return line

    @staticmethod
    def draw_predict_line(date_list, confirm_list, dead_list, heal_list) -> Line:
        line = Line()
        line.set_global_opts(title_opts=opts.TitleOpts(title="疫情曲线"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),datazoom_opts=opts.DataZoomOpts(range_start=0, range_end=10, ))
        line.add_xaxis(date_list)
        line.add_yaxis('预测确诊人数', confirm_list)
        line.add_yaxis('预测死亡人数', dead_list)
        line.add_yaxis('预测治愈人数', heal_list)
        line.render("./web/predict_line.html")
        return line




if __name__ == '__main__':
    dict= {"continentName": "亚洲", "continentEnglishName": "Asia", "countryName": "中国", "countryEnglishName": "China",
     "provinceName": "上海市", "provinceEnglishName": "Shanghai", "province_confirmedCount": "11111",
     "province_suspectedCount": "1111", "province_curedCount": "111", "province_deadCount": "11",
     "updateTime": "2019-01-01 0:00", "cityName": "嘉定区", "cityEnglishName": "Jiading District",
     "city_confirmedCount": "5", "city_suspectedCount": "4", "city_curedCount": "3", "city_deadCount": "0","city_zipCode":"2323"
}
    data = pd.DataFrame(dict,index=[0])  # data需要是字典格式
    data.to_csv('.\\data\\dataFile.csv', mode='a', index=None, header=False,encoding="utf_8",)

    # draft.to_csv('.\ChinaInfoByCityName.csv', index=None, encoding='gbk')  # china没有按照时间排序

