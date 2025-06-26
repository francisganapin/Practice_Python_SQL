light = input("Enter traffic light color ( red,yellow,green): ").lower()


if light == "red":
    print("Stop!")
elif light == 'yellow':
    print('slow down')
elif light == 'green':
    print("Go!")
else:
    print("Invalid Color")