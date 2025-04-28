def make_guest_list():
    guest_list = []
    while True:
        add_guest = input()

        if add_guest == '.':
            print(guest_list)
            print(len(guest_list))
            break

        guest_list.append(add_guest)

make_guest_list()