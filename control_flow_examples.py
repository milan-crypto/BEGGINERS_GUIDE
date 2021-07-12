# Control Flow Examples

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
# if 2 == 2:
#     print('These numbers are equal')

"""
Cinema System Age Management
1. If someone is under 12 - U, PG and 12 films are available.
2. If someone is under 15 - U, PG, 12 and 15 films are available.
3. Over 18 - All films are available.
"""

# customer_age = 18
#
# if customer_age <= 12:
#     print('U, PG and 12 films are available.')
# elif customer_age <= 15:
#     print('U, PG, 12 and 15 films are available.')
# else:
#     print('All films are available.')
import random


"""
Chatbot Greetings
1. Between 05:00 - 12:00 - Good Morning
2. Between 12:00 - 18:00 - Good Afternoon
3. Between 18:00 - 00:00 - Good Evening
"""

time_of_day = 2

# Or & And

if time_of_day > 5 and time_of_day < 12:
    print('Good Morning')
elif time_of_day > 12 and time_of_day < 18:
    print('Good Afternoon')
else:
    print('Good Evening')


# passingScore = 65
# studentScore = random.randint(0 , 100)
#
# if studentScore >= passingScore:
#   testResult = True
# else:
#   testResult = False
#
# print(testResult)
