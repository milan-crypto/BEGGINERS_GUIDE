# Functions

# DRY Don't repeat yourself

def full_name(first_name, last_name):
    return first_name + ' ' + last_name

def print_name(data_type):
    print(data_type)

# print(full_name("Milan", "Cosgrove"))
print_name(full_name("Milan", "Cosgrove"))
