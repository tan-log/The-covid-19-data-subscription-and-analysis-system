# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import json
import tkinter as tk
from tkinter import filedialog
import pandas as pd
ip = '47.100.197.182'
port = 1883
topic = "/python/mqtt"
client_id = f'python-mqtt-publish'#f'python-mqtt-{random.randint(0, 1000)}'
continent_list=["亚洲","非洲","欧洲","大洋洲","北美洲","南美洲"]
continent_list_E={
    "亚洲":"Asia",
    "非洲":"Africa",
    "欧洲":"Europe",
    "大洋洲":"Oceania",
    "北美洲":"North America",
    "南美洲":"South America",
}
country_list=[ "赞比亚共和国" ,  "韩国" ,  "伊拉克" ,  "圣其茨和尼维斯" ,  "海地" ,  "爱沙尼亚" ,  "突尼斯" ,  "阿塞拜疆" ,  "喀麦隆" ,  "苏里南" ,  "新西兰" ,  "卡塔尔" ,  "拉脱维亚" ,  "圣多美和普林西比" ,  "瑞典" ,  "圣文森特和格林纳丁斯" ,  "不丹" ,  "澳大利亚" ,  "巴布亚新几内亚" ,  "北马里亚纳群岛联邦" ,  "北马其顿" ,  "科威特" ,  "乌兹别克斯坦" ,  "博茨瓦纳" ,  "南苏丹" ,  "挪威" ,  "摩纳哥" ,  "哈萨克斯坦" ,  "荷兰加勒比地区" ,  "新喀里多尼亚" ,  "巴基斯坦" ,  "贝宁" ,  "马来西亚" ,  "钻石公主号邮轮" ,  "俄罗斯" ,  "塞浦路斯" ,  "加纳" ,  "萨尔瓦多" ,  "厄立特里亚" ,  "格陵兰" ,  "梵蒂冈" ,  "斐济" ,  "土耳其" ,  "意大利" ,  "英国（含北爱尔兰）" ,  "圣皮埃尔和密克隆群岛" ,  "巴拿马" ,  "索马里" ,  "保加利亚" ,  "也门共和国" ,  "特克斯和凯科斯群岛" ,  "希腊" ,  "黎巴嫩" ,  "卢旺达" ,  "塞尔维亚" ,  "西班牙" ,  "塞内加尔" ,  "多米尼加" ,  "巴拉圭" ,  "摩尔多瓦" ,  "约旦" ,  "巴巴多斯" ,  "肯尼亚" ,  "瑞士" ,  "苏丹" ,  "以色列" ,  "直布罗陀" ,  "印度" ,  "克罗地亚" ,  "圣马力诺" ,  "尼日尔" ,  "阿曼" ,  "库拉索岛" ,  "冰岛" ,  "马达加斯加" ,  "芬兰" ,  "法罗群岛" ,  "尼泊尔" ,  "中非共和国" ,  "法属波利尼西亚" ,  "利比亚" ,  "刚果（布）" ,  "阿尔巴尼亚" ,  "马拉维" ,  "吉尔吉斯斯坦" ,  "关岛" ,  "利比里亚" ,  "马耳他" ,  "法属圭亚那" ,  "塞拉利昂" ,  "黑山" ,  "泽西岛" ,  "摩洛哥" ,  "斯威士兰" ,  "斯里兰卡" ,  "荷兰" ,  "越南" ,  "波黑" ,  "莫桑比克" ,  "阿联酋" ,  "法国" ,  "奥地利" ,  "日本" ,  "葡萄牙" ,  "丹麦" ,  "波兰" ,  "尼加拉瓜" ,  "墨西哥" ,  "亚美尼亚" ,  "叙利亚" ,  "毛里塔尼亚" ,  "乌干达" ,  "南非" ,  "蒙古" ,  "巴西" ,  "根西岛" ,  "新加坡" ,  "荷属圣马丁" ,  "捷克" ,  "埃塞俄比亚" ,  "阿根廷" ,  "圣巴泰勒米岛" ,  "厄瓜多尔" ,  "至尊公主邮轮" ,  "科索沃" ,  "坦桑尼亚" ,  "哥斯达黎加" ,  "安哥拉" ,  "马恩岛" ,  "罗马尼亚" ,  "巴哈马" ,  "柬埔寨" ,  "秘鲁" ,  "马尔代夫" ,  "北爱尔兰" ,  "洪都拉斯" ,  "巴勒斯坦" ,  "多哥" ,  "圣卢西亚" ,  "波多黎各" ,  "安圭拉" ,  "格鲁吉亚" ,  "布基纳法索" ,  "伯利兹" ,  "印度尼西亚" ,  "留尼旺" ,  "立陶宛" ,  "危地马拉" ,  "英属维尔京群岛" ,  "东帝汶" ,  "圣巴泰勒米" ,  "斯洛文尼亚" ,  "安提瓜和巴布达" ,  "马提尼克" ,  "中国" ,  "百慕大" ,  "瓜德罗普岛" ,  "阿富汗" ,  "刚果（金）" ,  "尼日利亚" ,  "几内亚" ,  "爱尔兰" ,  "土库曼斯坦" ,  "几内亚比绍" ,  "格林那达" ,  "白俄罗斯" ,  "乌拉圭" ,  "加蓬" ,  "美属维尔京群岛" ,  "沙特阿拉伯" ,  "大不列颠及北爱尔兰联合王国" ,  "列支敦士登" ,  "科摩罗" ,  "津巴布韦" ,  "圭亚那" ,  "佛得角" ,  "安道尔" ,  "莱索托" ,  "蒙特塞拉特" ,  "留尼汪" ,  "卢森堡" ,  "塞舌尔" ,  "孟加拉国" ,  "赤道几内亚" ,  "马里" ,  "斯洛伐克" ,  "菲律宾" ,  "玻利维亚" ,  "加拿大" ,  "伊朗" ,  "阿鲁巴" ,  "美国" ,  "匈牙利" ,  "牙买加" ,  "开曼群岛" ,  "缅甸" ,  "德国" ,  "古巴" ,  "哥伦比亚" ,  "塔吉克斯坦" ,  "乍得" ,  "吉布提" ,  "阿尔及利亚" ,  "比利时" ,  "智利" ,  "埃及" ,  "文莱" ,  "泰国" ,  "马约特" ,  "福克兰群岛" ,  "布隆迪共和国" ,  "特立尼达和多巴哥" ,  "纳米比亚" ,  "巴林" ,  "多米尼克" ,  "冈比亚" ,  "委内瑞拉" ,  "英国" ,  "老挝" ,  "乌克兰" ,  "毛里求斯" ,  "科特迪瓦" ,  "圣马丁岛"]
country_list_E={
"伯利兹":"Belize" ,  "摩洛哥":"Morocco" ,  "毛里求斯":"Mauritius" ,  "委内瑞拉":"Venezuela" ,  "列支敦士登":"Liechtenstein" ,  "肯尼亚":"Kenya" ,  "印度":"India" ,  "塞浦路斯":"Cyprus" ,  "圣巴泰勒米岛":"nan" ,  "马提尼克":"Martinique" ,  "阿尔巴尼亚":"Albania" ,  "马恩岛":"Isle of Man" ,  "卡塔尔":"Qatar" ,  "古巴":"Cuba" ,  "尼日利亚":"Nigeria" ,  "约旦":"Jordan" ,  "坦桑尼亚":"Tanzania" ,  "法属波利尼西亚":"French Polynesia" ,  "洪都拉斯":"Honduras" ,  "阿鲁巴":"nan" ,  "利比里亚":"Liberia" ,  "马约特":"nan" ,  "特立尼达和多巴哥":"Trinidad and Tobago" ,  "法国":"France" ,  "哥伦比亚":"Colombia" ,  "美属维尔京群岛":"nan" ,  "安哥拉":"Angola" ,  "莫桑比克":"Mozambique" ,  "瓜德罗普岛":"nan" ,  "安圭拉":"nan" ,  "斯洛伐克":"Slovakia" ,  "阿富汗":"Afghanistan" ,  "利比亚":"Libya" ,  "格林那达":"nan" ,  "克罗地亚":"Croatia" ,  "马达加斯加":"Madagascar" ,  "乌克兰":"Ukraine" ,  "波黑":"Bosnia and Herzegovina" ,  "澳大利亚":"Australia" ,  "马来西亚":"Malaysia" ,  "摩纳哥":"Monaco" ,  "至尊公主邮轮":"Grand Princess" ,  "苏里南":"Suriname" ,  "英国（含北爱尔兰）":"United Kingdom" ,  "叙利亚":"Syria" ,  "塞舌尔":"Seychelles" ,  "埃塞俄比亚":"Ethiopia" ,  "北马其顿":"North Macedonia" ,  "科摩罗":"nan" ,  "乌兹别克斯坦":"Uzbekistan" ,  "墨西哥":"Mexico" ,  "留尼旺":"Reunion" ,  "伊朗":"Iran" ,  "芬兰":"Finland" ,  "黑山":"nan" ,  "意大利":"Italy" ,  "喀麦隆":"Cameroon" ,  "梵蒂冈":"Status Civitatis Vaticanae" ,  "赞比亚共和国":"nan" ,  "巴林":"Bahrain" ,  "巴基斯坦":"Pakistan" ,  "苏丹":"Sudan" ,  "牙买加":"Jamaica" ,  "新加坡":"Singapore" ,  "刚果（金）":"Democratic Republic of the Congo" ,  "沙特阿拉伯":"Saudi Arabia" ,  "尼加拉瓜":"Nicaragua" ,  "马拉维":"Malawi" ,  "留尼汪":"Reunion Island" ,  "厄瓜多尔":"Ecuador" ,  "阿尔及利亚":"Algeria" ,  "吉布提":"Djibouti" ,  "贝宁":"Benin" ,  "圣马丁岛":"Sint Maarten" ,  "格陵兰":"nan" ,  "福克兰群岛":"nan" ,  "刚果（布）":"nan" ,  "越南":"Vietnam" ,  "文莱":"Brunei" ,  "以色列":"Israel" ,  "百慕大":"nan" ,  "西班牙":"Spain" ,  "立陶宛":"Lithuania" ,  "津巴布韦":"Zimbabwe" ,  "塞内加尔":"Senegal" ,  "土库曼斯坦":"Turkmenistan" ,  "泰国":"Thailand" ,  "老挝":"Laos" ,  "马里":"Mali" ,  "新喀里多尼亚":"nan" ,  "巴西":"Brazil" ,  "几内亚比绍":"nan" ,  "尼日尔":"Niger" ,  "巴布亚新几内亚":"Papua New Cuinea" ,  "德国":"Germany" ,  "爱尔兰":"Ireland" ,  "巴拿马":"Panama" ,  "南苏丹":"nan" ,  "荷属圣马丁":"nan" ,  "格鲁吉亚":"Georgia" ,  "科索沃":"nan" ,  "海地":"Haiti" ,  "亚美尼亚":"Armenia" ,  "南非":"South Africa" ,  "圣巴泰勒米":"Saint Barthelemy" ,  "东帝汶":"nan" ,  "斯里兰卡":"SriLanka" ,  "蒙古":"Mongolia" ,  "瑞典":"Sweden" ,  "伊拉克":"Iraq" ,  "阿联酋":"United Arab Emirates" ,  "北爱尔兰":"Northern Ireland" ,  "厄立特里亚":"nan" ,  "卢旺达":"Republic of Rwanda" ,  "佛得角":"nan" ,  "韩国":"Korea" ,  "也门共和国":"nan" ,  "开曼群岛":"Cayman Is" ,  "葡萄牙":"Portugal" ,  "拉脱维亚":"Latvia" ,  "圣其茨和尼维斯":"nan" ,  "阿塞拜疆":"Azerbaijan" ,  "关岛":"Guam" ,  "博茨瓦纳":"Botswana" ,  "圣马力诺":"San Marino" ,  "塔吉克斯坦":"Tajikstan" ,  "比利时":"Belgium" ,  "巴巴多斯":"Barbados" ,  "加拿大":"Canada" ,  "钻石公主号邮轮":"Diamond Princess Cruise Ship" ,  "多哥":"Togo" ,  "安道尔":"Andorra" ,  "圣文森特和格林纳丁斯":"Saint Vincent and the Grenadines" ,  "新西兰":"New Zealand" ,  "多米尼加":"Dominican Republic" ,  "捷克":"Czech Republic" ,  "中国":"China" ,  "萨尔瓦多":"El Salvador" ,  "英属维尔京群岛":"nan" ,  "加纳":"Ghana" ,  "俄罗斯":"Russia" ,  "希腊":"Greece" ,  "中非共和国":"Central African Republic" ,  "秘鲁":"Peru" ,  "菲律宾":"Philippines" ,  "泽西岛":"Bailiwick of Jersey" ,  "丹麦":"Denmark" ,  "乌干达":"Uganda" ,  "荷兰加勒比地区":"nan" ,  "根西岛":"Guernsey" ,  "马耳他":"Malta" ,  "美国":"United States of America" ,  "索马里":"Somali" ,  "不丹":"Kingdom of Bhutan" ,  "莱索托":"Lesotho"  ,  "波多黎各":"Puerto Rico" ,  "冈比亚":"Gambia" ,  "冰岛":"Iceland" ,  "瑞士":"Switzerland" ,  "巴布亚新几内亚":"Papua New Guinea" ,  "巴哈马":"Bahamas" ,  "挪威":"Norway" ,  "保加利亚":"Bulgaria" ,  "奥地利":"Austria" ,  "斯威士兰":"Swaziland" ,  "智利":"Chile" ,  "赤道几内亚":"The Republic of Equatorial Guinea" ,  "蒙特塞拉特":"nan" ,  "法属圭亚那":"French Guiana" ,  "乍得":"Chad" ,  "荷兰":"Netherlands" ,  "尼泊尔":"Nepal" ,  "几内亚":"Guinea" ,  "布隆迪共和国":"nan" ,  "卢森堡":"Luxembourg" ,  "埃及":"Egypt" ,  "哈萨克斯坦":"Kazakhstan" ,  "哥斯达黎加":"Costa Rica" ,  "巴勒斯坦":"Palestine" ,  "摩尔多瓦":"Moldova" ,  "巴拉圭":"Paraguay" ,  "毛里塔尼亚":"The Islamic Republic of Mauritania" ,  "圣多美和普林西比":"Sao Tome and Principe" ,  "黎巴嫩":"Lebanon" ,  "马尔代夫":"Maldives" ,  "罗马尼亚":"Romania" ,  "印度尼西亚":"Indonesia" ,  "乌拉圭":"Uruguay" ,  "土耳其":"Turkey" ,  "危地马拉":"Guatemala" ,  "柬埔寨":"Kampuchea (Cambodia )" ,  "安提瓜和巴布达":"Antigua and Barbuda" ,  "英国":"United Kingdom" ,  "北马里亚纳群岛联邦":"nan" ,  "大不列颠及北爱尔兰联合王国":"United Kingdom of Great Britain and Ireland" ,  "匈牙利":"Hungary" ,  "纳米比亚":"Namibia" ,  "圣皮埃尔和密克隆群岛":"nan" ,  "波兰":"Poland" ,  "爱沙尼亚":"Estonia" ,  "特克斯和凯科斯群岛":"nan" ,  "阿根廷":"Argentina" ,  "塞拉利昂":"Sierra Leone" ,  "塞尔维亚":"Republic of Serbia" ,  "科威特":"Kuwait" ,  "日本":"Japan" ,  "斐济":"Fiji" ,  "科特迪瓦":"Ivory Coast" ,  "法罗群岛":"Faroe" ,  "布基纳法索":"Burkina Faso" ,  "阿曼":"Oman" ,  "白俄罗斯":"Belarus" ,  "库拉索岛":"nan" ,  "吉尔吉斯斯坦":"nan" ,  "圭亚那":"Guyana" ,  "圣卢西亚":"St.Lucia" ,  "加蓬":"Gabon" ,  "缅甸":"Burma" ,  "多米尼克":"nan" ,  "斯洛文尼亚":"Slovenia" ,  "直布罗陀":"Gibraltar" ,  "玻利维亚":"Bolivia" ,  "孟加拉国":"Bangladesh" ,  "突尼斯":"Tunisia"
}
province_list=["丹麦" ,  "马恩岛" ,  "北马里亚纳群岛联邦" ,  "关岛" ,  "尼泊尔" ,  "直布罗陀" ,  "美国" ,  "刚果（布）" ,  "爱沙尼亚" ,  "荷兰加勒比地区" ,  "马耳他" ,  "厄立特里亚" ,  "陕西省" ,  "乌干达" ,  "亚美尼亚" ,  "马达加斯加" ,  "几内亚比绍" ,  "老挝" ,  "留尼汪" ,  "广东省" ,  "吉布提" ,  "斯洛伐克" ,  "钻石公主号邮轮" ,  "瓜德罗普岛" ,  "保加利亚" ,  "江西省" ,  "山西省" ,  "布隆迪共和国" ,  "坦桑尼亚" ,  "安徽省" ,  "波兰" ,  "阿尔巴尼亚" ,  "厄瓜多尔" ,  "韩国" ,  "甘肃省" ,  "加纳" ,  "百慕大" ,  "叙利亚" ,  "刚果（金）" ,  "湖南省" ,  "肯尼亚" ,  "南非" ,  "阿根廷" ,  "开曼群岛" ,  "毛里塔尼亚" ,  "巴哈马" ,  "科特迪瓦" ,  "四川省" ,  "埃及" ,  "阿联酋" ,  "留尼旺" ,  "印度尼西亚" ,  "葡萄牙" ,  "山东省" ,  "尼加拉瓜" ,  "不丹" ,  "奥地利" ,  "新疆维吾尔自治区" ,  "美属维尔京群岛" ,  "圣文森特和格林纳丁斯" ,  "尼日尔" ,  "海地" ,  "突尼斯" ,  "卡塔尔" ,  "新加坡" ,  "梵蒂冈" ,  "冰岛" ,  "古巴" ,  "索马里" ,  "波多黎各" ,  "乌拉圭" ,  "西班牙" ,  "格陵兰" ,  "赞比亚共和国" ,  "德国" ,  "土库曼斯坦" ,  "塞舌尔" ,  "贵州省" ,  "格鲁吉亚" ,  "阿鲁巴" ,  "东帝汶" ,  "特克斯和凯科斯群岛" ,  "科摩罗" ,  "西藏自治区" ,  "乌克兰" ,  "利比里亚" ,  "马约特" ,  "利比亚" ,  "文莱" ,  "尼日利亚" ,  "圣巴泰勒米岛" ,  "加拿大" ,  "中国" ,  "澳门" ,  "泽西岛" ,  "摩洛哥" ,  "冈比亚" ,  "蒙特塞拉特" ,  "荷兰" ,  "北爱尔兰" ,  "根西岛" ,  "多米尼克" ,  "比利时" ,  "莫桑比克" ,  "荷属圣马丁" ,  "天津市" ,  "马来西亚" ,  "赤道几内亚" ,  "辽宁省" ,  "黎巴嫩" ,  "佛得角" ,  "多米尼加" ,  "挪威" ,  "印度" ,  "法属波利尼西亚" ,  "安圭拉" ,  "大不列颠及北爱尔兰联合王国" ,  "摩尔多瓦" ,  "广西壮族自治区" ,  "也门共和国" ,  "塔吉克斯坦" ,  "日本" ,  "卢森堡" ,  "哥斯达黎加" ,  "斯里兰卡" ,  "河北省" ,  "博茨瓦纳" ,  "列支敦士登" ,  "圣巴泰勒米" ,  "伊朗" ,  "法罗群岛" ,  "乌兹别克斯坦" ,  "巴拉圭" ,  "英国" ,  "约旦" ,  "纳米比亚" ,  "智利" ,  "台湾" ,  "香港" ,  "海南省" ,  "缅甸" ,  "哥伦比亚" ,  "苏里南" ,  "至尊公主邮轮" ,  "福建省" ,  "斯威士兰" ,  "北马其顿" ,  "巴林" ,  "摩纳哥" ,  "圣卢西亚" ,  "阿塞拜疆" ,  "河南省" ,  "瑞士" ,  "马拉维" ,  "菲律宾" ,  "沙特阿拉伯" ,  "浙江省" ,  "圭亚那" ,  "中非共和国" ,  "江苏省" ,  "克罗地亚" ,  "安提瓜和巴布达" ,  "罗马尼亚" ,  "拉脱维亚" ,  "马提尼克" ,  "南苏丹" ,  "北京市" ,  "津巴布韦" ,  "爱尔兰" ,  "澳大利亚" ,  "塞浦路斯" ,  "秘鲁" ,  "黑山" ,  "加蓬" ,  "吉林省" ,  "卢旺达" ,  "重庆市" ,  "云南省" ,  "几内亚" ,  "墨西哥" ,  "内蒙古自治区" ,  "巴基斯坦" ,  "圣皮埃尔和密克隆群岛" ,  "立陶宛" ,  "苏丹" ,  "法国" ,  "安道尔" ,  "莱索托" ,  "芬兰" ,  "阿尔及利亚" ,  "危地马拉" ,  "圣多美和普林西比" ,  "多哥" ,  "泰国" ,  "孟加拉国" ,  "福克兰群岛" ,  "希腊" ,  "马尔代夫" ,  "圣马丁岛" ,  "马里" ,  "圣其茨和尼维斯" ,  "阿富汗" ,  "蒙古" ,  "塞尔维亚" ,  "毛里求斯" ,  "捷克" ,  "哈萨克斯坦" ,  "玻利维亚" ,  "圣马力诺" ,  "科威特" ,  "特立尼达和多巴哥" ,  "青海省" ,  "英属维尔京群岛" ,  "安哥拉" ,  "牙买加" ,  "以色列" ,  "越南" ,  "瑞典" ,  "黑龙江省" ,  "俄罗斯" ,  "上海市" ,  "阿曼" ,  "伊拉克" ,  "白俄罗斯" ,  "湖北省" ,  "科索沃" ,  "巴布亚新几内亚" ,  "巴拿马" ,  "巴西" ,  "埃塞俄比亚" ,  "塞内加尔" ,  "新西兰" ,  "格林那达" ,  "吉尔吉斯斯坦" ,  "斯洛文尼亚" ,  "塞拉利昂" ,  "伯利兹" ,  "法属圭亚那" ,  "英国（含北爱尔兰）" ,  "匈牙利" ,  "宁夏回族自治区" ,  "布基纳法索" ,  "喀麦隆" ,  "洪都拉斯" ,  "贝宁" ,  "土耳其" ,  "委内瑞拉" ,  "乍得" ,  "巴勒斯坦" ,  "库拉索岛" ,  "斐济" ,  "波黑" ,  "意大利" ,  "萨尔瓦多" ,  "新喀里多尼亚" ,  "柬埔寨" ,  "巴巴多斯"]
province_list_E={
     "巴哈马":"Bahamas" ,  "塞内加尔":"Senegal" ,  "塔吉克斯坦":"Tajikstan" ,  "阿尔巴尼亚":"Albania" ,  "格陵兰":"nan" ,  "青海省":"Qinghai" ,  "利比里亚":"Liberia" ,  "库拉索岛":"nan" ,  "葡萄牙":"Portugal" ,  "马耳他":"Malta" ,  "罗马尼亚":"Romania" ,  "塞拉利昂":"Sierra Leone" ,  "尼日尔":"Niger" ,  "蒙特塞拉特":"nan" ,  "亚美尼亚":"Armenia" ,  "德国":"Germany" ,  "波黑":"Bosnia and Herzegovina" ,  "斯洛伐克":"Slovakia" ,  "内蒙古自治区":"Neimenggu" ,  "美国":"United States of America" ,  "委内瑞拉":"Venezuela" ,  "至尊公主邮轮":"Grand Princess" ,  "巴林":"Bahrain" ,  "肯尼亚":"Kenya" ,  "东帝汶":"nan" ,  "特克斯和凯科斯群岛":"nan" ,  "圣巴泰勒米岛":"nan" ,  "刚果（布）":"nan" ,  "以色列":"Israel" ,  "钻石公主号邮轮":"Diamond Princess Cruise Ship" ,  "英国":"United Kingdom" ,  "巴基斯坦":"Pakistan" ,  "伊拉克":"Iraq" ,  "北马其顿":"North Macedonia" ,  "阿根廷":"Argentina" ,  "科威特":"Kuwait" ,  "英国（含北爱尔兰）":"United Kingdom" ,  "斯里兰卡":"SriLanka" ,  "圣皮埃尔和密克隆群岛":"nan" ,  "也门共和国":"nan" ,  "江苏省":"Jiangsu" ,  "波兰":"Poland" ,  "上海市":"Shanghai" ,  "博茨瓦纳":"Botswana" ,  "马拉维":"Malawi" ,  "日本":"Japan" ,  "多米尼加":"Dominican Republic" ,  "香港":"Hongkong" ,  "江西省":"Jiangxi" ,  "大不列颠及北爱尔兰联合王国":"United Kingdom of Great Britain and Ireland" ,  "斐济":"Fiji" ,  "拉脱维亚":"Latvia" ,  "塞舌尔":"Seychelles" ,  "马来西亚":"Malaysia" ,  "吉布提":"Djibouti" ,  "希腊":"Greece" ,  "台湾":"Taiwan" ,  "英属维尔京群岛":"nan" ,  "安徽省":"Anhui" ,  "摩洛哥":"Morocco" ,  "苏丹":"Sudan" ,  "伊朗":"Iran" ,  "浙江省":"Zhejiang" ,  "澳门":"Macao" ,  "西藏自治区":"Xizang" ,  "重庆市":"Chongqing" ,  "赞比亚共和国":"nan" ,  "瑞士":"Switzerland" ,  "加蓬":"Gabon" ,  "比利时":"Belgium" ,  "瓜德罗普岛":"nan" ,  "印度尼西亚":"Indonesia" ,  "新西兰":"New Zealand" ,  "北爱尔兰":"Northern Ireland" ,  "加拿大":"Canada" ,  "荷属圣马丁":"nan" ,  "利比亚":"Libya" ,  "克罗地亚":"Croatia" ,  "巴布亚新几内亚":"Papua New Guinea" ,  "安哥拉":"Angola" ,  "丹麦":"Denmark" ,  "智利":"Chile" ,  "几内亚比绍":"nan" ,  "纳米比亚":"Namibia" ,  "福建省":"Fujian" ,  "山西省":"Shanxi" ,  "土库曼斯坦":"Turkmenistan" ,  "索马里":"Somali" ,  "黎巴嫩":"Lebanon" ,  "广东省":"Guangdong" ,  "圣卢西亚":"St.Lucia" ,  "留尼汪":"Reunion Island" ,  "沙特阿拉伯":"Saudi Arabia" ,  "乌兹别克斯坦":"Uzbekistan" ,  "白俄罗斯":"Belarus" ,  "圣多美和普林西比":"Sao Tome and Principe" ,  "刚果（金）":"Democratic Republic of the Congo" ,  "坦桑尼亚":"Tanzania" ,  "海地":"Haiti" ,  "泽西岛":"Bailiwick of Jersey" ,  "多米尼克":"nan" ,  "荷兰":"Netherlands" ,  "中国":"China" ,  "科索沃":"nan" ,  "莫桑比克":"Mozambique" ,  "云南省":"Yunnan" ,  "印度":"India" ,  "危地马拉":"Guatemala" ,  "巴勒斯坦":"Palestine" ,  "意大利":"Italy" ,  "瑞典":"Sweden" ,  "安圭拉":"nan" ,  "保加利亚":"Bulgaria" ,  "香港":"Hong Kong" ,  "新疆维吾尔自治区":"Xinjiang" ,  "乌干达":"Uganda" ,  "黑山":"nan" ,  "马恩岛":"Isle of Man" ,  "老挝":"Laos" ,  "天津市":"Tianjin" ,  "厄瓜多尔":"Ecuador" ,  "阿曼":"Oman" ,  "吉尔吉斯斯坦":"nan" ,  "北马里亚纳群岛联邦":"nan" ,  "乍得":"Chad" ,  "立陶宛":"Lithuania" ,  "巴拿马":"Panama" ,  "特立尼达和多巴哥":"Trinidad and Tobago" ,  "陕西省":"Shaanxi" ,  "留尼旺":"Reunion" ,  "关岛":"Guam" ,  "洪都拉斯":"Honduras" ,  "毛里塔尼亚":"The Islamic Republic of Mauritania" ,  "海南省":"Hainan" ,  "多哥":"Togo" ,  "蒙古":"Mongolia" ,  "伯利兹":"Belize" ,  "冈比亚":"Gambia" ,  "辽宁省":"Liaoning" ,  "阿联酋":"United Arab Emirates" ,  "摩尔多瓦":"Moldova" ,  "马约特":"nan" ,  "韩国":"Korea" ,  "法属圭亚那":"French Guiana" ,  "吉林省":"Jilin" ,  "突尼斯":"Tunisia" ,  "柬埔寨":"Kampuchea (Cambodia )" ,  "埃塞俄比亚":"Ethiopia" ,  "尼加拉瓜":"Nicaragua" ,  "河北省":"Hebei" ,  "芬兰":"Finland" ,  "几内亚":"Guinea" ,  "马提尼克":"Martinique" ,  "文莱":"Brunei" ,  "河南省":"Henan" ,  "约旦":"Jordan" ,  "巴西":"Brazil" ,  "法属波利尼西亚":"French Polynesia" ,  "贝宁":"Benin" ,  "巴拉圭":"Paraguay" ,  "摩纳哥":"Monaco" ,  "加纳":"Ghana" ,  "梵蒂冈":"Status Civitatis Vaticanae" ,  "乌克兰":"Ukraine" ,  "圣马丁岛":"Sint Maarten" ,  "冰岛":"Iceland" ,  "卡塔尔":"Qatar" ,  "奥地利":"Austria" ,  "卢旺达":"Republic of Rwanda" ,  "荷兰加勒比地区":"nan" ,  "南苏丹":"nan" ,  "斯威士兰":"Swaziland" ,  "四川省":"Sichuan" ,  "越南":"Vietnam" ,  "安提瓜和巴布达":"Antigua and Barbuda" ,  "马尔代夫":"Maldives" ,  "科摩罗":"nan" ,  "哥斯达黎加":"Costa Rica" ,  "不丹":"Kingdom of Bhutan" ,  "新喀里多尼亚":"nan" ,  "山东省":"Shandong" ,  "泰国":"Thailand" ,  "赤道几内亚":"The Republic of Equatorial Guinea" ,  "秘鲁":"Peru" ,  "牙买加":"Jamaica" ,  "墨西哥":"Mexico" ,  "卢森堡":"Luxembourg" ,  "圣巴泰勒米":"Saint Barthelemy" ,  "埃及":"Egypt" ,  "湖南省":"Hunan" ,  "圭亚那":"Guyana" ,  "南非":"South Africa" ,  "格林那达":"nan" ,  "土耳其":"Turkey" ,  "圣马力诺":"San Marino" ,  "菲律宾":"Philippines" ,  "俄罗斯":"Russia" ,  "新加坡":"Singapore" ,  "开曼群岛":"Cayman Is" ,  "宁夏回族自治区":"Ningxia" ,  "美属维尔京群岛":"nan" ,  "布基纳法索":"Burkina Faso" ,  "巴巴多斯":"Barbados" ,  "津巴布韦":"Zimbabwe" ,  "苏里南":"Suriname" ,  "爱尔兰":"Ireland" ,  "布隆迪共和国":"nan" ,  "佛得角":"nan" ,  "法国":"France" ,  "捷克":"Czech Republic" ,  "安道尔":"Andorra" ,  "马里":"Mali" ,  "百慕大":"nan" ,  "玻利维亚":"Bolivia" ,  "贵州省":"Guizhou" ,  "福克兰群岛":"nan" ,  "挪威":"Norway" ,  "圣文森特和格林纳丁斯":"Saint Vincent and the Grenadines" ,  "叙利亚":"Syria" ,  "西班牙":"Spain" ,  "古巴":"Cuba" ,  "孟加拉国":"Bangladesh" ,  "列支敦士登":"Liechtenstein" ,  "根西岛":"Guernsey" ,  "波多黎各":"Puerto Rico" ,  "塞尔维亚":"Republic of Serbia" ,  "阿尔及利亚":"Algeria" ,  "圣其茨和尼维斯":"nan" ,  "阿鲁巴":"nan" ,  "黑龙江省":"Heilongjiang" ,  "澳门":"Macau" ,  "科特迪瓦":"Ivory Coast" ,  "乌拉圭":"Uruguay" ,  "匈牙利":"Hungary" ,  "阿塞拜疆":"Azerbaijan" ,  "塞浦路斯":"Cyprus" ,  "尼泊尔":"Nepal" ,  "萨尔瓦多":"El Salvador" ,  "马达加斯加":"Madagascar" ,  "直布罗陀":"Gibraltar" ,  "北京市":"Beijing" ,  "阿富汗":"Afghanistan" ,  "巴布亚新几内亚":"Papua New Cuinea" ,  "斯洛文尼亚":"Slovenia" ,  "喀麦隆":"Cameroon" ,  "格鲁吉亚":"Georgia" ,  "哥伦比亚":"Colombia" ,  "尼日利亚":"Nigeria" ,  "中非共和国":"Central African Republic" ,  "广西壮族自治区":"Guangxi" ,  "莱索托":"Lesotho" ,  "哈萨克斯坦":"Kazakhstan" ,  "法罗群岛":"Faroe" ,  "厄立特里亚":"nan" ,  "甘肃省":"Gansu" ,  "湖北省":"Hubei" ,  "澳大利亚":"Australia" ,  "爱沙尼亚":"Estonia" ,  "缅甸":"Burma" ,  "毛里求斯":"Mauritius"
}

