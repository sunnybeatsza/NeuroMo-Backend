import os

def file_based_db():
    db_file = "demo_db.txt"
    
    if os.path.exists(db_file):
        print("File based db already exists\n")
    else:
        print("Initialising file based db.......\n")
        demo_db = open(db_file, "w")
        if (demo_db):
            print("File based db is intialised\n")
            demo_db.close()
        else:
            print("In file based db failed to initialise\n")