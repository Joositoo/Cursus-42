def ft_print_harvest(current_day, harvest_day):
    if (current_day > harvest_day):
        print("Harvest time!")
    else:
        print(f"Day {current_day}")
        ft_print_harvest(current_day + 1, harvest_day)


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    ft_print_harvest(1, day)
