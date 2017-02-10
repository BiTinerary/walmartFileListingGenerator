import os, csv, time, datetime, pyperclip

newArrayLog = []

dayStamp = str(datetime.datetime.now().strftime('%m-%d-%y'))
timeStamp =  str(datetime.datetime.now().strftime('%I-%M-%S_%p')) + '.txt' #only once, filename ultimately
cwd = os.getcwd() #current working directory
opj = os.path.join #for windows and linux compatibility in getting complete path of cwd
folderWithTodaysDate = opj(cwd, 'Logs '+dayStamp)  # folder to place all todays scans in

walmartArrayForHomeDecor = ['ATTRIBUTE', 'LISTINGTITLE', 'LONGDESCRIPTION', 'SHELFDESCRIPTION', 'LANTERNREFURB', 'IMAGEURL',
							'MAINIMAGEALTERNATE', 'ASSETALTTEXT', 'ASSETURL', 'ASSETTYPE', 'ADDITIONALASSETALT', 'ADDITIONALASSETURL',
							'ADDITIONALASSETTYPE', 'ADDITIONALASSETALTTEST', 'ADDITIONALURLASSETTHREE', '', 'UPC', 'UPCNUMBER', '', '',
							'', '', 'USD', 'MSRPMEASURE', '', '', '', '', '', '', '', 'INCHES', 'LENGTH', 'INCHES', 'WIDTH', 'INCHES',
							'HEIGHT', 'POUNDS', 'WEIGHT', '2038346', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', 'WARRANTYTEXT', '', '', '', 'WARRANTYLENGTH', '', '', '', '', '', '', '', '', 'CUSTOMSKU', '', '', '',
							'USD', 'SELLFORAMOUNT', 'USD', 'MINSELLFOR', '', 'SHIPWEIGHTVALUE', 'LB', '', '', '', '', '', '', '', '',
							'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', '', '', '', '', 'CATEGORYSPECIFICATTRIBUTES', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', '', '', '', 'BRANDNAME', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
							'', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

#Arbitrary layout of walmart cells in listing spreadsheet. Format is susceptible to change and will vary depending on listing category.
#This is for HomeDecor (Luminara) but obviously would contain different info and variables if listing in Electronics, Lawn/Garden, HBA, etc...

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