import Tkinter as tk
import os, time, datetime, pyperclip

def center(toplevel): # Function for centering all windows upon execution.
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth() #Find width resolution
    h = toplevel.winfo_screenheight() #Find height resolution
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2 # find the middle of width resolution
    y = h/2 - size[1]/2 # find the middle of height resolution
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

newArrayLog = []

dayStamp = str(datetime.datetime.now().strftime('%m-%d-%y'))
timeStamp =  str(datetime.datetime.now().strftime('%I-%M-%S_%p')) + '.txt' #only once, filename ultimately
cwd = os.getcwd() #current working directory
opj = os.path.join #for windows and linux compatibility in getting complete path of cwd
folderWithTodaysDate = opj(cwd, 'Logs '+dayStamp)  # folder to place all todays scans in

walmartArrayForHomeDecor = ['ATTRIBUTE', 'LISTINGTITLE', 'LONGDESCRIPTION', 'SHELFDESCRIPTION', 'LANTERNREFURB', 'IMAGEURL', #Arbitrary layout of walmart cells in listing spreadsheet.
							'MAINIMAGEALTERNATE', 'ASSETALTTEXT', 'ASSETURL', 'ASSETTYPE', 'ADDITIONALASSETALT', 'ADDITIONALASSETURL', #Format is susceptible to change and will vary depending on listing category.
							'ADDITIONALASSETTYPE', 'ADDITIONALASSETALTTEST', 'ADDITIONALURLASSETTHREE', '', 'UPC', 'UPCNUMBER', '', '', #This is for HomeDecor (Luminara) but obviously would contain different info if Electronics, Lawn/Garden, HBA, etc...
							'', '', 'USD', 'MSRPMEASURE', '', '', '', '', '', '', '', 'INCHES', 'LENGTH', 'INCHES', 'WIDTH', 'INCHES',
							'HEIGHT', 'POUNDS', 'WEIGHT', '2038346', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', 'WARRANTYTEXT', '', '', '', 'WARRANTYLENGTH', '', '', '', '', '', '', '', '', 'CUSTOMSKU', '', '', '',
							'USD', 'SELLFORAMOUNT', 'USD', 'MINSELLFOR', '', 'SHIPWEIGHTVALUE', 'LB', '', '', '', '', '', '', '', '',
							'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', '', '', '', '', 'CATEGORYSPECIFICATTRIBUTES', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', '', '', '', 'BRANDNAME', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']


def createLogFolderFile(): # Create date/time stamped folder/file which contains the raw newArrayLog and a copy w/o brackets, apostrophy, etc...
	if os.path.exists(folderWithTodaysDate) == True: #If file w/ today's date exists, then continue the script.
		pass
	else: #else create the directory with read/write/exe permissions.
		os.makedirs(folderWithTodaysDate, 0666) #read/write permissions for creating files inside python created folder. For Win & Linux.

	createFileInDateDirectory = str(opj(folderWithTodaysDate, timeStamp)) #current file in progress, based on timestamp above
	thisToClipBoardAndXLSX = ','.join(newArrayLog) # Remove brackets, quotes, etc... from array so it can be copy/pasted into spreadsheet, in turn recognized as individual cells delimited by commas.

	with open(createFileInDateDirectory, 'w+') as newSheet: # create the log file, inside dated folder
		newSheet.write(str(newArrayLog)) # write array to file, everytime input is entered. No data loss!
		newSheet.write('\n\n%s\n' % thisToClipBoardAndXLSX) # After log array is written, also write a copy of it that can be identified by spreadsheets when copy/pasted
		newSheet.close() # redundantly and securely close file thats being written to
	pyperclip.copy('\n'+thisToClipBoardAndXLSX+'\n') # copy the stripped version of array to computers clip board for easy transfer to MS Excel, Google Docs or Libre Calc.

class mainApp(tk.Tk): # The core class for creating tkinter GUI
	def __init__(self):
		tk.Tk.__init__(self)
		x = 0
		for everyOption in walmartArrayForHomeDecor:
			if everyOption == '':
				newArrayLog.append('') # append empty to array.
				createLogFolderFile() # write modified array to file
			elif everyOption == 'UPC' or everyOption == 'USD' or everyOption == 'INCHES' or everyOption == 'POUNDS' or everyOption == "2038346" or everyOption == 'LB': # if index is static information (measuring units, tax number, currency) then...
				newArrayLog.append(everyOption) # Change nothing. Write static unit into array.
				createLogFolderFile() # Write modified array to log file.
			else: # otherwise do the following.
				#get = raw_input('What is %s?: ' % str(everyOption)) # For every index/entry in HomeDecor array, ask a question relating to specific index.
				#newArrayLog.append(str(get)) # append user's raw input to log file.
				print ','.join(newArrayLog) # debug/print the contents of clipboard
				createLogFolderFile() # write current/modified array to file.
				makeLabelOption = tk.Label(width=25, anchor='w', relief='ridge', text=str(everyOption+':'))
				makeLabelOption.grid(row=x, column=0, padx=5, pady=1)
				makeInputOption = tk.Entry(width=45)
				makeInputOption.grid(row=x, column=1, padx=5, pady=1)
				x+=1

if __name__ == "__main__":
	root = mainApp()
	root.resizable(0,0) # Not resizeable
	root.geometry("480x675") # Static width/height of tkinter GUI
	center(root) # call Center function on entire frame, so each run is displayed on same monitors coordinates
	root.title('Wally Lister') # Name GUI Window
	root.mainloop()

"""
for everyOption in walmartArrayForHomeDecor: # For every index in HomeDecor Array do the following
	if everyOption == '': # if cell/index is empty
		newArrayLog.append('') # append empty to array.
		createLogFolderFile() # write modified array to file
	elif everyOption == 'UPC' or everyOption == 'USD' or everyOption == 'INCHES' or everyOption == 'POUNDS' or everyOption == "2038346" or everyOption == 'LB': # if index is static information (measuring units, tax number, currency) then...
		newArrayLog.append(everyOption) # Change nothing. Write static unit into array.
		createLogFolderFile() # Write modified array to log file.
	else: # otherwise do the following.
		get = raw_input('What is %s?: ' % str(everyOption)) # For every index/entry in HomeDecor array, ask a question relating to specific index.
		newArrayLog.append(str(get)) # append user's raw input to log file.
		print ','.join(newArrayLog) # debug/print the contents of clipboard
		createLogFolderFile() # write current/modified array to file.
"""