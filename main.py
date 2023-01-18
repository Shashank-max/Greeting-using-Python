import time
timestamp = time.strftime('%H, %M, %S')
print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
# timestamp = int(time.strftime('%M'))
# print(timestamp)
# timestamp = int(time.strftime('%S'))
# print(timestamp)

if (0 < timestamp < 12):
    print("Good Morninng")
elif (12 <= timestamp < 18):
    print("Good Afternoon")
elif (18 <= timestamp < 22):
    print("Good Evening")
elif (22 <= timestamp < 0):
    print("Good Night")
