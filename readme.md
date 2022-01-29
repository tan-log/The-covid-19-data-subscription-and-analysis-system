# COVID-19数据发布、订阅及分析预测

## 开发/运行环境

- **开发环境**：Windows10

- **开发软件**：PyCharm 2020.3.2 (Community Edition)内部版本号 #PC-203.6682.179

- **开发语言**：python3

- **引用库**：PyQt5、time、sys、datetime、pyecharts、pandas、numpy、statsmodels

## 项目要求

对搜集到的疫情历史数据进行分析研究，了解疫情与疫情的发展态势。

## 界面设计

![image-20211225212015749](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system/blob/main/img/image-20211225212015749.png)
![image-20211225212032310](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system/blob/main/img/image-20211225212032310.png)

## 操作说明

- **单击**分析进入数据分析界面。

  ![image-20211225212351539](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system\img\image-20211225212351539.png)

- 左上方选择**导入**、**导出**疫情数据。
  ![image-20211225212450860](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system\img\image-20211225212450860.png)

- 中上方可选择查看数据信息（地区名,、起始时间、 结束时间）。

  ![image-20211225212534075](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system\img\image-20211225212534075.png)

- **单击**右方刷新按钮，可以在下方列表筛选的疫情数据。
  ![image-20211225212733536](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system\img\image-20211225212733536.png)

- **单击**疫情地区图按钮，可以显示所选结束时间的疫情地图。
  ![image-20211225213107722](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system\img\image-20211225213107722.png)![image-20211225213010255](.\img\image-20211225213010255.png)

- **单击**右侧分析按钮，可以显示疫情累计、新增和预测数据。

  ![image-20211225213133846](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system\img\image-20211225213133846.png)
  ![image-20211225213306269](https://github.com/tan-log/The-covid-19-data-subscription-and-analysis-system\img\image-20211225213306269.png)

## 系统实现

### 基本数据处理

包括：**选取子集，缺失数据处理、数据格式转换、异常值数据处理**等。

#### 1.国家每日疫情数据选取

- 选取某国家疫情数据
- 对于更新时间(updateTime)列，需将其转换为日期类型并提取出年-月-日，并查看处理结果。
- 因数据每天按小时更新，一天之内有很多重复数据，去重并只保留一天之内最新的数据。

```python
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

```

#### 2.省每日疫情数据选取

- 选取某省疫情数据
- 对于更新时间(updateTime)列，需将其转换为日期类型并提取出年-月-日，并查看处理结果。
- 因数据每天按小时更新，一天之内有很多重复数据，去重并只保留一天之内最新的数据。

```python
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
            
```

#### 3.城市每日疫情数据选取

- 选取某城市疫情数据
- 对于更新时间(updateTime)列，需将其转换为日期类型并提取出年-月-日，并查看处理结果。
- 因数据每天按小时更新，一天之内有很多重复数据，去重并只保留一天之内最新的数据。

```python
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
```

#### 4.数据插值

有的国家/省/城市不是每日都上报的，如果某日只统计上报的那些国家/省/城市，那些存在患者却不上报的国家/省/城市就会被忽略，数据就失真了，需要补全所有国家/省/城市每日的数据，即便不上报的国家/省/城市也要每日记录数据统计，所以要进行插值处理补全部分数据。

```python
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
        （略）
        # 所有省份插值，日期格式化
		（略）
        # 去重
        interpolatingDailyInfo = interpolatingDailyInfo.drop_duplicates(subset=['provinceName', 'updateTime'],
                                                                        keep='first')
```



## 数据分析及可视化

#### 1.累计确诊/疑似/治愈/死亡情况

以国家累计确诊为例，

- 要获得全国累计情况随时间变化趋势，首先需要整合每日全国累计确诊情况做成date_confirmed
- 要整合每日全国累计确诊情况，首先得提取每个省份每日当天最新累计确诊人数，省份数据求和后形成dataframe，for循环拼接到date_confirmed中

```python
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
```

#### 2.新增确诊/疑似/治愈/死亡情况随时间变化情况

以国家为例，新增确诊/治愈/死亡的数据需要对国家每日各省数据进行运算，每省每日累计确诊/治愈/死亡的数据进行diff差值运算

#### 3.累计确诊/疑似/治愈/死亡预测

使用**指数平滑法**进行简单预测

##### 指数平滑法概念

 指数平滑法是布朗(Robert G..Brown)所提出，布朗(Robert G..Brown)认为时间序列的态势具有稳定性或规则性，所以时间序列可被合理地顺势推延；他认为最近的过去态势，在某种程度上会持续到最近的未来，所以将较大的权数放在最近的资料。

指数平滑法是在移动平均法基础上发展起来的一种时间序列分析预测法，它是通过计算指数平滑值，配合一定的时间序列预测模型对现象的未来进行。其原理是任一期的指数平滑值都是本期实际观察值与前一期指数平滑值的加权平均。

##### 指数平滑法方法应用

指数平滑法的基本公式：$St=a*yt+(1-a)*St-1$ 式中，

- St--时间t的平滑值；
- yt--时间t的实际值；
- St-1--时间t-1的平滑值；
- a--平滑常数，其取值范围为[0,1]

据平滑次数不同，指数平滑法分为：一次指数平滑法、二次指数平滑和三次指数平滑法等。

```python
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
```
