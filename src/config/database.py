def file_based_db():
    print("Initialising file based db.......\n")
    demo_db = open("demo_db.txt", "w")
    if (demo_db):
        print("File based db is intialised\n")
    else:
        print("In file based db failed to initialise\n")