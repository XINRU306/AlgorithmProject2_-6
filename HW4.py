class My_Queue:
    def __init__(self, data_type):
        self.data_type = data_type
        self.queue = []
        # Index of the rear element to add element
        self.index = -1
        # Initialize number to 0 to count the number of queue
        self.number = 0

    # Define push function to add element into queue
    def push(self, element):
        # The default input type of python ia string
        # So if the input data are all digit,convert it to integer.
        if element.isdigit():
           element = int(element)
        if isinstance(element, self.data_type):
            self.index += 1
            self.queue[self.index:] = [element]
            self.number += 1
            print(self.queue)
        else:
            print("Wrong data type is entered")

    # Define pop function to delete the head element og queue
    def pop(self):
        if self.queue:
            popped_element = self.queue[0]
            print("Popped Element:", popped_element)
            # Remove the head element
            self.queue = self.queue[1:]
            self.number -= 1
        else:
            print("There is no element in the queue")

    # Print the total number of elements in the queue
    def count(self):
        print("Total number of elements in the queue:", self.number)


def main():
    # Display the options of input type
    data_type_option = input("Select data type (a for Integer, b for String): ")
    if data_type_option == 'a':
        data_type = int
    elif data_type_option == 'b':
        data_type = str
    else:
        print("Invalid data type selection")
        return

    my_queue = My_Queue(data_type)

    # Display the options of functions
    while True:
        print("\nMain Menu:")
        print("a. push")
        print("b. pop")
        print("c. count")
        print("d. end")
        choice = input("Enter your choice: ")

        if choice == 'a':
            element = input("Enter an element to push: ")
            my_queue.push(element)
        elif choice == 'b':
            my_queue.pop()
        elif choice == 'c':
            my_queue.count()
        elif choice == 'd':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()