#__author__ = "ISHAN PATEL"
#__version__ = "3.5.2"
#__email__ = "ishanpatel415@gmail.com"
# Program for Room_number ( file character assignment using user input)


file1=open('test_read.txt','r') 												#opening the file_1

file2=open('test_new.txt','w')													#opening the file_2

no=int(input("Enter the position/index of character to remove  : "))			#taking user input

for delineation in file1:														#iteration)_1
	file2.write(delineation[:no])
	file2.write(delineation[no+1:])
	
file1.close()																	#closing file1
file2.close()																	#closing file2

#end

