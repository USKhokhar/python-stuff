def tower_hanoi(number, src, des, aux):
    if number == 1:
        print(f"Move disk 1 from {src} to {des}")
        return
    tower_hanoi(number-1, src, aux, des)
    print(f"Move disk {number} from {src} to {des}")
    tower_hanoi(number-1, aux, des, src)


number = 6
tower_hanoi(number, 'A', 'B', 'C')