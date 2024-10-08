binary_read = None
cp_file = None

try:
    binary_read = open("Screenshot 2024-02-18 193359.png", "rb")
    file_reading = binary_read.read()
    cp_file = open("ss.jpg", "wb")
    cp_file.write(file_reading)
except Exception as e:
    raise e
finally:
    binary_read.close()
    cp_file.close()