city_list=[ "兰州" ,  "普陀区" ,  "潜江" ,  "惠州" ,  "外地来京" ,  "通州区" ,  "酉阳" ,  "南通" ,  "临高县" ,  "眉山" ,  "西城" ,  "亳州" ,  "丰台" ,  "巩义" ,  "曲靖" ,  "安庆" ,  "彭水县" ,  "江门" ,  "璧山区" ,  "涪陵区" ,  "待明确治愈" ,  "门头沟" ,  "郑州" ,  "渝北区" ,  "兵团第九师" ,  "湘西自治州" ,  "崇明区" ,  "甘南" ,  "黔江区" ,  "信阳" ,  "三门峡" ,  "韩城" ,  "秦皇岛" ,  "白城" ,  "松江区" ,  "吉林市" ,  "塔城" ,  "南京" ,  "满洲里" ,  "河东区" ,  "顺义区" ,  "乌鲁木齐" ,  "城口" ,  "杨凌" ,  "通州" ,  "长沙" ,  "保定" ,  "文昌" ,  "未明确地区" ,  "新乡" ,  "梁平区" ,  "不明地区" ,  "鄂州" ,  "兴安盟" ,  "安康" ,  "新乡（含长垣）" ,  "通化" ,  "锡林郭勒盟二连浩特" ,  "宝坻区" ,  "孝感" ,  "焦作" ,  "儋州" ,  "漯河市" ,  "渭南" ,  "两江新区" ,  "呼和浩特" ,  "张家口" ,  "伊春" ,  "娄底" ,  "深圳" ,  "潍坊" ,  "安顺" ,  "呼伦贝尔牙克石市" ,  "龙岩" ,  "阜新" ,  "张掖" ,  "外地来津" ,  "垫江" ,  "南平" ,  "红河" ,  "渝中区" ,  "随州" ,  "宜昌" ,  "保亭" ,  "苏州" ,  "鄂尔多斯" ,  "锡林郭勒盟锡林浩特" ,  "吉林" ,  "开州区" ,  "肇庆" ,  "淮安" ,  "凉山州" ,  "滨海新区" ,  "泸州" ,  "宁东" ,  "襄阳" ,  "怀柔区" ,  "酉阳县" ,  "安阳" ,  "滨州" ,  "浦东新区" ,  "兵团第七师" ,  "密云区" ,  "东城区" ,  "邓州" ,  "杨浦区" ,  "武汉" ,  "待明确" ,  "第八师石河子" ,  "奉节" ,  "乌海市" ,  "外地来粤人员" ,  "石河子" ,  "大同" ,  "洛阳" ,  "湘潭" ,  "吐鲁番" ,  "延边" ,  "梧州" ,  "阜阳" ,  "湛江" ,  "铜仁" ,  "铜川" ,  "第八师石河子市" ,  "岳阳" ,  "景德镇" ,  "监狱系统" ,  "桂林" ,  "第九师" ,  "咸阳" ,  "赣州" ,  "抚顺" ,  "西城区" ,  "厦门" ,  "永城" ,  "宝鸡" ,  "福州" ,  "晋中" ,  "无锡" ,  "兵团第五师五家渠市" ,  "内江" ,  "防城港" ,  "金山区" ,  "外地来京人员" ,  "唐山" ,  "聊城" ,  "鹤壁市" ,  "秀山" ,  "衡水" ,  "漯河" ,  "菏泽" ,  "济宁" ,  "威海" ,  "海北州" ,  "中卫" ,  "南岸区" ,  "宁波" ,  "贵阳" ,  "永州" ,  "朝阳区" ,  "红桥区" ,  "荣昌区" ,  "营口" ,  "辽阳" ,  "毕节" ,  "滁州" ,  "汕头" ,  "待明确地区" ,  "大理" ,  "松原" ,  "nan" ,  "天水" ,  "海淀" ,  "公主岭" ,  "江北区" ,  "门头沟区" ,  "境外输入人员" ,  "昌平区" ,  "大兴区" ,  "临汾市" ,  "黄冈" ,  "荆州" ,  "韶关" ,  "昭通" ,  "万州区" ,  "城口县" ,  "遵义" ,  "合川区" ,  "烟台" ,  "莆田" ,  "佳木斯" ,  "鹤岗" ,  "中山" ,  "佛山" ,  "固原" ,  "兵团第六师五家渠市" ,  "钦州" ,  "定安" ,  "外地来沪人员" ,  "德宏" ,  "成都" ,  "甘孜州" ,  "南宁" ,  "金昌" ,  "普洱" ,  "阿拉善盟" ,  "白银市" ,  "玉溪" ,  "第八师" ,  "怀化" ,  "拉萨" ,  "嘉兴" ,  "四平" ,  "漳州" ,  "柳州" ,  "丰台区" ,  "济南" ,  "石柱" ,  "黑河" ,  "奉节县" ,  "浦东区" ,  "大兴安岭" ,  "乌兰察布" ,  "綦江区" ,  "和平区" ,  "巴中" ,  "长春" ,  "房山区" ,  "澄迈" ,  "承德" ,  "湖州" ,  "梅河口" ,  "江津区" ,  "河北区" ,  "仙桃" ,  "自贡" ,  "晋城" ,  "周口" ,  "宝山区" ,  "庆阳" ,  "雅安" ,  "宿州" ,  "任城监狱" ,  "青浦区" ,  "九龙坡区" ,  "包头市东河区" ,  "河源" ,  "阿克苏地区" ,  "百色" ,  "台州" ,  "三明" ,  "河西区" ,  "芜湖" ,  "巴州" ,  "顺义" ,  "商洛" ,  "朔州市" ,  "铜梁区" ,  "东莞" ,  "石家庄" ,  "五家渠" ,  "大足区" ,  "安阳（含滑县）" ,  "黔西南州" ,  "长治" ,  "楚雄" ,  "高新区" ,  "丽江" ,  "淮南" ,  "通辽" ,  "海口" ,  "汉中" ,  "武清区" ,  "攀枝花" ,  "抚州" ,  "泉州" ,  "邵阳" ,  "咸宁" ,  "宁东管委会" ,  "揭阳" ,  "巫山" ,  "牡丹江" ,  "梅州" ,  "陇南" ,  "宜宾" ,  "锦州" ,  "淮北" ,  "楚雄州" ,  "大兴" ,  "呼和浩特（新城区）" ,  "昌吉州" ,  "太原" ,  "东方市" ,  "丹东" ,  "温州" ,  "怀柔" ,  "外地来穗人员" ,  "南昌" ,  "赤峰市林西县" ,  "大庆" ,  "琼海" ,  "琼海市" ,  "丽江市" ,  "运城" ,  "天门" ,  "石景山区" ,  "珠海" ,  "临高" ,  "盘锦" ,  "达州" ,  "吕梁" ,  "青岛" ,  "武隆区" ,  "伊犁州" ,  "未知" ,  "奉贤区" ,  "固始县" ,  "文山" ,  "衢州" ,  "西双版纳州" ,  "阳泉" ,  "茂名" ,  "本溪" ,  "包头" ,  "南充" ,  "合肥" ,  "淄博市" ,  "津南区" ,  "榆林" ,  "恩施州" ,  "万宁" ,  "新余" ,  "葫芦岛" ,  "南阳" ,  "保山" ,  "德州" ,  "赤峰" ,  "境外来沪" ,  "东丽区" ,  "长垣县" ,  "齐齐哈尔" ,  "沧州" ,  "黄浦区" ,  "云阳" ,  "省十里丰监狱" ,  "四平市" ,  "陵水县" ,  "广安" ,  "虹口区" ,  "绍兴" ,  "省级（湖北输入）" ,  "东城" ,  "铁岭" ,  "常德" ,  "临沧" ,  "金华" ,  "开封" ,  "平凉" ,  "未知地区" ,  "朔州" ,  "清远" ,  "宜春" ,  "昌江" ,  "琼中" ,  "海淀区" ,  "泰安" ,  "乐山" ,  "邯郸市" ,  "西安" ,  "歙县" ,  "平顶山" ,  "北海" ,  "西宁市" ,  "黔东南州" ,  "河源市" ,  "鄂尔多斯鄂托克前旗" ,  "昌平" ,  "宁河区" ,  "资阳" ,  "德宏州" ,  "衡阳" ,  "巫溪县" ,  "石柱县" ,  "白银" ,  "贺州" ,  "赣江新区" ,  "澄迈县" ,  "汕尾" ,  "丰都县" ,  "阿坝州" ,  "锡林郭勒" ,  "三亚" ,  "兵团第四师" ,  "吴忠" ,  "凉山" ,  "长垣" ,  "锡林郭勒盟" ,  "红河州" ,  "通辽市经济开发区" ,  "第六师" ,  "德阳" ,  "乐东" ,  "昌吉" ,  "潼南区" ,  "滑县" ,  "杨浦" ,  "许昌" ,  "扬州" ,  "绵阳" ,  "商丘（含永城）" ,  "金昌市" ,  "潮州" ,  "泰州" ,  "未明确" ,  "东方" ,  "吐鲁番市" ,  "绥化" ,  "十堰" ,  "萍乡" ,  "徐汇区" ,  "荆门" ,  "外地来津人员" ,  "廊坊" ,  "抚顺市" ,  "呼伦贝尔满洲里" ,  "文山州" ,  "鹤壁" ,  "武汉来京人员" ,  "临夏" ,  "黔南州" ,  "巫溪" ,  "喀什地区" ,  "巫山县" ,  "北辰区" ,  "鸡西" ,  "郴州" ,  "丰都" ,  "辽源" ,  "延庆区" ,  "淄博" ,  "兴安盟乌兰浩特" ,  "阳江" ,  "张家界" ,  "赤峰市松山区" ,  "闵行区" ,  "云阳县" ,  "黄山" ,  "垫江县" ,  "徐州" ,  "平凉市" ,  "濮阳" ,  "定西" ,  "连云港" ,  "长宁区" ,  "宿松" ,  "盐城" ,  "兵团第八师石河子市" ,  "蚌埠" ,  "西双版纳" ,  "临汾" ,  "银川" ,  "舟山" ,  "贵港" ,  "第七师" ,  "永川区" ,  "丽水" ,  "六盘水" ,  "铜陵" ,  "上饶" ,  "沈阳" ,  "境外输入" ,  "邢台" ,  "巴南区" ,  "宁德" ,  "商丘" ,  "吉安" ,  "嘉定区" ,  "鄂尔多斯东胜区" ,  "西宁" ,  "大理州" ,  "金山" ,  "南开区" ,  "安阳市" ,  "玉林" ,  "常州" ,  "包头市昆都仑区" ,  "枣庄" ,  "天水市" ,  "巴彦淖尔" ,  "秀山县" ,  "九江" ,  "鹰潭" ,  "外地来沪" ,  "驻马店" ,  "乌海" ,  "石景山" ,  "长寿区" ,  "日照" ,  "哈尔滨" ,  "六安" ,  "来宾" ,  "大连" ,  "池州" ,  "济源" ,  "株洲" ,  "邯郸" ,  "宿迁" ,  "马鞍山" ,  "琼中县" ,  "西青区" ,  "七台河" ,  "黄石" ,  "静安区" ,  "沙坪坝区" ,  "益阳" ,  "陵水" ,  "昆明" ,  "河池" ,  "朝阳" ,  "遂宁" ,  "澳门" ,  "镇江" ,  "忻州" ,  "忠县" ,  "延安" ,  "海东" ,  "广元" ,  "大渡口区" ,  "石嘴山" ,  "万盛经开区" ,  "南阳（含邓州）" ,  "鞍山" ,  "杭州" ,  "临沂" ,  "呼伦贝尔" ,  "双鸭山" ,  "兵团第十二师" ,  "广州" ,  "胡杨河" ,  "阿克苏" ,  "嘉峪关" ,  "呼伦贝尔牙克石" ,  "松江" ,  "神农架林区" ,  "宣城"]
city_list_E={
    "临高":"Lingao County" ,  "大足区":"Dazu District" ,  "衡水":"Hengshui" ,  "怀化":"Huaihua" ,  "铁岭":"Tieling" ,  "广州":"Guangzhou" ,  "烟台":"Yantai" ,  "德州":"Dezhou" ,  "新余":"Xinyu" ,  "西安":"Xi\ an" ,  "宣城":"Xuancheng" ,  "闵行区":"Minhang District" ,  "资阳":"Ziyang" ,  "达州":"Dazhou" ,  "酉阳":"nan" ,  "西城":"nan" ,  "济南":"Jinan" ,  "凉山州":"Liangshan Yi Autonomous Prefecture" ,  "甘南":"Gannan" ,  "黔江区":"Qianjiang Tujia and Miao Autonomous County" ,  "延边":"Yanbian" ,  "石河子":"nan" ,  "广安":"Guang\ an" ,  "清远":"Qingyuan" ,  "开封":"Kaifeng" ,  "德宏州":"Dehong" ,  "河源市":"nan" ,  "长治":"Changzhi" ,  "佳木斯":"Jiamusi" ,  "株洲":"Zhuzhou" ,  "曲靖":"Qujing" ,  "阜阳":"Fuyang" ,  "兰州":"Lanzhou" ,  "南阳":"Nanyang" ,  "延安":"Yan\ an" ,  "陵水县":"nan" ,  "北海":"Beihai" ,  "东城":"nan" ,  "晋中":"Jinzhong" ,  "通州区":"Tongzhou District" ,  "佛山":"Foshan" ,  "赣江新区":"Ganjiang New District" ,  "百色":"Baise" ,  "永州":"Yongzhou" ,  "江北区":"Jiangbei District" ,  "伊春":"Yichun" ,  "南阳（含邓州）":"nan" ,  "沧州":"Cangzhou" ,  "昌平":"nan" ,  "鄂尔多斯东胜区":"nan" ,  "松江":"nan" ,  "铜川":"Tongchuan" ,  "永城":"nan" ,  "雅安":"Ya\ an" ,  "第九师":"nan" ,  "河源":"Heyuan" ,  "牡丹江":"Mudanjiang" ,  "潮州":"Chaozhou" ,  "池州":"Chizhou" ,  "外地来粤人员":"nan" ,  "涪陵区":"Fuling District" ,  "澳门":"Macau" ,  "待明确治愈":"nan" ,  "辽阳":"Liaoyang" ,  "深圳":"Shenzhen" ,  "信阳":"Xinyang" ,  "兵团第十二师":"Xinjiang Production and Construction Corps 12th Division" ,  "成都":"Chengdu" ,  "未知地区":"nan" ,  "太原":"Taiyuan" ,  "公主岭":"Gongzhuling" ,  "榆林":"Yulin" ,  "阿坝州":"Ngawa Tibetan and Qiang Autonomous Prefecture" ,  "无锡":"Wuxi" ,  "东莞":"Dongguan" ,  "湘西自治州":"Xiangxi" ,  "常州":"Changzhou" ,  "红河":"nan" ,  "永川区":"Yongchuan District" ,  "琼中县":"nan" ,  "攀枝花":"Panzhihua" ,  "济宁":"Jining" ,  "淄博":"Zibo" ,  "许昌":"Xuchang" ,  "辽源":"Liaoyuan" ,  "秀山县":"Xiushan Tujia and Miao Autonomous County" ,  "锡林郭勒盟锡林浩特":"nan" ,  "平顶山":"Pingdingshan" ,  "黔东南州":"Qiandongnan" ,  "郑州":"Zhengzhou" ,  "三门峡":"Sanmenxia" ,  "镇江":"Zhenjiang" ,  "海北州":"Haibei" ,  "天门":"Tianmen" ,  "鄂尔多斯鄂托克前旗":"nan" ,  "丰台":"nan" ,  "待明确地区":"Area not defined" ,  "泰州":"Taizhou" ,  "蚌埠":"Bengbu" ,  "城口":"nan" ,  "荣昌区":"Rongchang District" ,  "锡林郭勒":"nan" ,  "第七师":"nan" ,  "东方市":"nan" ,  "韶关":"Shaoguan" ,  "乐东":"Ledong Li Autonomous County" ,  "塔城":"Tacheng" ,  "长寿区":"Changshou District" ,  "海淀区":"Haidian District" ,  "锦州":"Jinzhou" ,  "桂林":"Guilin" ,  "万盛经开区":"Wansheng District" ,  "枣庄":"Zaozhuang" ,  "来宾":"Laibin" ,  "石柱":"nan" ,  "鸡西":"Jixi" ,  "银川":"Yinchuan" ,  "外地来沪":"nan" ,  "晋城":"Jincheng" ,  "广元":"Guangyuan" ,  "门头沟区":"Mentougou District" ,  "漯河":"Luohe" ,  "保亭":"Baoting Li and Miao Autonomous County" ,  "五家渠":"nan" ,  "绵阳":"Mianyang" ,  "益阳":"Yiyang" ,  "朔州市":"nan" ,  "琼海市":"nan" ,  "外地来京":"nan" ,  "孝感":"Xiaogan" ,  "泸州":"Luzhou" ,  "赤峰":"Chifeng" ,  "邵阳":"Shaoyang" ,  "未明确":"nan" ,  "张家口":"Zhangjiakou" ,  "昌吉":"nan" ,  "锡林郭勒盟二连浩特":"nan" ,  "城口县":"Chengkou County" ,  "宝鸡":"Baoji" ,  "荆门":"Jingmen" ,  "津南区":"Jinnan District" ,  "江门":"Jiangmen" ,  "秀山":"nan" ,  "两江新区":"Liangjiang New Area" ,  "中山":"Zhongshan" ,  "忻州":"Xinzhou" ,  "宿松":"nan" ,  "北辰区":"Beichen District" ,  "阿克苏":"nan" ,  "自贡":"Zigong" ,  "海口":"Haikou" ,  "大兴区":"Daxing District" ,  "大兴安岭":"Daxinganling" ,  "不明地区":"nan" ,  "东方":"Dongfang" ,  "大同":"Datong" ,  "通州":"nan" ,  "南宁":"Nanning" ,  "肇庆":"Zhaoqing" ,  "贵港":"Guigang" ,  "大兴":"nan" ,  "省级（湖北输入）":"nan" ,  "十堰":"Shiyan" ,  "咸阳":"Xianyang" ,  "兵团第八师石河子市":"Shihezi, Xinjiang Production and Construction Corps 8th Division" ,  "汕头":"Shantou" ,  "滑县":"nan" ,  "天水市":"nan" ,  "潼南区":"Tongnan District" ,  "武清区":"Wuqing District" ,  "淮北":"Huaibei" ,  "济源":"Jiyuan" ,  "河池":"Hechi" ,  "房山区":"Fangshan District" ,  "平凉":"Pingliang" ,  "日照":"Rizhao" ,  "泉州":"Quanzhou" ,  "南开区":"Nankai District" ,  "黄石":"Huangshi" ,  "外地来京人员":"People from other cities" ,  "汉中":"Hanzhong" ,  "苏州":"Suzhou" ,  "吕梁":"Lüliang" ,  "温州":"Wenzhou" ,  "湖州":"Huzhou" ,  "澄迈县":"nan" ,  "眉山":"Meishan" ,  "焦作":"Jiaozuo" ,  "朝阳区":"Chaoyang District" ,  "丽江":"Lijiang" ,  "合肥":"Hefei" ,  "密云区":"Miyun District" ,  "衢州":"Quzhou" ,  "秦皇岛":"Qinhuangdao" ,  "大理州":"Dali" ,  "周口":"Zhoukou" ,  "宁德":"Ningde" ,  "渝北区":"Yubei District" ,  "铜梁区":"Tongliang District" ,  "揭阳":"Jieyang" ,  "第八师石河子":"nan" ,  "昌吉州":"Changji" ,  "外地来穗人员":"nan" ,  "丽水":"Lishui" ,  "乌鲁木齐":"Urumqi" ,  "红桥区":"Hongqiao District" ,  "石柱县":"Shizhu Tujia Autonomous County" ,  "阿克苏地区":"Akesu" ,  "汕尾":"Shanwei" ,  "玉林":"Yulin" ,  "阜新":"Fuxin" ,  "普陀区":"Putuo District" ,  "铜仁":"Tongren" ,  "金昌":"Jinchang" ,  "延庆区":"Yanqing District" ,  "阿拉善盟":"Alashanmeng" ,  "厦门":"Xiamen" ,  "嘉兴":"Jiaxing" ,  "忠县":"Zhong County" ,  "杨凌":"Yangling District in Xianyang" ,  "nan":"nan" ,  "洛阳":"Luoyang" ,  "虹口区":"Hongkou District" ,  "巫溪":"nan" ,  "南充":"Nanchong" ,  "珠海":"Zhuhai" ,  "巫溪县":"Wuxi County" ,  "平凉市":"nan" ,  "潍坊":"Weifang" ,  "九龙坡区":"Jiulongpo District" ,  "外地来津":"nan" ,  "宿迁":"Suqian" ,  "呼和浩特（新城区）":"nan" ,  "青浦区":"Qingpu District" ,  "楚雄":"nan" ,  "兵团第五师五家渠市":"nan" ,  "武汉来京人员":"nan" ,  "赤峰市林西县":"nan" ,  "莆田":"Putian" ,  "临汾市":"nan" ,  "景德镇":"Jingdezhen" ,  "德宏":"nan" ,  "新乡":"Xinxiang" ,  "衡阳":"Hengyang" ,  "贺州":"Hezhou" ,  "石嘴山":"Shizuishan" ,  "乌海":"nan" ,  "鹤岗":"Hegang" ,  "静安区":"Jing\ an District" ,  "陇南":"Longnan" ,  "四平市":"Siping" ,  "中卫":"Zhongwei" ,  "邯郸":"Handan" ,  "未明确地区":"nan" ,  "未知":"nan" ,  "开州区":"Kaizhou District" ,  "包头":"Baotou" ,  "四平":"nan" ,  "商丘":"Shangqiu" ,  "韩城":"Hancheng" ,  "江津区":"Jiangjin District" ,  "宁河区":"Ninghe District" ,  "威海":"Weihai" ,  "杭州":"Hangzhou" ,  "鄂尔多斯":"Ordos" ,  "西双版纳":"Xishuangbanna" ,  "昭通":"Zhaotong" ,  "顺义区":"Shunyi District" ,  "阳泉":"Yangquan" ,  "锡林郭勒盟":"Linguolexi" ,  "芜湖":"Wuhu" ,  "河东区":"Hedong District" ,  "临沧":"Lincang" ,  "第六师":"nan" ,  "滨州":"Binzhou" ,  "安顺":"Anshun" ,  "淄博市":"nan" ,  "唐山":"Tangshan" ,  "临沂":"Linyi" ,  "垫江":"nan" ,  "白城":"Baicheng" ,  "凉山":"Liangshan" ,  "门头沟":"nan" ,  "运城":"Yuncheng" ,  "马鞍山":"Ma\ anshan" ,  "遵义":"Zunyi" ,  "外地来津人员":"People from other cities" ,  "金华":"Jinhua" ,  "临汾":"Linfen" ,  "遂宁":"Suining" ,  "彭水县":"Pengshui Miao and Tujia Autonomous County" ,  "奉节县":"Fengjie County" ,  "七台河":"Qitaihe" ,  "金昌市":"nan" ,  "甘孜州":"Garzê Tibetan Autonomous Prefecture" ,  "黑河":"Heihe" ,  "石家庄":"Shijiazhuang" ,  "渭南":"Weinan" ,  "酉阳县":"Youyang Tujia and Miao Autonomous County" ,  "宜春":"Yichun" ,  "高新区":"Chongqing High-tech Zone" ,  "歙县":"nan" ,  "菏泽":"Heze" ,  "赣州":"Ganzhou" ,  "黔南州":"Qiannan" ,  "盘锦":"Panjin" ,  "襄阳":"Xiangyang" ,  "漯河市":"nan" ,  "承德":"Chengde" ,  "惠州":"Huizhou" ,  "喀什地区":"nan" ,  "白银":"Baiyin" ,  "巩义":"nan" ,  "三亚":"Sanya" ,  "营口":"Yingkou" ,  "金山":"nan" ,  "安阳市":"nan" ,  "宁东":"Ningdong County" ,  "六盘水":"Liupanshui" ,  "湛江":"Zhanjiang" ,  "濮阳":"Puyang" ,  "玉溪":"Yuxi" ,  "杨浦区":"Yangpu District" ,  "商丘（含永城）":"nan" ,  "丰都县":"Fengdu County" ,  "巫山县":"Wushan County" ,  "南平":"Nanping" ,  "潜江":"Qianjiang" ,  "沈阳":"Shenyang" ,  "徐汇区":"Xuhui District" ,  "宜宾":"Yibin" ,  "齐齐哈尔":"Qiqihar" ,  "浦东新区":"Pudong District" ,  "璧山区":"Bishan District" ,  "梁平区":"Liangping District" ,  "葫芦岛":"Huludao" ,  "崇明区":"Chongming District" ,  "红河州":"Honghe" ,  "保定":"Baoding" ,  "巴彦淖尔":"Bayannur" ,  "文山":"nan" ,  "吐鲁番市":"Turpan" ,  "垫江县":"Dianjiang County" ,  "兴安盟":"Xinganmeng" ,  "梅河口":"Meihekou" ,  "东城区":"Dongcheng District" ,  "固原":"Guyuan" ,  "兵团第九师":"Xinjiang Production and Construction Corps 9th Division" ,  "吉林":"nan" ,  "荆州":"Jingzhou" ,  "吉安":"Ji\ an" ,  "巴中":"Bazhong" ,  "绥化":"Suihua" ,  "滨海新区":"Binhai New Area" ,  "怀柔":"nan" ,  "黄冈":"Huanggang" ,  "六安":"Lu\ an" ,  "南通":"Nantong" ,  "驻马店":"Zhumadian" ,  "监狱系统":"nan" ,  "宿州":"Suzhou" ,  "金山区":"Jinshan District" ,  "乌海市":"Wuhai" ,  "琼海":"Qionghai" ,  "海北州":"nan" ,  "保山":"Baoshan" ,  "西双版纳州":"nan" ,  "呼和浩特":"Hohhot" ,  "舟山":"Zhoushan" ,  "廊坊":"Langfang" ,  "和平区":"Heping District" ,  "綦江区":"Qijiang District" ,  "柳州":"Liuzhou" ,  "大理":"nan" ,  "新乡（含长垣）":"nan" ,  "渝中区":"Yuzhong District" ,  "钦州":"Qinzhou" ,  "顺义":"nan" ,  "河西区":"Hexi District" ,  "防城港":"Fangchenggang" ,  "长垣县":"nan" ,  "萍乡":"Pingxiang" ,  "鹤壁":"Hebi" ,  "临夏":"Linxia" ,  "张家界":"Zhangjiajie" ,  "漳州":"Zhangzhou" ,  "丰都":"nan" ,  "扬州":"Yangzhou" ,  "上饶":"Shangrao" ,  "省十里丰监狱":"Shilifeng Prison" ,  "吴忠":"Wuzhong" ,  "通辽":"Tongliao" ,  "第八师":"nan" ,  "连云港":"Lianyungang" ,  "仙桃":"Xiantao" ,  "浦东区":"nan" ,  "咸宁":"Xianning" ,  "抚州":"Fuzhou" ,  "盐城":"Yancheng" ,  "长沙":"Changsha" ,  "吐鲁番":"nan" ,  "淮南":"Huainan" ,  "昆明":"Kunming" ,  "定安":"Ding\ an County" ,  "合川区":"Hechuan District" ,  "境外来沪":"nan" ,  "茂名":"Maoming" ,  "定西":"Dingxi" ,  "琼中":"Qiongzhong Li and Miao Autonomous County" ,  "南京":"Nanjing" ,  "西青区":"Xiqing District" ,  "待明确":"nan" ,  "巴南区":"Banan District" ,  "呼伦贝尔牙克石":"nan" ,  "境外输入":"nan" ,  "龙岩":"Longyan" ,  "武隆区":"Wulong District" ,  "张掖":"Zhangye" ,  "大渡口区":"Dadukou District" ,  "徐州":"Xuzhou" ,  "湘潭":"Xiangtan" ,  "邓州":"nan" ,  "常德":"Changde" ,  "嘉峪关":"Jiayuguan" ,  "松江区":"Songjiang District" ,  "庆阳":"Qingyang" ,  "兴安盟乌兰浩特":"nan" ,  "鹤壁市":"nan" ,  "九江":"Jiujiang" ,  "丰台区":"Fengtai District" ,  "西宁":"Xining" ,  "安阳（含滑县）":"nan" ,  "胡杨河":"nan" ,  "宝坻区":"Baodi District" ,  "呼伦贝尔":"Hulunbuir" ,  "宁东管委会":"nan" ,  "阳江":"Yangjiang" ,  "澄迈":"Chengmai County" ,  "哈尔滨":"Harbin" ,  "儋州":"Danzhou" ,  "神农架林区":"Shennongjia" ,  "普洱":"Pu\ er" ,  "黄浦区":"Huangpu District" ,  "海淀":"nan" ,  "随州":"Suizhou" ,  "德阳":"Deyang" ,  "安康":"Ankang" ,  "朔州":"Shuozhou" ,  "乌兰察布":"Ulanqab" ,  "昌平区":"Changping District" ,  "吉林市":"Jilin" ,  "天水":"Tianshui" ,  "伊犁州":"Yili" ,  "东丽区":"Dongli District" ,  "宝山区":"Baoshan District" ,  "梅州":"Meizhou" ,  "固始县":"nan" ,  "邢台":"Xingtai" ,  "聊城":"Liaocheng" ,  "抚顺市":"nan" ,  "朝阳":"nan" ,  "昌江":"Changjiang Li Autonomous County" ,  "海东":"Haidong" ,  "鞍山":"Anshan" ,  "乐山":"Leshan" ,  "丹东":"Dandong" ,  "兵团第四师":"Xinjiang Production and Construction Corps 4th Division" ,  "朝阳":"Chaoyang" ,  "铜陵":"Tongling" ,  "鄂州":"Ezhou" ,  "鹰潭":"Yingtan" ,  "大连":"Dalian" ,  "白银市":"nan" ,  "石景山区":"Shijingshan District" ,  "安庆":"Anqing" ,  "巫山":"nan" ,  "丽江市":"nan" ,  "嘉定区":"Jiading District" ,  "黔西南州":"Qianxinan" ,  "万州区":"Wanzhou District" ,  "云阳县":"Yunyang County" ,  "长垣":"nan" ,  "文山州":"Wenshan" ,  "满洲里":"nan" ,  "郴州":"Chenzhou" ,  "岳阳":"Yueyang" ,  "兵团第六师五家渠市":"Wujiaqu, Xinjiang Production and Construction Corps 5th Division" ,  "呼伦贝尔牙克石市":"nan" ,  "内江":"Neijiang" ,  "西宁市":"nan" ,  "临高县":"nan" ,  "河北区":"Hebei District" ,  "滁州":"Chuzhou" ,  "外地来沪人员":"People from other cities" ,  "毕节":"Bijie" ,  "呼伦贝尔满洲里":"nan" ,  "大庆":"Daqing" ,  "兵团第七师":"Xinjiang Production and Construction Corps 7th Division" ,  "境外输入人员":"nan" ,  "松原":"Songyuan" ,  "本溪":"Benxi" ,  "双鸭山":"Shuangyashan" ,  "长春":"Changchun" ,  "淮安":"Huainan" ,  "巴州":"Bayingolin Mongol Autonomous Prefecture" ,  "省十里丰监狱":"nan" ,  "贵阳":"Guiyang" ,  "通辽市经济开发区":"nan" ,  "邯郸市":"nan" ,  "石景山":"nan" ,  "绍兴":"Shaoxing" ,  "安阳":"Anyang" ,  "沙坪坝区":"Shapingba District" ,  "奉贤区":"Fengxian District" ,  "包头市昆都仑区":"nan" ,  "宁波":"Ningbo" ,  "文昌":"Wenchang" ,  "万宁":"Wanning" ,  "抚顺":"Fushun" ,  "杨浦":"nan" ,  "长宁区":"Changning District" ,  "奉节":"nan" ,  "南岸区":"Nan\ an District" ,  "通化":"Tonghua" ,  "拉萨":"Lhasa" ,  "黄山":"Huangshan" ,  "三明":"Sanming" ,  "陵水":"Lingshui Li Autonomous County" ,  "南昌":"Nanchang" ,  "青岛":"Qingdao" ,  "武汉":"Wuhan" ,  "赤峰市松山区":"nan" ,  "任城监狱":"nan" ,  "台州":"Taizhou" ,  "商洛":"Shangluo" ,  "楚雄州":"Chuxiong" ,  "恩施州":"Enshi Tujia and Miao Autonomous Prefecture" ,  "云阳":"nan" ,  "泰安":"Tai\ an" ,  "第八师石河子市":"nan" ,  "包头市东河区":"nan" ,  "福州":"Fuzhou" ,  "亳州":"Bozhou" ,  "怀柔区":"Huairou District" ,  "梧州":"Wuzhou" ,  "娄底":"Loudi" ,  "西城区":"Xicheng District" ,  "宜昌":"Yichang"
}
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from paho.mqtt import client as mqtt_client

