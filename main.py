mode = input("Select you mode : ")

if mode == "1":
    exec(open("mode1.py").read())
elif mode == "2":
    exec(open("mode2.py").read())
else:
    print("Error")

for i in range(20):
    print("Hello")