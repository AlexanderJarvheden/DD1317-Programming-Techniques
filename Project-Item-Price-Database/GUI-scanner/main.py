from file_management import File_input_GUI
from store import Store
from receipt_management import ScannerGUI

def main():
    store = Store()
    filemanagement = File_input_GUI(store)
    ScannerGUI(store, filemanagement.filename)


if __name__ == "__main__":
    main()