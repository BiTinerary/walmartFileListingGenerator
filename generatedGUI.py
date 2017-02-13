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
			inputArray = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get(), entry9.get(), entry10.get(), entry11.get(), entry12.get(), entry13.get(), entry14.get(), entry15.get(), entry16.get(), entry17.get(), entry18.get(), entry19.get()]
			with open('walmartArrayForCategory.txt', 'r+') as getList:
				
				stringFromCatFile = getList.read()
				convertToArray = stringFromCatFile.split(",")

			finalArray = []
			x = 0

			for each in convertToArray:
				if each == 'UPC' or each == 'USD' or each == 'INCHES' or each == 'POUNDS' or each == '2038346' or each =='LB':
						finalArray.append(each)
						continue
				elif each == '':
						finalArray.append(each)
						continue
				else:
					try:
						finalArray.append(inputArray[x])
					except:
						pass
				x += 1
			
			with open('finalFile.txt', 'a+') as final2:
				final2.write(str(finalArray)+'\r\n')

			thisToClipAndXLSX = ','.join(finalArray)
			pyperclip.copy('\n'+thisToClipAndXLSX+'\n')
			print 'copied to clipboard'
			print thisToClipAndXLSX.encode('utf-8')

		self.bind('<Return>', (lambda event: getInput()))

		getAllInputs0 = tk.Button(text='Gather Inputs', width=65, command=lambda: getInput())
		getAllInputs0.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

		label1 = tk.Label(width=25, anchor='w', relief='ridge', text="Listing Title")
		label1.grid(row=1, column=0, padx=5, pady=1)
		entry1 = tk.Entry(width=45)
		entry1.grid(row=1, column=1, padx=5, pady=1)

		label2 = tk.Label(width=25, anchor='w', relief='ridge', text="Long Description")
		label2.grid(row=2, column=0, padx=5, pady=1)
		entry2 = tk.Entry(width=45)
		entry2.grid(row=2, column=1, padx=5, pady=1)

		label3 = tk.Label(width=25, anchor='w', relief='ridge', text="Shelf Description")
		label3.grid(row=3, column=0, padx=5, pady=1)
		entry3 = tk.Entry(width=45)
		entry3.grid(row=3, column=1, padx=5, pady=1)

		label4 = tk.Label(width=25, anchor='w', relief='ridge', text="Short Description")
		label4.grid(row=4, column=0, padx=5, pady=1)
		entry4 = tk.Entry(width=45)
		entry4.grid(row=4, column=1, padx=5, pady=1)

		label5 = tk.Label(width=25, anchor='w', relief='ridge', text="Image URL")
		label5.grid(row=5, column=0, padx=5, pady=1)
		entry5 = tk.Entry(width=45)
		entry5.grid(row=5, column=1, padx=5, pady=1)

		label6 = tk.Label(width=25, anchor='w', relief='ridge', text="Main Image Alternate Text")
		label6.grid(row=6, column=0, padx=5, pady=1)
		entry6 = tk.Entry(width=45)
		entry6.grid(row=6, column=1, padx=5, pady=1)

		label7 = tk.Label(width=25, anchor='w', relief='ridge', text="UPC Number")
		label7.grid(row=7, column=0, padx=5, pady=1)
		entry7 = tk.Entry(width=45)
		entry7.grid(row=7, column=1, padx=5, pady=1)

		label8 = tk.Label(width=25, anchor='w', relief='ridge', text="MSRP")
		label8.grid(row=8, column=0, padx=5, pady=1)
		entry8 = tk.Entry(width=45)
		entry8.grid(row=8, column=1, padx=5, pady=1)

		label9 = tk.Label(width=25, anchor='w', relief='ridge', text="Length")
		label9.grid(row=9, column=0, padx=5, pady=1)
		entry9 = tk.Entry(width=45)
		entry9.grid(row=9, column=1, padx=5, pady=1)

		label10 = tk.Label(width=25, anchor='w', relief='ridge', text="Width")
		label10.grid(row=10, column=0, padx=5, pady=1)
		entry10 = tk.Entry(width=45)
		entry10.grid(row=10, column=1, padx=5, pady=1)

		label11 = tk.Label(width=25, anchor='w', relief='ridge', text="Height")
		label11.grid(row=11, column=0, padx=5, pady=1)
		entry11 = tk.Entry(width=45)
		entry11.grid(row=11, column=1, padx=5, pady=1)

		label12 = tk.Label(width=25, anchor='w', relief='ridge', text="Weight")
		label12.grid(row=12, column=0, padx=5, pady=1)
		entry12 = tk.Entry(width=45)
		entry12.grid(row=12, column=1, padx=5, pady=1)

		label13 = tk.Label(width=25, anchor='w', relief='ridge', text="Warranty Text")
		label13.grid(row=13, column=0, padx=5, pady=1)
		entry13 = tk.Entry(width=45)
		entry13.grid(row=13, column=1, padx=5, pady=1)

		label14 = tk.Label(width=25, anchor='w', relief='ridge', text="Waranty Length")
		label14.grid(row=14, column=0, padx=5, pady=1)
		entry14 = tk.Entry(width=45)
		entry14.grid(row=14, column=1, padx=5, pady=1)

		label15 = tk.Label(width=25, anchor='w', relief='ridge', text="Custom SKU")
		label15.grid(row=15, column=0, padx=5, pady=1)
		entry15 = tk.Entry(width=45)
		entry15.grid(row=15, column=1, padx=5, pady=1)

		label16 = tk.Label(width=25, anchor='w', relief='ridge', text="Sell For Amount")
		label16.grid(row=16, column=0, padx=5, pady=1)
		entry16 = tk.Entry(width=45)
		entry16.grid(row=16, column=1, padx=5, pady=1)

		label17 = tk.Label(width=25, anchor='w', relief='ridge', text="Min Advertised Price")
		label17.grid(row=17, column=0, padx=5, pady=1)
		entry17 = tk.Entry(width=45)
		entry17.grid(row=17, column=1, padx=5, pady=1)

		label18 = tk.Label(width=25, anchor='w', relief='ridge', text="Shipping Weight (lbs)")
		label18.grid(row=18, column=0, padx=5, pady=1)
		entry18 = tk.Entry(width=45)
		entry18.grid(row=18, column=1, padx=5, pady=1)

		label19 = tk.Label(width=25, anchor='w', relief='ridge', text="Brand Name")
		label19.grid(row=19, column=0, padx=5, pady=1)
		entry19 = tk.Entry(width=45)
		entry19.grid(row=19, column=1, padx=5, pady=1)

if __name__ == "__main__": # compile the main class/widgets to be displayed on screen.
	root = mainApp()
	root.resizable(0,0)
	center(root)
	root.title('Wally Lister')
	root.mainloop()
