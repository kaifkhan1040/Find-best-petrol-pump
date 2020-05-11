import pandas as pd
from tkinter import *
import webbrowser
from twilio.rest import Client

def pump():
    ro = Tk()
    ro.geometry('350x300+120+120')
    ro.title('PETROL PUMP')
    def close():
        ro.destroy()
    def petrol1():
        # def sms():
        a = 'Enter Account Sid'
        b = 'Enter twillo tokken'
        # d = str('+91' + e2.get())
        client = Client(a, b)
        try:
            a_df = pd.read_csv('datasetof petrolpump.csv')
        except FileNotFoundError:
            print("File Missing")
        ci=e1.get()

        try:
            b_df = a_df.loc[a_df['city'] == ci]
            print(b_df)
        except ValueError:
            print("invalid value")
        except TypeError:
            print("invalid value")

        b_df.to_csv("city.csv")

        city_df = pd.read_csv("city.csv")
       
        try:
            location = city_df['name'][city_df['ratting'].idxmax()]
            print(location)
            print('The best petrol pump in {} is {}'.format(ci, location))
            location = str(location)
            print('https://www.google.com/maps/search/' + location)
            f = 'https://www.google.com/maps/search/' + location
            client.messages.create(to='enter your mobile number with country code',
                                   from_='Enter twillo number ',
                                   body=f)
            print("Link send to your register mobile number")
            webbrowser.open('https://www.google.com/maps/search/petrol pump ' + location)
        except UnboundLocalError:
            print("variable error")
        except TypeError:
            print("invalid")
    user_ci=StringVar()
    l1=Label(ro,text='Enter the city : ')
    l1.grid(row=0,column=0)
    e1=Entry(ro,text=user_ci)
    e1.grid(row=0,column=1)
    btn=Button(ro,text='Search Petrol Pump',command=petrol1)
    btn.grid(row=1,column=1)
    btn1 = Button(ro, text='Quit', command=close)
    btn1.grid(row=2, column=1)
    ro.mainloop()
if __name__ == '__main__':
    pump()