class Ui_MainWindow_Data():
    ip=""
    port=1
    topic=""
    continentName=""
    continentEnglishName=""
    countryName=""
    countryEnglishName=""
    provinceName=""
    provinceEnglishName=""
    province_zipCode=""
    province_confirmedCount=""
    province_suspectedCount=""
    province_curedCount=""
    province_deadCount=""
    updateTime=""
    cityName=""
    cityEnglishName=""
    city_zipCode=""
    city_confirmedCount=""
    city_suspectedCount=""
    city_curedCount=""
    city_deadCount=""

class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("SubWindow")
        SubWindow.resize(353, 240)
        self.centralwidget = QtWidgets.QWidget(SubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 60, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 160, 75, 23))
        self.pushButton.setObjectName("pushButton")
        # SubWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SubWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 353, 23))
        self.menubar.setObjectName("menubar")
        # SubWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SubWindow)
        self.statusbar.setObjectName("statusbar")
        # SubWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubWindow)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("SubWindow", "SubWindow"))
        self.label.setText(_translate("SubWindow", "ip:"))
        self.label_2.setText(_translate("SubWindow", "port:"))
        self.label_3.setText(_translate("SubWindow", "topic:"))
        self.lineEdit.setText(_translate("SubWindow", "47.100.197.182"))
        self.lineEdit_2.setText(_translate("SubWindow", "1883"))
        self.lineEdit_3.setText(_translate("SubWindow", "/python/mqtt"))
        self.pushButton.setText(_translate("SubWindow", "finish"))
        self.pushButton.clicked.connect(self.pushButton_onClick)  # 链接槽函数

    def pushButton_onClick(self):
        global ip
        global port
        global topic
        ip = self.lineEdit.text()
        port = int(self.lineEdit_2.text())
        topic = self.lineEdit_3.text()
        print(ip)
        print(port)
        print(topic)

