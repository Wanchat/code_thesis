from test import angle
from test_2_distance import distance
from test_blink import blink

while True:
    print ("\n | distance 1 | angle  2 | blink 3 | quit any key |")
    try:
        choice = int(input(" entry key : "))
        if choice == 1:
            print(" >> distance")
            distance()
        elif choice == 2:
            print(" >> angle")
            angle()
        elif choice == 3:
            print(" >> blink")
            blink()
        else:
            print(" >> quit")
            break
    except ValueError as err:
        pass
        print("\n Valueerror: {0}".format(err))
        print(" ** please entry number **\n")


