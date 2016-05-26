import textwrap
def textToBook(file_name, out_file_name, line_width):
	out_file = open(out_file_name,'w')

	# consider it's a large text, we read line by line
	with open(file_name,'r') as in_file:
		for line in in_file:
			# remove the tab/space at both the leading and trailing position
			line = line.strip()

			# Escape any empty line
			if len(line):
				# in case there are '\n' new line symbol in the line 			
				line_list = line.split("\\n")
				line_list = [string.strip() for string in line_list if len(string.strip()) > 0]
				# print "line_list", line_list
				for new_line in line_list:
					# in case the space/tab between two words is larger than the line_width, the second word starts in the new line.
					# print new_line[:line_width].rsplit(' ', 1)[0]
					# print new_line[line_width+1:2*line_width].rsplit(' ', 1)[0]
					print new_line
					new_line_list = textwrap.wrap(new_line, line_width, break_long_words=False)		
					for item in new_line_list:
						print item 
						out_file.write("%s\n" % item)

	out_file.close()
			
if __name__ == '__main__':
	# we assume once we know the page size (A3, A4) and the font of words, we can calculate the number of alphabets  (line_width) each line can hold  
	line_width = 7
	in_file_name = "text.txt"
	out_file_name = "book.txt"
	textToBook(in_file_name, out_file_name, line_width)