file_handler = None

try:
    file_handler = open("my-data.txt", "r+")
    file_reading = file_handler.read()
    print(file_reading)
except FileNotFoundError as e:
    print(f"Error: {e}")
except IOError as e:
    print(f"An I/O error occurred: {e}")
finally:
    if file_handler is not None:
        file_handler.close()
