import os

#folder to path you want to change the name of. Drag folder into terminal from Finder
os.chdir('/Users/bryanwi09/Downloads/ebooks/')

for f in os.listdir():
	f_name, f_ext = os.path.splitext(f)

	f_title, f_course = f_name.split('-')

	print('{}-{}'.format(f_course, f_title, f_ext))
