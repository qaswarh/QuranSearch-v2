# QuranSearch-v2
Quran search powered by pandas and tkinter 

Similar to the earlier version, the script looks for Quran words and their meanings having the same root from QuranTM.xlsm file, downloaded from quransteps.wordpress.com 

At first the script looks for all the roots in Quran from the said file, 1670 found, and create a dictionary for the user. 
The dictionary is created so that user can enter numeric value (married with root) instead of typing the root in Arabic.

The script also does extract and display the rows (in Arabic) from the said file where the words found

What's new in this version?
1. GUI window to 'choose your file'; user selects the file from the directory where the file has been saved.
2. pandas reads the file to built the data frames and the script is around around pandas, replacing the pyexcel.
3. This gives better speed, specially for large dbs 

Here is how it will look when you run


![image](https://user-images.githubusercontent.com/47313728/75135417-51761e00-5696-11ea-9f3c-ebfd8119ba91.png)

![image](https://user-images.githubusercontent.com/47313728/75140449-cdc32e00-56a3-11ea-8ca0-428cefdb6f44.png)

![image](https://user-images.githubusercontent.com/47313728/75140715-504bed80-56a4-11ea-8fe7-54d837fbf61b.png)
