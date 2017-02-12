walmartArrayForCategory = ['ATTRIBUTE', 'LISTINGTITLE', 'LONGDESCRIPTION', 'SHELFDESCRIPTION', 'LANTERNREFURB', 'IMAGEURL','MAINIMAGEALTERNATE', 'ASSETALTTEXT', 'ASSETURL', 'ASSETTYPE', 'ADDITIONALASSETALT', 'ADDITIONALASSETURL','ADDITIONALASSETTYPE', 'ADDITIONALASSETALTTEST', 'ADDITIONALURLASSETTHREE', '', 'UPC', 'UPCNUMBER', '', '','', '', 'USD', 'MSRPMEASURE', '', '', '', '', '', '', '', 'INCHES', 'LENGTH', 'INCHES', 'WIDTH', 'INCHES','HEIGHT', 'POUNDS', 'WEIGHT', '2038346', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', 'WARRANTYTEXT', '', '', '', 'WARRANTYLENGTH', '', '', '', '', '', '', '', '', 'CUSTOMSKU', '', '', '','USD', 'SELLFORAMOUNT', 'USD', 'MINSELLFOR', '', 'SHIPWEIGHTVALUE', 'LB', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', 'CATEGORYSPECIFICATTRIBUTES', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', 'BRANDNAME', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

getInputArray = []
number = 1

def createHeader():
	with open('generatedGUI.py', 'w+') as header:
		header.write("""import Tkinter as tk
import pyperclip

def center(toplevel): # Function for centering all windows upon execution.
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth() #Find width resolution
    h = toplevel.winfo_screenheight() #Find height resolution
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2 # find the middle of width resolution
    y = h/2 - size[1]/2 # find the middle of height resolution
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

class mainApp(tk.Tk): # The core class for creating tkinter GUI
	def __init__(self):
		tk.Tk.__init__(self)

		def getInput():
			inputArray = %REPLACEMEARRAY%
			with open('walmartArrayForCategory.txt', 'r+') as getList:
				
				stringFromCatFile = getList.read()
				convertToArray = stringFromCatFile.split(",")

			finalArray = []
			x = 0

			for each in convertToArray:
				if each == 'UPC' or each == 'USD' or each == 'INCHES' or each == 'POUNDS' or each == '2038346' or each =='LB':
					with open('finalFile.txt', 'w+') as final:
						finalArray.append(each)
						final.write(str(finalArray))
					continue
					
				elif each == '':
					with open('finalFile.txt', 'w+') as final:
						finalArray.append(each)
						final.write(str(finalArray))
						continue

				else:
					try:
						with open('finalFile.txt', 'w+') as final:
							finalArray.append(inputArray[x])
					except:
						pass
				x += 1
			thisToClipAndXLSX = ','.join(finalArray)
			pyperclip.copy('\\n'+thisToClipAndXLSX+'\\n')
			print 'copied to clipboard'
			print thisToClipAndXLSX

		self.bind('<Return>', (lambda event: getInput()))

		getAllInputs0 = tk.Button(text='Gather Inputs', width=65, command=lambda: getInput())
		getAllInputs0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
""")
		header.close()

def createBody():
	with open('generatedGUI.py', 'a+') as body:
		body.write("""
		label%s = tk.Label(width=25, anchor='w', relief='ridge', text="%s")
		label%s.grid(row=%s, column=0, padx=5, pady=1)
		entry%s = tk.Entry(width=45)
		entry%s.grid(row=%s, column=1, padx=5, pady=1)
""" % (number, everyOption, number, number, number, number, number))
		body.close()

def createEnder():
	with open('generatedGUI.py', 'a+') as ender:
		ender.write("""
if __name__ == "__main__": # compile the main class/widgets to be displayed on screen.
	root = mainApp()
	root.resizable(0,0)
	center(root)
	root.title('Wally Lister')
	root.mainloop()
""")
		ender.close()

createHeader()
for everyOption in walmartArrayForCategory:
	if everyOption in ['UPC','USD','INCHES','POUNDS',"2038346",'LB']:
		pass
	elif everyOption == '':
		pass
	else:
		getInputArray.append('entry%s.get()' % number)
		with open('arrayLog.txt', 'w+') as arrayLogging:
			arrayLogging.write(str(getInputArray))
		createBody()
		number += 1

with open('generatedGUI.py', 'r') as replaceArray:
	with open('arrayLog.txt', 'r') as rawArray:
			reading = replaceArray.read()
			readRawArray = rawArray.read()
			replacement = reading.replace('%REPLACEMEARRAY%', readRawArray.replace("'", ""))

with open('generatedGUI.py', 'r+') as newfile:
	newfile.write(str(replacement))
createEnder()

#with open('whiteListedArray.txt', 'r') as whiteListedArray:
#readWhite = whiteListedArray.read()
#replacement = replacement.replace('%WHITELISTARRAY%', str(readWhite.split(',')))