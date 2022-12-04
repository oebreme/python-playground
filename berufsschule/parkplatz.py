# import numpy as np

# brr = np.empty(10, None)
#
# print(brr)

# arr = [None] * 10
#
# print(arr)
#


parkingLot = [0, 1, 1, 0, 0, 2, 0, 1, 2, 0]
blob = True
status = ""
iterator = iter(parkingLot)

statusChange = ""
parkingSpaceChange = ""


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


while blob:
    for index, parkingSpace in enumerate(parkingLot):
        define_status_text(parkingSpace)
        print("Parkplatz " + str(index) + " ist " + status + "\n\n")
    print("Eingabe")
    print("-----------" + "\n")
    statusChange = input("Status (0-2): ")
    parkingSpaceChange = input("ParkplatzNr. (1-10): ")

    statusChange = int(statusChange)

    define_status_text(statusChange)

    parkingLot[int(parkingSpaceChange)] = statusChange
    print("Parkplatz " + parkingSpaceChange + " wurde " + status + "\n\n")
    print("\n" * 50)
