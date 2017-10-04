import string

def open_file(file):
	book = open(file)
	line_list = []
	for line in book:
		line_list.append(line)

	for line in line_list:
		process_line(line, line_list)
	return line_list

def process_line(line, lista):
    """Adds the words in the line to the histogram.

    Modifies hist.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    

    line = line.replace('-', ' ')
    
    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        # update the histogram
        lista.append(word)


print open_file('hamlet.txt')



