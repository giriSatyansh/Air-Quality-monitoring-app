#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from PIL import ImageTk,Image
import requests
import json
root=Tk()
root.title('Air Quality App')
root.geometry("600x100")

def zipLookup():
    try:
        api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode= " + zip.get() + "&distance=5&API_KEY=00B7FAED-FD8D-4672-8A8E-5FEDF9785E94")
        api=json.loads(api_request.content)
        city=api[0]['ReportingArea']
        quality=api[0]['AQI']
        category=api[0]['Category']['Name']
        if category=="Good":
            weather_color="#0C0"
        elif category=="Moderate":
            weater_color=="#FFFF00"
        elif category=="Unhealthy for Sensitive Groups":
            weater_color=="#ff9900"
        elif category=="Unhealthy":
            weater_color=="#FF0000"
        elif category=="Very Unhealthy":
            weater_color=="#990066"
        elif category=="Hazardous":
            weater_color=="#660000"
        
        root.configure(background=weather_color)
    
        myLabel=Label(root,text=city +" "+ "Air Quality" +"  "+ str(quality)+" "+category,font=("Helvetica",20),background=weather_color)
        myLabel.grid(row=1,column=0,columnspan=2)
    except Exception as e:
        api="Error..."


#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=00B7FAED-FD8D-4672-8A8E-5FEDF9785E94


zip=Entry(root,bg="yellow")
zip.grid(row=0,column=0,stick=W+E+N+S)
zipButton=Button(root,text="Enter Area Code",command=zipLookup)
zipButton.grid(row=0,column=1,stick=W+E+N+S)
root.mainloop()


# In[ ]:




