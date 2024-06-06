from tkinter import * 
import requests 
import datetime
import messagebox

root= Tk()
root.title("Weather App")
root.geometry("700x880")
root.configure(bg="#2c2d2e")

def weather():
    city=enter_box.get()
    api_key = '58d812937a6bcaf679b3917726756580'
    url =f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    temperature_box.delete(0, END)
    speed_box.delete(0, END)
    pressure_box.delete(0, END)
    humidity_box.delete(0, END)
    clouds_box.delete(0, END)
    description_box.delete(0, END)
    time_box.delete(0, END)
    if response.status_code== 200:
        data= response.json()
        temperature = data['main']['temp']-273.15
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        speed = ( data['wind']['speed'])*3.6
        epoch_time =data['dt']
        date_time = datetime.datetime.fromtimestamp(epoch_time)
        description = data['weather'][0]['description']
        clouds = data['clouds']['all']


        temperature_box.insert(0 , '{:.2f}'.format (temperature) + " celcius")
        speed_box.insert(0 , '{:.2f}'.format (speed) + " km/h")
        pressure_box.insert(0 , str (pressure) + " hPa")
        humidity_box.insert(0 , str (humidity) + " %")
        clouds_box.insert(0 , str (clouds) + " %")
        description_box.insert(0 , str (description) )
        time_box.insert(0 , str (date_time) )

    else :
        messagebox.showerror("Error" , "CITY NOT FOUND \n Enter a valid City Name")
        enter_box.delete(0, END)



# creating title
title_label = Label( root, text="Weather App" ,font=("",30,"bold"),bg="#2c2d2e",fg="#44bb57")

# creating Entry Label and Box
enter_label = Label( root, text="Enter The City" ,font=("",15,""),bg="#2c2d2e",fg="white")
enter_box =  Entry(root, font=("", 24))  

# creating Weather Button
weather_button = Button(root, text="Weather", padx=15, pady=5, font=("arial",18,"bold"),bd=3,fg="#323639",activebackground="white",bg="#44bb57",width=6,command= weather)

# creating frame1 for remaining elements
frame1 = Frame(root)
frame1.configure(bg="#2c2d2e")


# creating Labels 
temperature_label = Label( frame1, text="Temperature" ,font=("",20,""),bg="#2c2d2e",fg="white")
speed_label = Label( frame1, text="Speed" ,font=("",20,""),bg="#2c2d2e",fg="white")
pressure_label = Label( frame1, text="Pressure" ,font=("",20,""),bg="#2c2d2e",fg="white")
humidity_label = Label( frame1, text="Humidity" ,font=("",20,""),bg="#2c2d2e",fg="white")
clouds_label = Label( frame1, text="Clouds" ,font=("",20,""),bg="#2c2d2e",fg="white")
description_label = Label( frame1, text="Description" ,font=("",20,""),bg="#2c2d2e",fg="white")
time_label = Label( frame1, text="Date & Time",font=("",20,""),bg="#2c2d2e",fg="white")

# creating Entry Boxes 
temperature_box =  Entry(frame1, font=("", 24)) 
speed_box =  Entry(frame1, font=("", 24)) 
pressure_box =  Entry(frame1, font=("", 24)) 
humidity_box =  Entry(frame1, font=("", 24)) 
clouds_box =  Entry(frame1, font=("", 24)) 
description_box =  Entry(frame1, font=("", 24)) 
time_box =  Entry(frame1, font=("", 24)) 



# creating grid for root elements  
title_label.grid(row=0, column=0, padx=220, pady=35)
enter_label.grid(row=1, column=0, padx=5, pady=5)
enter_box.grid(row=2, column=0, padx=5, pady=5)
weather_button.grid(row=3, column=0, padx=5, pady=25)

# creating grid for frame1  
frame1.grid(row=4, column=0, padx=5, pady=5)

# creating grid for frame1 labels  
temperature_label.grid(row=0, column=0, padx=5, pady=12)
speed_label.grid(row=1, column=0, padx=5, pady=12)
pressure_label.grid(row=2, column=0, padx=5, pady=12)
humidity_label.grid(row=3, column=0, padx=5, pady=12)
clouds_label.grid(row=4, column=0, padx=5, pady=12)
description_label.grid(row=5, column=0, padx=12, pady=12)
time_label.grid(row=6, column=0, padx=5, pady=12)


# creating grid for frame1 displsy boxes  
temperature_box.grid(row=0, column=1, padx=5, pady=12)
speed_box.grid(row=1, column=1, padx=5, pady=12)
pressure_box.grid(row=2, column=1, padx=5, pady=12)
humidity_box.grid(row=3, column=1, padx=5, pady=12)
clouds_box.grid(row=4, column=1, padx=5, pady=12)
description_box.grid(row=5, column=1, padx=5, pady=12)
time_box.grid(row=6, column=1, padx=5, pady=12)




root.mainloop()