Zim_Tourist_Destinations=["Victoria Falls","Kariba","Nyanga"]
Travel_Options=["Car Rental","Chauffer Driven","Transfer","Bus","Flight"]
Travel_Packages=["Victoria Falls Couples Safari","Victoria Falls Family's Safari","Kariba Couples'Safari", "Kariba Family's Safari","Nyanga Couples'Safari", "Nyanga Family's Safari"]
input("Name: ")
input("Email Address: ")
input("Home Address: ")
input("Telephone Number: ")
input("Number of people in group: ")
def Tourist_Destination():
    print("""
    [1]=Victoria Falls
    [2]=Kariba
    [3]=Nyanga
    """)
    Destination_Choice=input("Please select choice of preferred destination from the list above!!:  ")
    if Destination_Choice=='1':
        print("Victoria Falls is 878KM from Harare!")
    elif Destination_Choice=='2':
        print("Kariba is 141KM from Harare!")
    elif Destination_Choice=='3':
        print("Nyanga is 268KM from Harare")
    else:
        print("No valid Destination was selected!")
Tourist_Destination( )
def Travelling_Options():
    print("""
    [1]=Car Rental
    [2]=Chauffer
    [3]=Bus
    [4]=Transfer
    [5]=Flight
    """)
    Travel_Choice=input("Please select choice of preferred Travelling Option from the list above!!:  ")
    if Travel_Choice=='1':
        print("Car Rental to Victoria Falls cost $100/day, Car Rental to Kariba costs $50/day & Car Rental to Nyanga costs $75/day!")
    elif Travel_Choice=='2':
        print("Chauffer driven cars to Victoria Falls cost $500/day, Car Rental to Kariba costs $200/day & Car Rental to Nyanga costs $350/day!")
    elif Travel_Choice=='3':
        print("Bus to Victoria Falls cost $35/person, Bus to Kariba costs $25/person & Bus to Nyanga costs $30/person!")
    elif Travel_Choice=='4':
        print("Transfers for groups to Victoria Falls cost $600/group, Transfers to Kariba costs $300/group & Transfers to Nyanga costs $450/day!")
    elif Travel_Choice=='5':
        print("Flights to Victoria Falls cost $200/person, Flights to Kariba costs $100/person & Flights to Nyanga costs $150/person!")
    else:
        print("No valid Travelling option was selected!")
Travelling_Options()
def Holiday_Packages():
    print("""
    [a]=Single Person's Package Victoria Falls
    [b]=Couples'Package Victoria Falls
    [c]=Family's Package Victoria Falls
    [d]=Single Person's Package Kariba
    [e]=Couples'Package Kariba
    [f]=Family's Package Kariba
    [g]=Single Person's Package Nyanga
    [h]=Couples'Package Nyanga
    [i]=Family's Package Nyanga
    """)
    Package_Choice=input("Please select choice of preferred Package from the list above!!:  ")
    if Package_Choice=='a':
        print("This package is worth $500.00!")
    elif Package_Choice=='b':
        print("This package is worth $1000.00!")
    elif Package_Choice=='c':
        print("This package is worth $1500.00 for a family of 3.Add $500 for every additional person!")
    elif Package_Choice=='d':
        print("This package is worth $300.00!")
    elif Package_Choice=='e':
        print("This package is worth $6000.00!") 
    elif Package_Choice=='f':
        print("This package is worth $900.00 for a family of 3.Add $300 for every additional person!")
    elif Package_Choice=='g':
        print("This package is worth $450.00!")
    elif Package_Choice=='h':
        print("This package is worth $900.00!") 
    elif Package_Choice=='i':
        print("This package is worth $1350.00 for a family of 3.Add $450 for every additional person!")
    else:
        print("No valid Package was selected!") 
Holiday_Packages()

