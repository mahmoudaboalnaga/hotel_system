"""
reservation.py
This is the reservation class file
"""
import hotel
class Reservation(object):

    reservation_list=[]


    def __init__(self, hotel_name, customer_name,mobile_number):
        self.hotel_name = hotel_name
        self.customer_name = customer_name
        self.mobile_number = mobile_number

        Reservation.reservation_list.append([self.hotel_name, self.customer_name, self.mobile_number])
