"""
    main.py
    This is the main application file for the Hotel Reservation system
"""
import hotel
import reservation
import notification
import customer
import tester
import datetime


class Main(object):
    def __init__(self):
        pass
    
    def start_app(self):
        i=0
        test=tester.Tester.hotels
        while i< len(test):
            new_hotel=hotel.Hotel(test[i][0],test[i][1],test[i][2],test[i][3],test[i][4])
            i+=1


        ################################
        #check if there is empty room in a hotels_list

        x=0
        test_reservation=tester.Tester.reservation
        while x< len(test_reservation):
            hotel_name=test_reservation[x][0]
            customer_name=test_reservation[x][1]
            mobile_number=test_reservation[x][2]
            if new_hotel.get_no_empty_rooms(hotel_name)>0:
                new_reservation=reservation.Reservation(hotel_name,customer_name,mobile_number)
                new_hotel.update_empty_rooms(hotel_name,new_hotel.get_no_empty_rooms(hotel_name)-1)

            #confirmation message
                message="thank you {}\n you reserve in {}\n date: {}".format(customer_name,hotel_name,datetime.datetime.now().strftime("%a, %d %B %Y %I:%M:%S"))
            #send confirmation message to customer
                new_notification=notification.Notification()
                new_notification.send_sms(mobile_number,message)
                # new_notification=notification.Notification(mobile_number,message)
            #add to customers list
                new_customer=customer.Customer(customer_name,mobile_number)


            else:
                print "no reservation available"
            x+=1




