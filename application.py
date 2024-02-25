import streamlit as st
import pickle
import pandas as pd
from sklearn.pipeline import Pipeline

un= pd.read_pickle("unique_value_dict.pkl")


st.title("Mobile Price Predictor")
flag=0

col1, col2 = st.columns(2)

with col1:
   company = st.selectbox('Mobile Brand',([ 'Realme', 'Samsung', 'Xiaomi', 'Vivo', 'Apple', 'OPPO', 'Motorola','Tecno', 'Infinix', 'Poco', 'iQOO', 'Nokia', 'iKall', 'Lava', 'OnePlus', 'Google', 'POCO', 'Oppo', 'Micromax', 'Asus', 'itel', 'Huawei', 'Sony','Nothing', 'LG', 'Oukitel', 'Gionee', 'Jio', 'Yu', 'BlackBerry','Coolpad', 'CAT', 'Lyf'])
   ,index=None,placeholder="Choose an option")
   
   battery_capcity = st.selectbox('Battery size', ([5000, 6000, 4500, 4000, 3200, 4230, 5020, 4700, 3000, 4300, 5050, 3300,
   4400, 3500, 4200, 3700, 5160, 4800, 4030, 4352, 4250, 7000, 4323, 3095,
   4520, 4325, 1821, 3240, 2438, 4350, 4020, 3279, 4100, 3100, 3450, 3360,
   2700, 3260, 2600, 5065, 3110, 4050, 4980, 3080, 4600, 4610, 4830, 4310,
   5003, 5080, 5200, 2500, 3765, 8300, 4025, 3030, 3010, 4060, 4614, 8000,
   3430, 3190, 1960, 2730, 4780, 4015, 4080, 3520, 2800, 4355, 4410, 2550]),index=None,placeholder="Choose an option")
   
   charger_capacity = st.selectbox('Charger', (un["charger_capacity"]),index=None,placeholder="Choose an option")
   
   fast_charging = st.selectbox('Fast Charging', (un["fast_charging"]),index=None,placeholder="Choose an option")

   ram_capacity = st.selectbox('Ram', (un["ram_capacity"]),index=None,placeholder="Choose an option")

   rom = st.selectbox('Rom', (un["rom"]),index=None,placeholder="Choose an option")
   
   processor_name = st.selectbox('Name of processor', (un["processor_name"]),index=None,placeholder="Choose an option")

   processor_cores = st.selectbox('Cores of processor', (un["processor_cores"]),index=None,placeholder="Choose an option")

   processor_speed = st.selectbox('Processor Speed', (un["processor_speed"]),index=None,placeholder="Choose an option")


with col2:

   five_G = st.selectbox('5G', (un["5G"]),index=None,placeholder="Choose an option")

   nfc = st.selectbox('NFC',(un["nfc"]),index=None,placeholder="Choose an option")
   
   rear_camera = st.selectbox('Rear Camera', (un["rear_camera"]),index=None,placeholder="Choose an option")
   
   rear_camera_count = st.selectbox('Number of Rear Camera', (un["rear_camera_count"]),index=None,placeholder="Choose an option")
   
   front_camera = st.selectbox('Front Camera', (un["front_camera"]),index=None,placeholder="Choose an option")

   front_camera_count = st.selectbox('Number Of Front Camera', (un["front_camera_count"]),index=None,placeholder="Choose an option")

   screen_size = st.selectbox('Size of Screen', (un["screen_size"]),index=None,placeholder="Choose an option")
   
   pixel1 = st.selectbox('pixel1', (un["pixel1"]),index=None,placeholder="Choose an option")

   pixel2 = st.selectbox('pixel2', (un["pixel2"]),index=None,placeholder="Choose an option")

os_type = st.selectbox('Operating System', (un["os_type"]),index=None,placeholder="Choose an option")

pipe = pd.read_pickle("prediction.pkl")
# pipe=       pickle.load(open("transform.pkl","rb"))
# rf=pickle.load(open("random_forest.pkl","rb"))


col1, col2, col3 = st.columns(3)
with col2 :
    if st.button("Submit"):
      x=[[pixel1,pixel2,company,battery_capcity,charger_capacity,fast_charging,ram_capacity,rom,five_G,nfc,processor_name
         ,processor_cores,processor_speed,screen_size,rear_camera,rear_camera_count,front_camera,front_camera_count
         ,os_type]]
      column=['pixel1', 'pixel2', 'company', 'battery_capacity', 'charger_capacity',
       'fast_charging', 'ram_capacity', 'rom', '5G', 'nfc', 'processor_name',
       'processor_cores', 'processor_speed', 'screen_size', 'rear_camera',
       'rear_camera_count', 'front_camera', 'front_camera_count', 'os_type']
      
      df=pd.DataFrame(x,columns=column)
      value=pipe.predict(df)
      flag=1
if flag==1:
   st.write("Cost of mobile is around")      
   st.title(value.round(1))


