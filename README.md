# walmartFileListingGenerator
Generate rows, which corespond to individual listing properties, to copy/paste in walmart spreadsheet for bulk listing.
Similar to eBay's 'File Exchange.'

##Overall
WalMart marketplace's listing process is lack luster. Also, their API is mostly still in beta.
Current process is to manually update a (really bad) ~200 cell `xlsx` spreadsheet per listing. Granted you don't <b>need</b> to use all cells but each cell does correspond to something in the listing.<br>
Of which you have to discern what to keep and what goes where. After filtering out this selection, there's still the process of manually adding or copy/pasting the specifications per product and then going back and changing listing name, UPC's, etc...

Anyways, this script aims to automate at least the input of these mentioned variables. A major hitch is that walmart only accepts/requires `.xlsx` formatted spreadsheet uploads.
Furthermore, there are hidden rows, excessive sheets (unused categories, cell description, etc...) that if removed or altered will result in an upload error.
Given the fact that reading `xlsx` spreadsheets and then editing them on the fly is overly complicated and more than what I need. I simply log the array and then copy a stripped version of the array into the clip board which can then be pasted with 'special format' to a (crappy walmart) spreadsheet. 

##Library Requirements
`pip install pyperclip`

##TODO
*Extensible to more than just the home decor listing category. At the moment this category is all that applies to me personally.
*Add tkinter GUI
*
