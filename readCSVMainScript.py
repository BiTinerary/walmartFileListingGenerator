import os, csv, time, datetime, pyperclip

newArrayLog = []

dayStamp = str(datetime.datetime.now().strftime('%m-%d-%y'))
timeStamp =  str(datetime.datetime.now().strftime('%I-%M-%S_%p')) + '.txt' #only once, filename ultimately
cwd = os.getcwd() #current working directory
opj = os.path.join #more magic - OS PATH JOIN = opj, for windows and linux compatibility
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

def createLogFolderFile():
	if os.path.exists(folderWithTodaysDate) == True: #If file w/ today's date exists, then continue the script.
		pass
	else: #else create the directory with read/write/exe permissions.
		os.makedirs(folderWithTodaysDate, 0666) #read/write permissions for creating files inside python created folder. For Win & Linux.

	createFileInDateDirectory = str(opj(folderWithTodaysDate, timeStamp)) #current file in progress, based on timestamp above
	thisToClipBoardAndXLSX = ','.join(newArrayLog)

	with open(createFileInDateDirectory, 'w+') as newSheet:
		newSheet.write(str(newArrayLog))
		newSheet.write('\n\n%s\n' % thisToClipBoardAndXLSX)
		newSheet.close()
	pyperclip.copy('\n'+thisToClipBoardAndXLSX+'\n')

for everyOption in walmartArrayForHomeDecor:
	if everyOption == '':
		newArrayLog.append('')
		createLogFolderFile()
	elif everyOption == 'UPC' or everyOption == 'USD' or everyOption == 'INCHES' or everyOption == 'POUNDS' or everyOption == "2038346" or everyOption == 'LB':
		newArrayLog.append(everyOption)
		createLogFolderFile()
	else:
		get = raw_input('What is %s?: ' % str(everyOption))
		newArrayLog.append(str(get))
		print ','.join(newArrayLog)
		createLogFolderFile()

# Read CSV and convert to pythonic array, complete with appropriately places brackets, commas, and quote syntax.
# To be used for other WalMart categories that will have different cells relating to products and/or have simlar cells placed in different indexes.

""" 
with open('CSVTemplate.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		print row[0:]
		with open('withArraySyntax.txt', 'w+') as dlp:
			dlp.write(str(row[0:]))
"""