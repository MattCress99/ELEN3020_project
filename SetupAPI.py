import os


def CreateLogsFolder():
    try:
        os.mkdir('Logs')
        print("Logs folder was not found and was created automatically")
    except:
        print("Folder creation failed, either the folder exists or failed to create")

def CreateInvoicesFolder():
    try:
        os.mkdir('Invoices')
        print("Invoices folder was not found and was created automatically")
    except:
        print("Folder creation failed, either the folder exists or failed to create")
    f = open("Invoices/InvoiceIndex", "a+")
    f.close()

def CreateToAddFolder():
    try:
        os.mkdir('ToAdd')
        print("ToAdd folder was not found and was created automatically")
    except:
        pass
    

def CreateSampleTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS SampleTable(
                                    sampleID TEXT NOT NULL PRIMARY KEY,
                                    boxID TEXT NOT NULL,
                                    boxX INTEGER NOT NULL,     
                                    boxY INTEGER NOT NULL,
                                    boxZ INTEGER NOT NULL,
                                    sampleType TEXT NOT NULL,
                                    originCountry TEXT NOT NULL,
                                    collectionDate TEXT NOT NULL,
                                    entryDate TEXT NOT NULL,
                                    subjectAge INTEGER NOT NULL,
                                    tubeRating INTEGER NOT NULL,
                                    collectionTitle TEXT NOT NULL,
                                    returnType TEXT NOT NULL,
                                    returnDate TEXT NOT NULL,
                                    phenotypeValue TEXT NOT NULL,
                                    diseaseState TEXT NOT NULL,
                                    FOREIGN KEY(boxID) REFERENCES BoxTable(boxID),
                                    FOREIGN KEY(collectionTitle) REFERENCES CollectionTable(collectionTitle))""")
    _conn.commit()
                                    
def CreateCollectionTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS CollectionTable(
                                    collectionTitle TEXT NOT NULL PRIMARY KEY,
                                    donorName TEXT NOT NULL,
                                    donorPhoneNumber TEXT NOT NULL,
                                    donorEmail TEXT NOT NULL,
                                    donorOrganization TEXT NOT NULL,   
                                    authorisorName TEXT NOT NULL,
                                    authorisorPhoneNumber TEXT NOT NULL,
                                    authorisorEmail TEXT NOT NULL,
                                    authorisorOrganization TEXT NOT NULL)""")
    _conn.commit()

def CreateFridgeTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FridgeTable(
                                    fridgeID TEXT NOT NULL PRIMARY KEY,
                                    temperature INTEGER NOT NULL,
                                    numShelves INTEGER NOT NULL,
                                    widthShelves INTEGER NOT NULL)""")
    _conn.commit()

def CreateLoginTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS LoginTable(
                                    username TEXT NOT NULL PRIMARY KEY,
                                    password TEXT NOT NULL,
                                    accessLevel INTEGER NOT NULL,
                                    loggedIn INTEGER NOT NULL)""")
    _conn.commit()                               

def CreateBoxTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS BoxTable(
                                    boxID TEXT NOT NULL PRIMARY KEY,
                                    fridgeID TEXT NOT NULL,
                                    fridgeX INTEGER NOT NULL,
                                    fridgeY INTEGER NOT NULL,
                                    boxX INTEGER NOT NULL,                                    
                                    boxY INTEGER NOT NULL,                                    
                                    boxZ INTEGER NOT NULL,
                                    FOREIGN KEY(fridgeID) REFERENCES FridgeTable(fridgeID))""")
    _conn.commit()  

def CreateSampleTestTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS SampleTestTable(
                                    sampleID TEXT NOT NULL PRIMARY KEY,
                                    testType TEXT NOT NULL,
                                    testResult TEXT NOT NULL,                                    
                                    FOREIGN KEY(sampleID) REFERENCES SampleTable(sampleID))""")
    _conn.commit()


def CreateAllTables(_conn):
    CreateFridgeTable(_conn)
    CreateBoxTable(_conn)
    CreateSampleTable(_conn)
    CreateLoginTable(_conn)
    CreateSampleTestTable(_conn)
    CreateCollectionTable(_conn)
    CreateLogsFolder()
    CreateInvoicesFolder()
    CreateToAddFolder()

#JESSE'S COMMENT
