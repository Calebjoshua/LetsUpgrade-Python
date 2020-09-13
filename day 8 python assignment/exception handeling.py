file = open("cj.txt", "w")
file.write("hi")
file.close()

file= open("cj.txt", "r")
try:
    file.write("hello")
    file.close()
except Exception as e:
    print(e)