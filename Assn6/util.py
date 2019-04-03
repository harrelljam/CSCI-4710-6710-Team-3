# if a file extension is not listed, the system will not upload the file
ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
	if '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
		return True
	print ("wrong file type")
	return False
    #return '.' in filename and \
     #      filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS