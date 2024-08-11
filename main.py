import os

def create_files(directory, filename):
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, 'x') as f:
            print(f"File '{filename}' created successfully in '{directory}'!")
    except FileExistsError:
        print(f"File '{filename}' already exists in '{directory}'!")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_files(directory):
    try:
        files = os.listdir(directory)
        if not files:
            print(f'No files found in {directory}.')
        else:
            print(f'Files in Directory {directory}:')
            for file in files:
                print(file)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_files(directory, filename):
    filepath = os.path.join(directory, filename)
    try:
        os.remove(filepath)
        print(f"'{filename}' has been deleted successfully from '{directory}'!")
    except FileNotFoundError:
        print(f"File '{filename}' not found in '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file(directory, filename):
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}' in '{directory}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' doesn't exist in '{directory}'!")
    except Exception as e:
        print(f"An error occurred: {e}")

def edit_file(directory, filename):
    filepath = os.path.join(directory, filename)
    try:
        with open(filepath, 'a') as f:
            content = input('Enter the data to add: ')
            f.write(content + "\n")
            print(f"Content added to '{filename}' in '{directory}' successfully!")
    except FileNotFoundError:
        print(f"File '{filename}' doesn't exist in '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print('\nFILE MANAGEMENT SYSTEM')
        print('1: List all files in a directory')
        print('2: Create File')
        print('3: Delete File')
        print('4: Read File')
        print('5: Edit File')
        print('6: Exit')

        directory = input('Enter the directory path: ')
        choice = input('Enter your choice (1-6): ')

        if choice == '1':
            view_all_files(directory)

        elif choice == '2':
            filename = input("Enter the file name to create: ")
            create_files(directory, filename)

        elif choice == '3':
            filename = input("Enter the file name to delete: ")
            delete_files(directory, filename)

        elif choice == '4':
            filename = input("Enter the file name to read: ")
            read_file(directory, filename)

        elif choice == '5':
            filename = input("Enter the file name to edit: ")
            edit_file(directory, filename)

        elif choice == '6':
            print('Closing the app...')
            break

        else:
            print('Invalid choice. Please choose a valid option.')

if __name__ == "__main__":
    main()
