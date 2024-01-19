import sys

if len(sys.argv) != 2:
    print("Usage: python myscript.py param1")
    #sys.exit(1)

print("python vars")
print(sys.argv)

for arg in sys.argv:
    print(arg)

whoToGreet = sys.argv[1]

print(f"Greeting : {whoToGreet}")