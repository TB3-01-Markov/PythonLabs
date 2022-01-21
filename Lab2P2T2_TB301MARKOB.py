# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

filename = 'lab2p22.txt'
with open(filename, 'r') as file:
   # file = open(r'lab2p22.txt', 'r')
    data = file.read()
    lines = data.split()
    number_of_words = 0
    number_of_words += len(lines)
    print(number_of_words, ' words in file ', filename)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    f = open(filename, "w+")
    f.write("Lab #2.  Part 2.  Task 2. \nCreate a class that performs statistical processing of a text file - counting characters, words, sentences, etc. Determine the required attributes-data and attributes-methods in class for working with the text file.")

    print(f'HELLO, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('MARKOB from TB301')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
