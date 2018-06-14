from controllers.hotel import *
from controllers.customer import *
from controllers.reservation import *
from controllers.notification import *
from controllers.main import *
from controllers.tester import *

from django.http import HttpResponse




def HotelList(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    i=0
    test=Tester.hotels
    while i< len(test):
        hotel_obj=Hotel(test[i][0],test[i][1],test[i][2],test[i][3],test[i][4])
        i+=1
    hotel_list=Hotel.hotels
    
    hotel_list_output = "<ul>"
    i=0
    while i<len(hotel_list):
        hotel_list_output +="<li>"+hotel_list[i][1]+"</li>"
        i+=1
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output)

def HotelInCity(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    # select any city 
    # your code here
    i=0
    test=Tester.hotels
    city="Abu Dhabi"
    while i< len(test):
        hotel_obj=Hotel(test[i][0],test[i][1],test[i][2],test[i][3],test[i][4])
        i+=1
    city_hotels_list=hotel_obj.city_hotels(city)
    city_hotels='<h1><center> hotels in '+city+'</h1></center></br>'
    city_hotels+='<ul>'
    for h in city_hotels_list:
        city_hotels+='<li>'+h+'</li>'
        
    city_hotels+='</ul>'       
    return HttpResponse(city_hotels)
    

def ReservationList(request):
    
    main_app=Main()
    main_app.start_app()
    ReservationList_obj=Reservation.reservation_list
    ReservationList_text='<h1><center>Reservation List</h1></center>'
    ReservationList_text+='<table>'
    for r in ReservationList_obj:
        ReservationList_text+='<tr>'
        i=0
        while i<len(r):
            ReservationList_text+='<td>'+r[i]+'</td>'
            i+=1
        ReservationList_text+='</tr>'
    ReservationList_text+='</table>'        
            

    return HttpResponse(ReservationList_text)
    # call the functions to fill all the data about hotels, customers, and reservations
    # select any hotel 
    # your code here
