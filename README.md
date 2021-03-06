# walmartFileListingGenerator
Generate rows, which correspond to individual listing properties, to copy/paste into walmart spreadsheet for bulk listing.<br>
The `guiGenerator.py` script uses metaprogramming to generate `generatedGUI.py` with variables based on category requirements. This GUI then produces a string to be 'special pasted' into a spreadsheet which can be uploaded in a similar fashion to eBay's 'File Exchange.'

##Overall
`tkinterGUIGenerator.py` uses a manually created template (from different Walmart Category spreadsheet) to generate a GUI.py script
with labels and entry options for each cell with content. ie: not empty, static variables like USD, Mesaurements, etc... Yes it's ugly. Yes it's metaprogramming. Yes, it gets the job done.<br>
<br>
Which looks like this: `generatedGUI.py`<br>
<img src='https://s13.postimg.org/j51qpujaf/github_Wally_Image.png'><br>
<br>
When you press <kbd>Enter</kbd> or the top button, it copies the following into your keyboard and writes to log file:<br>
<br>
`,,Long desc no special characters Only HTML <br>Then some stuff,,,,,,,,,,,,,,UPC,,,,,,USD,,,,,,,,,INCHES,,INCHES,,INCHES,,POUNDS,,2038346,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,USD,,USD,,,,LB,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
`<br>
<br>
You would then paste this into a spreadsheet (with 'special paste' option where applicable) and in turn have one more listing.

##More info, reasoning, limitations
WalMart marketplace's listing process is lack luster. Also, their API is mostly still in beta. Current process is to manually update a (really bad) ~200 cell `xlsx` spreadsheet per listing.<br>Granted you don't <b>need</b> to use all cells but each cell does correspond to something in the listing.<br>
<br>
Of which you have to discern what to keep and what goes where. After filtering out this selection, there's still the process of manually adding or copy/pasting the specifications per product and then going back and changing listing name, UPC's, etc...

Anyways, this script aims to automate at least the input of these mentioned variables. A major hitch is that walmart only accepts/requires `.xlsx` formatted spreadsheet uploads.<br>
Furthermore, there are hidden rows, excessive sheets (unused categories, cell description, etc...) that if removed or altered will result in an upload error.<br>
<br>
Given the fact that reading `xlsx` spreadsheets and then editing them on the fly is overly complicated and more than what I need. I simply log the array and then copy a stripped version of the array into the clip board which can then be pasted with 'special format' to a (crappy walmart) spreadsheet. 

##Library Requirements<br>
`pip install pyperclip`<br>
`pip install python-tk`<br>

##TODO
*<strike>Extensible to more than just the home decor listing category. At the moment this category is all that applies to me personally.</strike><br>
*<strike>Add tkinter GUI</strike><br>
*<strike>Make final/output string a log file. <b>It is overwritten</b> every time a new listing is filled out, or when <kbd>Enter</kbd> is pressed.</strike>
* <strike>Sanitize input</strike>, comma's are currently an issue. Obviously messes up list format. <strike>(urls? not an issue as of yet.)</strike>
	* Input sanitized [using regex] to allow, but <b>remove</b> special characters from text <b>box</b>, with exception of `html` characters. Other regular input's still needs sanitization.
	* URL's are properly encoded so that copying to clipboard isn't an issue.
* Sanitize number inputs, UPC, MSRP, $$, etc...
* Add 'upload file' option.
    * Instead of manual input per listing, accept input file (2d array) of copy/pasted log file that are marginally different (ie: sizes color) but allow for easy editing of certain cells (html, `<li></li>`, Description) and copy/pasting those to another array.
* Include/preserve WPID option for accelerated ingestion.
   * If WPID is included (gathered from previously established listing) then item has existed and has already been approved. So listing doesn't go through same sifting process. Think of WPID as Walmart's equivalent to Amazon's ASIN.
