#__author__ = "ISHAN PATEL"
#__version__ = "3.5.2"
#__email__ = "ishanpatel415@gmail.com"
# Program for Room_number ( linux user print assignment)

file_op=open("/etc/passwd","r") 			#opening the file
for i in file_op.readlines():				#iteration_1
	if "usr" in i:							#conditional_statement_1
		print(i.split(":")[0])				#print_result
		
#end