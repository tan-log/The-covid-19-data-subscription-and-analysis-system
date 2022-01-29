import pandas as pd
data=pd.read_csv("DXYArea.csv")
xx=data[['cityName','city_zipCode']]
# print(x.iloc[0])
# print(x)
x=1
y=set()
print(type(y))
while True:

    z =  "\""+ str(xx.iloc[x]['cityName'])+"\""+":"+"\""+str(xx.iloc[x]['city_zipCode'])+"\""
    # print(z)
    y.add(z)
    # print(y)
    x=x+1
    # print(x)
    if x>711574:
        break

print(y)
