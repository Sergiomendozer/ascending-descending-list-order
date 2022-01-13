class color:
   BOLD = '\033[1m'
   END = '\033[0m'
try:
    inp = input("Choose"+color.BOLD+" asc "+color.END+"or"+color.BOLD+" desc "+color.END+"or"+ color.BOLD+" both "+color.END+ ", asc is for ascending order and desc is for descending order:")
    if inp == "asc":
        try:
            my_list = []
            while True:
                my_list.append(int(input("input the numbers you would like in ascending order,after each number press enter, when you want to stop enter stop:")))
                my_list.sort()
                print (my_list)
        except:
            print(my_list)

    if inp == "desc":
        try:
            my_list = []
            while True:
                my_list.append(int(input("input the numbers you would like in descending order,after each number press enter, when you want to stop enter stop:")))
                my_list.sort(reverse=True)
                print (my_list)
        except:
            print(my_list)
    if inp == "both":
        try:
            my_list = []
            while True:
                my_list.append(int(input("input the numbers you would like in ascending and descending order,after each number press enter, when you want to stop enter stop:")))
                my_list.sort(reverse=True)
                print (my_list)

            my_list2 = []
            while True:
                my_list2.append(int(input("input the numbers you would like in ascending order,after each number press enter, when you want to stop enter stop:")))
                my_list2.sort()
                print (my_list2)
        except:
            print(my_list + my_list2)
except ValueError:
    print("You must enter either"+color.BOLD+ " asc " +color.END+"or"+color.BOLD+" desc "+color.END)