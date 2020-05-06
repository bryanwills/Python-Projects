import csv

with open('names.csv','r') as csv_file:
	#csv_reader = csv.reader(csv_file)
	csv_reader = csv.DictReader(csv_file)


	#steps over header line
	#next(csv_reader)
	with open('new_names.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name', 'email']
		
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
		#csv_writer = csv.writer(new_file, delimiter='\t')
		csv_writer.writeheader()

		for line in csv_reader:
		#returns only emails
			#print(line[2])
			del line['email']
			csv_writer.writerow(line)

#use same data and write to file with dashes instead of commas