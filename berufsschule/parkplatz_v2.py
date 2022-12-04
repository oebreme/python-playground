parkingLot = [0, 1, 1, 0, 0, 2, 0, 1, 2, 0]
status = ""
continue_readNewStatus = True
continue_readParkingSpace = True


def validate_status(e):
    global continue_readNewStatus
    if 2 >= e >= 0:
        continue_readNewStatus = False
        return e
    else:
        return print("Bitte eine Eingabe zwischen 0 - 2")


def validate_parkinglot(e):
    global continue_readParkingSpace
    if 9 >= e >= 0:
        continue_readParkingSpace = False
        return e
    else:
        return print("Bitte eine Eingabe zwischen 0 - 9")


def read_new_status():
    return int(input("Status (0-2): "))


def read_parkinglot():
    return int(input("ParkplatzNr. (0-9): "))


def print_parking_spaces(e):
    global status
    if e == 0:
        status = "frei"
    elif e == 1:
        status = "reserviert"
    elif e == 2:
        status = "belegt"


def reset_validation():
    global continue_readNewStatus
    global continue_readParkingSpace
    continue_readNewStatus = True
    continue_readParkingSpace = True


while True:
    for index, parkingSpace in enumerate(parkingLot):
        print_parking_spaces(parkingSpace)
        print("Parkplatz " + str(index) + " ist " + status)
    print("\n\nEingabe")
    print("-----------" + "\n")

    while continue_readNewStatus:
        statusChange = read_new_status()
        validate_status(statusChange)
    while continue_readParkingSpace:
        parkingSpaceChange = read_parkinglot()
        validate_parkinglot(parkingSpaceChange)

    print_parking_spaces(statusChange)

    parkingLot[parkingSpaceChange] = statusChange
    print("Parkplatz " + str(parkingSpaceChange) + " wurde " + status + "\n\n")
    print("\n" * 50)

    reset_validation()
