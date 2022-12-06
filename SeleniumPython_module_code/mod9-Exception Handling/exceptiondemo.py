# x = input("Enter num 1 : ")
# y = input("Enter num 2 : ")
#
# try:
#     result = int(x)/int(y)
# except Exception as e:
#     print(e)
#     result = None
# except ZeroDivisionError as z:
#     print(z)
#     result = None
# except ValueError as a:
#     print("division ont possible")
# finally:
#     print(result)

#files : txt, excel, etc
#file not found, permission error
try:
    path = "D:\Jaspreet\demo.txt"
    filepath = open(path, "w")
    filepath.write("Exception handling for files......")
    filepath = open(path, "r")
    print(filepath.read())
except Exception as e:
    print(e)
finally:
    try:
        filepath.close()
    except Exception as e:
        print(e)


