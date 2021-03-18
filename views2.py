from django.shortcuts import render
from django.http import HttpResponse
from .models import passengers
from .models import flit
from .models import food
from datetime import date
from random import choice
import datetime
Pass=0
app_name='main'
cost_flight=[9425,4275,9200,5000,6500,2100,15000,9425,5000,15000,6500,2100,
            9200,4275]
number_=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
name_flight=['jet_airways','indigo','spicejet','go_air','tejas','vistara','air india','jet_airways',
             'go_air','air india','tejas','vistara','spicejet','indigo']
images=['jet_airways.png','indigo.png','spicejet.png','go_air.png','tejas.jpg','vistara.png',
        'air india.png','jet_airways.png','go_air.png','air india.png','tejas.jpg','vistara.png',
        'spicejet.png','indigo.png']             
time_flight=['8:00-10:00','22:00-22:00','8:00-10:00','20:00-22:00','15:45-17:00','8:00-10:30',
            '21:00-23:00','15:45-17:00','22:30-1:00','20:00-00:00','15:45-17:00','8:00-10:30',
            '21:00-23:00','15:45-17:00']
name_food=['pizza','burger','biryani','cbriyani','idli','dosa','noodles','cake','chapati','sandwich',
           'aloop','FFries','Gjamun','upma','coke','sprite','kfisher','coffee','tea','vodaka','redbull',
           'afizz','frooti','thumbs','orangejuice','lemonjuice','pinejuice','soda','pepsi']
cost_of_food=[200,100,300,500,150,150,200,300,100,150,100,300,400,250,400,100,100,250,150,100,400,200,100,150,100,150,150,200,100]
sum_amount=0
d={}
for i in range(len(name_food)):
    d[name_food[i]]=cost_of_food[i]
# Create your views here.
def main(request):
    return render(request,'mainhtml2.html')

def account(request):
    return render(request,'create_account.html')
def about(request):
    return render(request,'about.html')

def details(request):
    global Pass
    val1=request.GET['From']
    val2=request.GET['To']
    date=request.GET['date']
    Pass=int(request.GET['no_of_people'])
    """and date=>datetime.date.today()""" 
    if int(Pass)>0 and str(date)>=str(datetime.date.today()) :
        pass_info=passengers(From=val1,To=val2,Date=date,no_of_people=Pass)
        pass_info.save()
       #return render(request,'flights.html',{'date':date,'from':val1,'to':val2})
        fli1,fli2,fli3,fli4,fli5=flit(),flit(),flit(),flit(),flit()
        fli6,fli7,fli8,fli9,fli10=flit(),flit(),flit(),flit(),flit()
        fli11,fli12,fli13,fli14=flit(),flit(),flit(),flit()

        flights=[fli1,fli2,fli3,fli3,fli4,fli5,fli6,fli7,fli8,fli9,fli10]
        flights+=[fli11,fli12,fli13,fli14]
        for i in range(len(flights)-1):
            print(i)
            #print(flights[i])
            flights[i].no=number_[i]
            #print(flights[i].no)
            flights[i].name=name_flight[i]
            #print(flights[i].name)
            flights[i].time=time_flight[i]
           # print(flights[i].time)
            flights[i].fare=str(cost_flight[i])
            #print(flights[i].fare)
            flights[i].image=images[i]
            #print(flights[i].image)
     
        
        return render(request,'for_flight.html',{'flight':flights,'no_p':Pass})
    else:
        if int(Pass)<0:
            msg='no of people'
        elif str(date)<str(datetime.date.today()):
            msg='date'    
        return render(request,'message.html',{'msg':msg})   


def transaction(request):
    return render(request,'trans_complete.html')    

def food_booked_pay(request):
    global d,sum_amount
    x=request.GET['name_food']
    if x!='':
        x=x.split(',')
        # print(x)
        for i in x:
        # print(i)
            sum_amount+=d[i]
        # print(sum_amount)
    else:
        sum_amount+=0

    captcha_var='qwertyuiopla90ASDFGHJKLQWERTYUsdfghjklzxcvbnm12345678IOPZXCVBNM'
    captcha=''
    for i in range(5):
       
        captcha+=choice(captcha_var)
    return render(request,'pay.html',{'captcha':captcha,'sum_amount':sum_amount})    

def cost(request):
    return render(request,'food.html')
def cost1(request):
    global sum_amount,Pass
    flight_no=request.GET['fl_no']
    sum_amount=(cost_flight[int(flight_no)-1])*Pass

    return render(request,'food.html',{'flight_no':flight_no,'sum_amount':sum_amount})

def history(request):
     objs=passengers.objects.all()
     obj1=flit.objects.all()
     lst,lst1=[],[]
     for i in objs:
         lst+=[i.From,i.To,i.Date]
     for i in obj1:
         lst1+=[i.fare]



     return render(request,'history.html',{'his':lst,'his2':lst1})   
