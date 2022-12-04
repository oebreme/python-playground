parkingLot = [0, 1, 1, 0, 0, 2, 0, 1, 2, 0]
status = ""


def define_status_text(e):
    global status
    if e == 0:
        status = "frei"
    elif e == 1:
        status = "reserviert"
    elif e == 2:
        status = "belegt"
    else:
        status = ":("


while True:
    for index, parkingSpace in enumerate(parkingLot):
        define_status_text(parkingSpace)
        print("Parkplatz " + str(index) + " ist " + status)
    print("\n\nEingabe")
    print("-----------" + "\n")
    statusChange = int(input("Status (0-2): "))
    parkingSpaceChange = int(input("ParkplatzNr. (1-10): "))

    define_status_text(statusChange)

    parkingLot[parkingSpaceChange] = statusChange
    print("Parkplatz " + str(parkingSpaceChange) + " wurde " + status + "\n\n")
    print("\n" * 50)
