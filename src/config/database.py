def in_memory_db():
    print("Initialising in memory db.......")
    demo_db = open("demo_db.txt", "w")
    if (demo_db):
        print("In memory db is intialised")
    else:
        print("In memory db failed to initialise")