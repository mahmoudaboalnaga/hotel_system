"""
hotel.py
This is the Hotel class file
"""

class Hotel():
    hotels = []


    def __init__(self, number,hotel_name, city,total_rooms,empty_rooms):
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        Hotel.hotels.append([self.number , self.hotel_name, self.city, self.total_rooms,self.empty_rooms])

    ############################################################################

   

    def find_hotel(self,hotel_name):
        #function to find a specific hotel in the list
        x=0

        while x<len(self.hotels):
            if self.hotels[x][1]==hotel_name:
                return self.hotels[x]
            x+=1
        return False

    ###########################################################################

    def get_no_empty_rooms(self,hotel_name):
         #function to get empty rooms in  a specific hotel in the list
        if self.find_hotel(hotel_name)!=False:
            search_list=self.find_hotel(hotel_name)
            empty_rooms=self.hotels[self.hotels.index(search_list)][4]
            return empty_rooms



    ###########################################################################
    def update_empty_rooms(self,hotel_name,new_empty_rooms):
        #function to update empty rooms in a specific hotel in the list
        if self.find_hotel(hotel_name)!=False:
            edit_list=self.find_hotel(hotel_name)
            self.hotels[self.hotels.index(edit_list)][4]=new_empty_rooms
        else:
            print "cannot update empty rooms"



    ###########################################################################

    def edit_hotel(self,hotel_name,new_hotel_name,new_city,new_total_rooms,new_empty_rooms):
        #function to update a specific hotel in the list
        if self.find_hotel(hotel_name)!=False:
            edit_list=self.find_hotel(hotel_name)
            self.hotels[self.hotels.index(edit_list)][1]=new_hotel_name
            self.hotels[self.hotels.index(edit_list)][2]=new_city
            self.hotels[self.hotels.index(edit_list)][3]=new_total_rooms
            self.hotels[self.hotels.index(edit_list)][4]=new_empty_rooms

            print "update success"
        else:
            print "cannot update a null value"



################################################################################



    def remove_hotel(self,hotel_name):
        #function to remove a specific hotel in the list
        if self.find_hotel(hotel_name)!=False:
            del_list=self.find_hotel(hotel_name)
            del(self.hotels[self.hotels.index(del_list)])
            print "deleted"
        else:
            print "cannot delete a null value"



###############################################################################


    def list_hotels_in_city(self,city):

        # search inside Hotel.hotels for hotels in a 'city'
        no_of_hotels_in_city=0

        x=0

        while x<len(self.hotels):
            if self.hotels[x][2]==city:
                no_of_hotels_in_city+=1
            x+=1
        return no_of_hotels_in_city



####################################################
    def city_hotels(self,city):
    
        # search inside Hotel.hotels for hotels in a 'city'
        hotels_in_city=[]

        x=0

        while x<len(self.hotels):
            if self.hotels[x][2]==city:
                hotels_in_city.append(self.hotels[x][1])
               
            x+=1
        return hotels_in_city
####################################################