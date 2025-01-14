elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]
#print("Elements:", elements)

#git add . &

# def function_name():
#     return True;

def say_greeting(name, message="hi"):
    print(f" {message}, {name}")

say_greeting("Mansi","Ssup")

def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(print))
        except ValueError:
            print("Please enter a valid integer")
            continue
