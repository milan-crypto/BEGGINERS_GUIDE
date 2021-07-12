"""
Booleans and equality operators

    Operator  |         Meaning                      |          Example              |
        ==    |      Equal to                        |       4 == 4 (True)           |
        !=    |      Not equal to                    |       4 != 3 (True)           |
        >     |      Greater than                    |       3 > 4 (False)           |
        <     |      Less than                       |       3 < 4 (True)            |
        >=    |      Greater than or equal to        |       5 >= 5 (True)           |
        <=    |      Less than or equal to           |       5 <= 4 (False)          |

"""

# loop_control = True

counter = 0

while counter < 10:
    if counter % 2 == 0:
        print(counter)
    else:
        print("Odd number")
    counter += 1



