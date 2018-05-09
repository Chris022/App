try:
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
except ImportError:
     raise ImportError('You need to install two librarys by usning         pip install gspread oauth2client ')
    
    
    
scope = []
creds = None
client = None
sheet = None

def getClient():
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json',scope)
        client = gspread.authorize(creds)
        return client
    except:
        raise NameError("Have you downloaded the jason file form google Api-Manager and named it client_secret.json.\n Also you have to put it in the same folder as this file" )

def getSheet(name,client,count):
    try:
        sheet = client.open(name).get_worksheet(count)
        return sheet
    except:
        raise NameError("The Project with the name "+name+"does not exists" )
        
def addRow(row,data,sheet):
    sheet.insert_row(data,row)
    
def changeRow(row,data,sheet):
    sheet.delete_row(row)
    sheet.insert_row(data,row)

def getRow(row,sheet):
    return (sheet.row_values(row))

def clearRow(row,sheet):
    sheet.delete_row(row)
    
def search(sheet,txt):
    return(sheet.findall(txt))

def getColAndRowOf(cell):
    return (cell.col,cell.row)

def getRowOf(cell):
    return cell.row

def setCell(row,col,val,s):
    s.update_cell(row,col,val)
    
def getCell(row,col,s):
    return s.cell(row,col).value

c = getClient()

s = getSheet("Testing 2018",c,0)

def getExercises(s,txt):
    x = []
    cells = search(s,txt)
    for y in cells:
        x.append(getRow(getRowOf(y),s))
    return x


print(getExercises(s,"Mathematik"))
print(getCell(2,17,s))