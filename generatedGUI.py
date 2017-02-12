import Tkinter as tk
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
			inputArray = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get(), entry9.get(), entry10.get(), entry11.get(), entry12.get(), entry13.get(), entry14.get(), entry15.get(), entry16.get(), entry17.get(), entry18.get(), entry19.get(), entry20.get(), entry21.get(), entry22.get(), entry23.get(), entry24.get(), entry25.get(), entry26.get(), entry27.get(), entry28.get(), entry29.get()]
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
			pyperclip.copy('\n'+thisToClipAndXLSX+'\n')
			print 'copied to clipboard'
			print thisToClipAndXLSX

		self.bind('<Return>', (lambda event: getInput()))

		getAllInputs0 = tk.Button(text='Gather Inputs', width=65, command=lambda: getInput())
		getAllInputs0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

		label1 = tk.Label(width=25, anchor='w', relief='ridge', text="ATTRIBUTE")
		label1.grid(row=1, column=0, padx=5, pady=1)
		entry1 = tk.Entry(width=45)
		entry1.grid(row=1, column=1, padx=5, pady=1)

		label2 = tk.Label(width=25, anchor='w', relief='ridge', text="LISTINGTITLE")
		label2.grid(row=2, column=0, padx=5, pady=1)
		entry2 = tk.Entry(width=45)
		entry2.grid(row=2, column=1, padx=5, pady=1)

		label3 = tk.Label(width=25, anchor='w', relief='ridge', text="LONGDESCRIPTION")
		label3.grid(row=3, column=0, padx=5, pady=1)
		entry3 = tk.Entry(width=45)
		entry3.grid(row=3, column=1, padx=5, pady=1)

		label4 = tk.Label(width=25, anchor='w', relief='ridge', text="SHELFDESCRIPTION")
		label4.grid(row=4, column=0, padx=5, pady=1)
		entry4 = tk.Entry(width=45)
		entry4.grid(row=4, column=1, padx=5, pady=1)

		label5 = tk.Label(width=25, anchor='w', relief='ridge', text="LANTERNREFURB")
		label5.grid(row=5, column=0, padx=5, pady=1)
		entry5 = tk.Entry(width=45)
		entry5.grid(row=5, column=1, padx=5, pady=1)

		label6 = tk.Label(width=25, anchor='w', relief='ridge', text="IMAGEURL")
		label6.grid(row=6, column=0, padx=5, pady=1)
		entry6 = tk.Entry(width=45)
		entry6.grid(row=6, column=1, padx=5, pady=1)

		label7 = tk.Label(width=25, anchor='w', relief='ridge', text="MAINIMAGEALTERNATE")
		label7.grid(row=7, column=0, padx=5, pady=1)
		entry7 = tk.Entry(width=45)
		entry7.grid(row=7, column=1, padx=5, pady=1)

		label8 = tk.Label(width=25, anchor='w', relief='ridge', text="ASSETALTTEXT")
		label8.grid(row=8, column=0, padx=5, pady=1)
		entry8 = tk.Entry(width=45)
		entry8.grid(row=8, column=1, padx=5, pady=1)

		label9 = tk.Label(width=25, anchor='w', relief='ridge', text="ASSETURL")
		label9.grid(row=9, column=0, padx=5, pady=1)
		entry9 = tk.Entry(width=45)
		entry9.grid(row=9, column=1, padx=5, pady=1)

		label10 = tk.Label(width=25, anchor='w', relief='ridge', text="ASSETTYPE")
		label10.grid(row=10, column=0, padx=5, pady=1)
		entry10 = tk.Entry(width=45)
		entry10.grid(row=10, column=1, padx=5, pady=1)

		label11 = tk.Label(width=25, anchor='w', relief='ridge', text="ADDITIONALASSETALT")
		label11.grid(row=11, column=0, padx=5, pady=1)
		entry11 = tk.Entry(width=45)
		entry11.grid(row=11, column=1, padx=5, pady=1)

		label12 = tk.Label(width=25, anchor='w', relief='ridge', text="ADDITIONALASSETURL")
		label12.grid(row=12, column=0, padx=5, pady=1)
		entry12 = tk.Entry(width=45)
		entry12.grid(row=12, column=1, padx=5, pady=1)

		label13 = tk.Label(width=25, anchor='w', relief='ridge', text="ADDITIONALASSETTYPE")
		label13.grid(row=13, column=0, padx=5, pady=1)
		entry13 = tk.Entry(width=45)
		entry13.grid(row=13, column=1, padx=5, pady=1)

		label14 = tk.Label(width=25, anchor='w', relief='ridge', text="ADDITIONALASSETALTTEST")
		label14.grid(row=14, column=0, padx=5, pady=1)
		entry14 = tk.Entry(width=45)
		entry14.grid(row=14, column=1, padx=5, pady=1)

		label15 = tk.Label(width=25, anchor='w', relief='ridge', text="ADDITIONALURLASSETTHREE")
		label15.grid(row=15, column=0, padx=5, pady=1)
		entry15 = tk.Entry(width=45)
		entry15.grid(row=15, column=1, padx=5, pady=1)

		label16 = tk.Label(width=25, anchor='w', relief='ridge', text="UPCNUMBER")
		label16.grid(row=16, column=0, padx=5, pady=1)
		entry16 = tk.Entry(width=45)
		entry16.grid(row=16, column=1, padx=5, pady=1)

		label17 = tk.Label(width=25, anchor='w', relief='ridge', text="MSRPMEASURE")
		label17.grid(row=17, column=0, padx=5, pady=1)
		entry17 = tk.Entry(width=45)
		entry17.grid(row=17, column=1, padx=5, pady=1)

		label18 = tk.Label(width=25, anchor='w', relief='ridge', text="LENGTH")
		label18.grid(row=18, column=0, padx=5, pady=1)
		entry18 = tk.Entry(width=45)
		entry18.grid(row=18, column=1, padx=5, pady=1)

		label19 = tk.Label(width=25, anchor='w', relief='ridge', text="WIDTH")
		label19.grid(row=19, column=0, padx=5, pady=1)
		entry19 = tk.Entry(width=45)
		entry19.grid(row=19, column=1, padx=5, pady=1)

		label20 = tk.Label(width=25, anchor='w', relief='ridge', text="HEIGHT")
		label20.grid(row=20, column=0, padx=5, pady=1)
		entry20 = tk.Entry(width=45)
		entry20.grid(row=20, column=1, padx=5, pady=1)

		label21 = tk.Label(width=25, anchor='w', relief='ridge', text="WEIGHT")
		label21.grid(row=21, column=0, padx=5, pady=1)
		entry21 = tk.Entry(width=45)
		entry21.grid(row=21, column=1, padx=5, pady=1)

		label22 = tk.Label(width=25, anchor='w', relief='ridge', text="WARRANTYTEXT")
		label22.grid(row=22, column=0, padx=5, pady=1)
		entry22 = tk.Entry(width=45)
		entry22.grid(row=22, column=1, padx=5, pady=1)

		label23 = tk.Label(width=25, anchor='w', relief='ridge', text="WARRANTYLENGTH")
		label23.grid(row=23, column=0, padx=5, pady=1)
		entry23 = tk.Entry(width=45)
		entry23.grid(row=23, column=1, padx=5, pady=1)

		label24 = tk.Label(width=25, anchor='w', relief='ridge', text="CUSTOMSKU")
		label24.grid(row=24, column=0, padx=5, pady=1)
		entry24 = tk.Entry(width=45)
		entry24.grid(row=24, column=1, padx=5, pady=1)

		label25 = tk.Label(width=25, anchor='w', relief='ridge', text="SELLFORAMOUNT")
		label25.grid(row=25, column=0, padx=5, pady=1)
		entry25 = tk.Entry(width=45)
		entry25.grid(row=25, column=1, padx=5, pady=1)

		label26 = tk.Label(width=25, anchor='w', relief='ridge', text="MINSELLFOR")
		label26.grid(row=26, column=0, padx=5, pady=1)
		entry26 = tk.Entry(width=45)
		entry26.grid(row=26, column=1, padx=5, pady=1)

		label27 = tk.Label(width=25, anchor='w', relief='ridge', text="SHIPWEIGHTVALUE")
		label27.grid(row=27, column=0, padx=5, pady=1)
		entry27 = tk.Entry(width=45)
		entry27.grid(row=27, column=1, padx=5, pady=1)

		label28 = tk.Label(width=25, anchor='w', relief='ridge', text="CATEGORYSPECIFICATTRIBUTES")
		label28.grid(row=28, column=0, padx=5, pady=1)
		entry28 = tk.Entry(width=45)
		entry28.grid(row=28, column=1, padx=5, pady=1)

		label29 = tk.Label(width=25, anchor='w', relief='ridge', text="BRANDNAME")
		label29.grid(row=29, column=0, padx=5, pady=1)
		entry29 = tk.Entry(width=45)
		entry29.grid(row=29, column=1, padx=5, pady=1)

if __name__ == "__main__": # compile the main class/widgets to be displayed on screen.
	root = mainApp()
	root.resizable(0,0)
	center(root)
	root.title('Wally Lister')
	root.mainloop()
