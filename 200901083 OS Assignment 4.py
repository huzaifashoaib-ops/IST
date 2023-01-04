import threading

def get_input():
  global string
  string = input("Enter the string: ")

def reversed_string(string):
  print("Reversed String is: ",string[::-1])

def uppercase(string):
  print("Capatalized String is: ", string.upper())

def shift_string(string, x):
  shifted_string = ""
  for var in string:

    shifted_char = chr(ord(var) + x)

    shifted_string += shifted_char
  print("Shifted String: ",shifted_string)

input_thread = threading.Thread(target=get_input)

input_thread.start()

input_thread.join()

reversed_thread = threading.Thread(target=reversed_string, args=(string,))
uppercase_thread = threading.Thread(target=uppercase, args=(string,))
shifted_thread = threading.Thread(target=shift_string, args=(string, 2))


reversed_thread.start()
uppercase_thread.start()
shifted_thread.start()


reversed_thread.join()
uppercase_thread.join()
shifted_thread.join()
