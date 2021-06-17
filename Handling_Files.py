def open_print_file(file):
    try:
        with open(file, "r") as opened_file:
            for line in opened_file.readlines():
                print(line.strip("\n"))
    except:
        print("File cannot be found in the file directory")
        raise
    finally:
        print("\nExecution complete")


open_print_file("order.txt")