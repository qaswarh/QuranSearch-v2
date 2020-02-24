# QuranSearch-v2
Quran search powered by pandas and tkinter 

Similar to earlier version, the script displays display meanings and lines from QuranTM.xlsm file downloaded from 
quransteps.wordpress.com, the script look for Quran words and their meanings having the same root.

The script looks for all the roots in Quran from the said file, 1670 found, and create a dictionary for the user. 
The dictionary is created so that user can enter numeric value (married with root) instead of typing root in Arabic.

The script also extract and display the rows (in Arabic) from the said file where the words found

What's new in this version?
1. 'choose your file' GUI window for user to select the file from the directory user has stored the file.
2. pandas reads the file to built the data frames to write the script around rather than using pyexcel science.
3. Better speed, specially for large db 

Here is how it will look when you run


![image](https://user-images.githubusercontent.com/47313728/75135417-51761e00-5696-11ea-9f3c-ebfd8119ba91.png)


![image](https://user-images.githubusercontent.com/47313728/75140449-cdc32e00-56a3-11ea-8ca0-428cefdb6f44.png)
