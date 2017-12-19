data = ["Hello", "World"]
try:
    file = open("file_1.txt", 'w')
    file.write(data)

except (TypeError,FileNotFoundError) as err:
    print(err)

finally:
    print("Finally executed...")
    file.close()
