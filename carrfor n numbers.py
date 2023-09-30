
class taxi:
    totalcars=int(input("taxi:"))
    taxi = {f'taxi{i}': {'point': 'A', 'earning': 0} for i in range(1, totalcars + 1)}
    # taxi={'taxe1':{'point':'A','earning':0},'taxe2':{'point':'A','earning':0},'taxe3':{'point':'A','earning':0},'taxe4':{'point':'A','earning':0}}
    pts=['A','B','C','D','E','F']
    id=0
    booked_passengers={}
    
    @classmethod
    def option(cls):
        print("\n1.Booking taxi\n2.display")
        a=int(input("Enter your choice: "))
        if (a==1):
            cls.book()
        elif (a==2):
            cls.display()
        else:
            print("\nInvalid choice")
            cls.option()
            
    @classmethod
    def book(cls):
        name=input("\nName:")
        pickuppoint=input("\nPickup_point:").upper()
        Dropepoint=input("\nDrope_point:").upper()
        time=int(input("\nTime:"))
        flag=False
        e = 0 
        t=0 
        if pickuppoint == 'A':
            neighboring_points = ['B', 'C', 'D','E','F']
            match=[cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == pickuppoint]

            if not match:
                for neighbor_point in neighboring_points:
                    match = [cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == neighbor_point]
                    if match:
                        break

            if match:
                min_earning_taxi = min(match, key=lambda x: x['earning'])
                key_min=[key for key,value in cls.taxi.items() if value==min_earning_taxi][0]
                print("taxi can be allocated")
                print (f'{key_min} is allocated')
                if Dropepoint=='B':
                    e=100+((15-5)*10)
                    t=time+1
                elif Dropepoint=='C':
                    e=100+((30-5)*10) 
                    t=time+2  
                elif Dropepoint=='D':
                    e=100+((45-5)*10)    
                    t=time+3   
                elif Dropepoint=='E':
                    e=100+((60-5)*10)  
                    t=time+4     
                elif Dropepoint=='F':
                    e=100+((75-5)*10)   
                    t=time+5
                else:
                    print("cant reachable")                    


        elif pickuppoint == 'B':
            neighboring_points = ['A', 'C', 'D','E','F']
            match=[cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == pickuppoint]

            if not match:
                for neighbor_point in neighboring_points:
                    match = [cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == neighbor_point]
                    if match:
                        break

            if match:
                min_earning_taxi = min(match, key=lambda x: x['earning'])
                key_min=[key for key,value in cls.taxi.items() if value==min_earning_taxi][0]
                print("taxi can be allocated")
                print (f'{key_min} is allocated')
                if Dropepoint=='A':
                    e=100+((15-5)*10)
                    t=time+1
                elif Dropepoint=='C':
                    e=100+((15-5)*10) 
                    t=time+2  
                elif Dropepoint=='D':
                    e=100+((30-5)*10)    
                    t=time+3   
                elif Dropepoint=='E':
                    e=100+((45-5)*10)  
                    t=time+4     
                elif Dropepoint=='F':
                    e=100+((60-5)*10)   
                    t=time+5
                else:
                    print("cant reachable")


        elif pickuppoint == 'C':
            neighboring_points = ['A', 'B', 'D','E','F']
            match=[cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == pickuppoint]

            if not match:
                for neighbor_point in neighboring_points:
                    match = [cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == neighbor_point]
                    if match:
                        break

            if match:
                min_earning_taxi = min(match, key=lambda x: x['earning'])
                key_min=[key for key,value in cls.taxi.items() if value==min_earning_taxi][0]
                print("taxi can be allocated")
                print (f'{key_min} is allocated')
                if Dropepoint=='A':
                    e=100+((30-5)*10)
                    t=time+1
                elif Dropepoint=='B':
                    e=100+((15-5)*10) 
                    t=time+2  
                elif Dropepoint=='D':
                    e=100+((15-5)*10)    
                    t=time+3   
                elif Dropepoint=='E':
                    e=100+((30-5)*10)  
                    t=time+4     
                elif Dropepoint=='F':
                    e=100+((45-5)*10)   
                    t=time+5
                else:
                    print("cant reachable")


        elif pickuppoint == 'D':
            neighboring_points = ['A', 'B', 'C','E','F']
            match=[cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == pickuppoint]

            if not match:
                for neighbor_point in neighboring_points:
                    match = [cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == neighbor_point]
                    if match:
                        break

            if match:
                min_earning_taxi = min(match, key=lambda x: x['earning'])
                key_min=[key for key,value in cls.taxi.items() if value==min_earning_taxi][0]
                print("taxi can be allocated")
                print (f'{key_min} is allocated')
                if Dropepoint=='A':
                    e=100+((45-5)*10)
                    t=time+1
                elif Dropepoint=='C':
                    e=100+((15-5)*10) 
                    t=time+2  
                elif Dropepoint=='B':
                    e=100+((30-5)*10)    
                    t=time+3   
                elif Dropepoint=='E':
                    e=100+((15-5)*10)  
                    t=time+4     
                elif Dropepoint=='F':
                    e=100+((30-5)*10)   
                    t=time+5
                else:
                    print("cant reachable")


        elif pickuppoint == 'E':
            neighboring_points = ['A', 'B', 'C','D','F']
            match=[cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == pickuppoint]

            if not match:
                for neighbor_point in neighboring_points:
                    match = [cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == neighbor_point]
                    if match:
                        break

            if match:
                min_earning_taxi = min(match, key=lambda x: x['earning'])
                key_min=[key for key,value in cls.taxi.items() if value==min_earning_taxi][0]
                print("taxi can be allocated")
                print (f'{key_min} is allocated')
                if Dropepoint=='A':
                    e=100+((45-5)*10)
                    t=time+1
                elif Dropepoint=='C':
                    e=100+((30-5)*10) 
                    t=time+2  
                elif Dropepoint=='D':
                    e=100+((15-5)*10)    
                    t=time+3   
                elif Dropepoint=='B':
                    e=100+((30-5)*10)  
                    t=time+4     
                elif Dropepoint=='F':
                    e=100+((15-5)*10)   
                    t=time+5
                else:
                    print("cant reachable")


        elif pickuppoint == 'F':
            neighboring_points = ['A','B', 'C', 'D','E']
            match=[cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == pickuppoint]

            if not match:
                for neighbor_point in neighboring_points:
                    match = [cls.taxi[key] for key in cls.taxi if cls.taxi[key]['point'] == neighbor_point]
                    if match:
                        break

            if match:
                min_earning_taxi = min(match, key=lambda x: x['earning'])
                key_min=[key for key,value in cls.taxi.items() if value==min_earning_taxi][0]
                print("taxi can be allocated")
                print (f'{key_min} is allocated')
                if Dropepoint=='A':
                    e=100+((75-5)*10)
                    t=time+1
                elif Dropepoint=='B':
                    e=100+((60-5)*10) 
                    t=time+2  
                elif Dropepoint=='D':
                    e=100+((30-5)*10)    
                    t=time+3   
                elif Dropepoint=='C':
                    e=100+((45-5)*10)  
                    t=time+4     
                elif Dropepoint=='E':
                    e=100+((15-5)*10)   
                    t=time+5
                else:
                    print("cant reachable")  


        else:
            print("not reachable")
            flag=True
        if not flag:
            
            cls.taxi[key_min]['point'] = Dropepoint
            cls.taxi[key_min]['earning']+=e  
            cls.id+=1
            cls.booked_passengers[cls.id]={'taxi':key_min,'name':name,'pick':pickuppoint,'drop':Dropepoint,'pickuptime':time,'dropetime':t,'amount':e}
            cls.option()   

    @classmethod
    def display(cls):
        if cls.taxi:
            for i, j in cls.taxi.items():
                print(i,j['earning'])
                if cls.booked_passengers:
                    for k,l in cls.booked_passengers.items():
                        if l['taxi']==i:
                            print(f'{k} {k} {l["pick"]} {l["drop"]} {l["pickuptime"]} {l["dropetime"]} {l["amount"]}')

        cls.option()

if __name__ == "__main__":
    taxi.option()                       


               







                



    
        
        




        