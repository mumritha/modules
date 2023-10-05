class book:
    total=int(input("total flights"))
    flights={f'flight{i}':{'ticket':50,'earning':0,'price':5000}for i in range(1,total+1)}
    
    id=0
    passengers={}

    @classmethod
    def choice(cls):
        print("\n1.book\n2.cancel\n3.show")
        a=int(input("enter the choice: "))
        if a==1:
            cls.book()
        elif a==2:
            cls.cancel()
        elif a==3:
            cls.show()    
        else:
            print("invalid choice")    
        cls.choice()    

    @classmethod
    def book(cls):
        flight_no=int(input("flight no: "))
        if flight_no <=cls.total:
            print(f"available tickets: {cls.flights[f'flight{flight_no}']['ticket']}")
            if cls.flights[f'flight{flight_no}']['ticket'] >0:
                no_of_tick=int(input("no of tickets required: "))
                t=no_of_tick*(cls.flights[f'flight{flight_no}']['price'])
                p=no_of_tick*200
                for i in range(1,no_of_tick+1):
                    name=input("\nname: ")
                    age=int(input("age: "))
                    cls.id+=1
                    cls.passengers[cls.id]={'flightno':f'flight{flight_no}','name':name,'age':age,'ticketprice':cls.flights[f'flight{flight_no}']['price']}
                cls.flights[f'flight{flight_no}']['price']+=p
                cls.flights[f'flight{flight_no}']['ticket']-=no_of_tick
                cls.flights[f'flight{flight_no}']['earning']+=t
                print("booked")
                cls.choice()
            else:
               print("There is no ticket available")    
               cls.choice()
        else:
            print("\nflights no is wrong")

    @classmethod
    def cancel(cls):
        canctick=int(input("Enter the id to cancel: "))
        canceled=cls.passengers.get(canctick)
        print(cls.flights)
        print(cls.passengers)
        print(canceled)
        if canceled:            
            e=cls.passengers[canctick]['ticketprice']
            fli=cls.passengers[canctick]['flightno']
            cls.flights[f'{fli}']['ticket']+=1
            cls.flights[f'{fli}']['price']-=200
            cls.flights[f'{fli}']['earning']-=e           
            cls.passengers.pop(canctick)
            print("ticket canceled")
            cls.choice()
        else:
            print("\nThere is no id to cancel ")
            cls.choice()

    @classmethod
    def show(cls):   
        if cls.flights:
            for i,j in cls.flights.items():
                print(f'{i},{j}\n')
                if cls.passengers:
                    for l,k in cls.passengers.items():
                        if k['flightno']==i:
                            print(f'{l},{k["name"]}\n')
            cls.choice()                
        else:
            print("there is no flight")
if __name__ == "__main__":
    book.choice()
        

        
            