class Ui_SubWindow(QtWidgets.QDialog,Ui_SubWindow):
    def __init__(self):
        super(Ui_SubWindow,self).__init__()
        self.setupUi(self)


class Ui_MainWindow(object):
    data = Ui_MainWindow_Data()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 30, 131, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 70, 131, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 110, 131, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(160, 310, 131, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 150, 131, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 190, 131, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 230, 131, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 270, 131, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(520, 30, 131, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(520, 70, 131, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_10.setGeometry(QtCore.QRect(520, 110, 131, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_11.setGeometry(QtCore.QRect(520, 150, 131, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_12.setGeometry(QtCore.QRect(520, 190, 131, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 151, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 161, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 201, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 270, 141, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 310, 81, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 30, 111, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 70, 181, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 110, 181, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(320, 150, 181, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(320, 190, 161, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 270, 91, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "continentName"))
        self.label_2.setText(_translate("MainWindow", "countryName"))
        self.label_3.setText(_translate("MainWindow", "provinceName"))
        self.label_4.setText(_translate("MainWindow", "province_confirmedCount"))
        self.label_5.setText(_translate("MainWindow", "province_suspectedCount"))
        self.label_6.setText(_translate("MainWindow", "province_curedCount"))
        self.label_7.setText(_translate("MainWindow", "province_deadCount"))
        self.label_8.setText(_translate("MainWindow", "updateTime"))
        self.label_9.setText(_translate("MainWindow", "（非必填）cityName"))
        self.label_10.setText(_translate("MainWindow", "（非必填）city_confirmedCount"))
        self.label_11.setText(_translate("MainWindow", "（非必填）city_suspectedCount"))
        self.label_12.setText(_translate("MainWindow", "（非必填）city_curedCount"))
        self.label_13.setText(_translate("MainWindow", "（非必填）city_deadCount"))
        self.pushButton.setText(_translate("MainWindow", "publish"))
        self.pushButton.clicked.connect(self.pushButton_onClick)  # 链接槽函数
        self.menu.setTitle(_translate("MainWindow", "设置"))
        self.action_2.setText(_translate("MainWindow", "设置端口"))
        self.action_2.triggered.connect(self.action_2_onClick)  # 链接槽函数
        self.action_3.setText(_translate("MainWindow", "导入文件"))
        self.action_3.triggered.connect(self.action_3_onClick)  # 链接槽函数
        self.completer_1()
        self.completer_2()
        self.completer_3()
        self.completer_8()




    def completer_1(self):
        self.completer__1=QCompleter(continent_list)
        self.completer__1.setFilterMode(Qt.MatchContains)
        self.completer__1.setCompletionMode(QCompleter.PopupCompletion)
        self.lineEdit.setCompleter(self.completer__1)
    def completer_2(self):
        self.completer__2=QCompleter(country_list)
        self.completer__2.setFilterMode(Qt.MatchContains)
        self.completer__2.setCompletionMode(QCompleter.PopupCompletion)
        self.lineEdit_2.setCompleter(self.completer__2)
    def completer_3(self):
        self.completer__3=QCompleter(province_list)
        self.completer__3.setFilterMode(Qt.MatchContains)
        self.completer__3.setCompletionMode(QCompleter.PopupCompletion)
        self.lineEdit_3.setCompleter(self.completer__3)

    def completer_8(self):
        self.completer__8 = QCompleter(city_list)
        self.completer__8.setFilterMode(Qt.MatchContains)
        self.completer__8.setCompletionMode(QCompleter.PopupCompletion)
        self.lineEdit_8.setCompleter(self.completer__8)

    def action_2_onClick(self):
        print("ddddddd")
        ui2 = Ui_SubWindow()
        ui2.show()
        ui2.exec_()
    def action_3_onClick(self):
        print("导入文件")
        root = tk.Tk()
        root.withdraw()
        Filepath = filedialog.askopenfilename()  # 获得选择好的文件
        data = pd.read_csv(Filepath)
        print(data.shape[0])
        row=data.shape[0]
        count=0;
        self.data.ip = ip
        self.data.port = port
        self.data.topic = topic
        client = self.connect_mqtt()
        client.loop_start()
        while True:
            if  pd.isnull(data.iloc[count]['continentName']):
                self.data.continentName = ''
            else:
                self.data.continentName = data.iloc[count]['continentName']
            if  pd.isnull(data.iloc[count]['continentEnglishName']):
                self.data.continentEnglishName = ''
            else:
                self.data.continentEnglishName = data.iloc[count]['continentEnglishName']
            if  pd.isnull(data.iloc[count]['countryName']):
                self.data.countryName = ''
            else:
                self.data.countryName = data.iloc[count]['countryName']
            if  pd.isnull(data.iloc[count]['countryEnglishName']):
                self.data.countryEnglishName = ''
            else:
                self.data.countryEnglishName = data.iloc[count]['countryEnglishName']
            if  pd.isnull(data.iloc[count]['provinceName']):
                self.data.provinceName = ''
            else:
                self.data.provinceName = data.iloc[count]['provinceName']
            if  pd.isnull(data.iloc[count]['provinceEnglishName']):
                self.data.provinceEnglishName = ''
            else:
                self.data.provinceEnglishName = data.iloc[count]['provinceEnglishName']
            if  pd.isnull(data.iloc[count]['province_confirmedCount']):
                self.data.province_confirmedCount = ''
            else:
                self.data.province_confirmedCount = int(data.iloc[count]['province_confirmedCount'])
            if  pd.isnull(data.iloc[count]['province_suspectedCount']):
                self.data.province_suspectedCount = ''
            else:
                self.data.province_suspectedCount = int(data.iloc[count]['province_suspectedCount'])
            if  pd.isnull(data.iloc[count]['province_curedCount']):
                self.data.province_curedCount = ''
            else:
                self.data.province_curedCount = int(data.iloc[count]['province_curedCount'])
            if  pd.isnull(data.iloc[count]['province_deadCount']):
                self.data.province_deadCount = ''
            else:
                self.data.province_deadCount = int(data.iloc[count]['province_deadCount'])
            if  pd.isnull(data.iloc[count]['updateTime']):
                self.data.updateTime = ''
            else:
                self.data.updateTime = data.iloc[count]['updateTime']
            if  pd.isnull(data.iloc[count]['cityName']):
                self.data.cityName = ''
            else:
                self.data.cityName = data.iloc[count]['cityName']
            if  pd.isnull(data.iloc[count]['cityEnglishName']):
                self.data.cityEnglishName = ''
            else:
                self.data.cityEnglishName = data.iloc[count]['cityEnglishName']
            if  pd.isnull(data.iloc[count]['city_confirmedCount']):
                self.data.city_confirmedCount = ''
            else:
                self.data.city_confirmedCount = int(data.iloc[count]['city_confirmedCount'])
            if  pd.isnull(data.iloc[count]['city_suspectedCount']):
                self.data.city_suspectedCount = ''
            else:
                self.data.city_suspectedCount = int(data.iloc[count]['city_suspectedCount'])
            if  pd.isnull(data.iloc[count]['city_curedCount']):
                self.data.city_curedCount = ''
            else:
                self.data.city_curedCount = int(data.iloc[count]['city_curedCount'])
            if  pd.isnull(data.iloc[count]['city_deadCount']):
                self.data.city_deadCount = ''
            else:
                self.data.city_deadCount = int(data.iloc[count]['city_deadCount'])
            send_data = {
                "continentName": str(self.data.continentName),
                "continentEnglishName": str(self.data.continentEnglishName),
                "countryName": str(self.data.countryName),
                "countryEnglishName": str(self.data.countryEnglishName),
                "provinceName": str(self.data.provinceName),
                "provinceEnglishName": str(self.data.provinceEnglishName),
                "province_confirmedCount": str(self.data.province_confirmedCount),
                "province_suspectedCount": str(self.data.province_suspectedCount),
                "province_curedCount": str(self.data.province_curedCount),
                "province_deadCount": str(self.data.province_deadCount),
                "updateTime": str(self.data.updateTime),
                "cityName": str(self.data.cityName),
                "cityEnglishName": str(self.data.cityEnglishName),
                "city_confirmedCount": str(self.data.city_confirmedCount),
                "city_suspectedCount": str(self.data.city_suspectedCount),
                "city_curedCount": str(self.data.city_curedCount),
                "city_deadCount": str(self.data.city_deadCount)
            }
            print(send_data)
            msg = json.dumps(send_data,ensure_ascii=False)
            client.publish(self.data.topic, msg, 1)
            count=count+1
            # print(count)
            if count >= row:
                break



    def pushButton_onClick(self):
        print('onClick')
        self.runPublish()

    def runPublish(self):
        print('runPublish')

        self.data.ip = ip
        self.data.port = port
        self.data.topic = topic
        # print(self.data.ip)
        # print(self.data.port)
        # print(self.data.topic)

        client = self.connect_mqtt()
        client.loop_start()
        self.publish(client)

    def connect_mqtt(self):
        print('connect_mqtt')

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(client_id)
        client.on_connect = on_connect
        client.connect(self.data.ip, self.data.port)
        return client

    def publish(self, client):
        print('publish')
        self.data.continentName = self.lineEdit.text()
        if self.lineEdit.text()=='':
            self.data.continentEnglishName=''
        else:
            self.data.continentEnglishName = continent_list_E[self.data.continentName]
        # self.data.continentEnglishName = continent_list_E[self.data.continentName]
        self.data.countryName =self.lineEdit_2.text()
        if self.lineEdit_2.text()=='':
            self.data.countryEnglishName=''
        else:
            self.data.countryEnglishName = country_list_E[self.data.countryName]
        # self.data.countryEnglishName = country_list_E[self.data.countryName]
        self.data.provinceName = self.lineEdit_3.text()
        if self.lineEdit_3.text()=='':
            self.data.provinceEnglishName=''
        else:
            self.data.provinceEnglishName = province_list_E[self.data.provinceName]
        # self.data.provinceEnglishName = province_list_E[self.data.provinceName]
        self.data.province_confirmedCount = self.lineEdit_4.text()
        self.data.province_suspectedCount = self.lineEdit_5.text()
        self.data.province_curedCount = self.lineEdit_6.text()
        self.data.province_deadCount = self.lineEdit_7.text()
        self.data.updateTime = self.dateTimeEdit.text()

        self.data.cityName = self.lineEdit_8.text()
        if self.lineEdit_8.text()=='':
            self.data.cityEnglishName=''
        else:
            self.data.cityEnglishName = city_list_E[self.data.cityName]
        # self.data.cityEnglishName = city_list_E[self.data.cityName]
        self.data.city_confirmedCount = self.lineEdit_9.text()
        self.data.city_suspectedCount = self.lineEdit_10.text()
        self.data.city_curedCount = self.lineEdit_11.text()
        self.data.city_deadCount = self.lineEdit_12.text()
        send_data = {
                "continentName": self.data.continentName,
                "continentEnglishName": self.data.continentEnglishName,
                "countryName": self.data.countryName,
                "countryEnglishName": self.data.countryEnglishName,
                "provinceName": self.data.provinceName,
                "provinceEnglishName": self.data.provinceEnglishName,
                "province_confirmedCount": self.data.province_confirmedCount,
                "province_suspectedCount": self.data.province_suspectedCount,
                "province_curedCount": self.data.province_curedCount,
                "province_deadCount": self.data.province_deadCount,
                "updateTime": self.data.updateTime,
                "cityName": self.data.cityName,
                "cityEnglishName": self.data.cityEnglishName,
                "city_confirmedCount": self.data.city_confirmedCount,
                "city_suspectedCount": self.data.city_suspectedCount,
                "city_curedCount": self.data.city_curedCount,
                "city_deadCount": self.data.city_deadCount
        }
        msg = json.dumps(send_data,ensure_ascii=False)
        # print(self.data.topic)
        result = client.publish(self.data.topic, msg, 1)
        # result: [0, 1]

        status = result[0]
        if status == 0:
            print(f"Successfully Send  ")
        else:
            print(f"Failed to send message")
if __name__ =='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # SubWindow = QtWidgets.QDialog()
    # ui2 = Ui_SubWindow()
    # ui2.setupUi(SubWindow)
    # SubWindow.show()
    sys.exit(app.exec_())