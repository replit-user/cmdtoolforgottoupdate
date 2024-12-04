import argparse
parser=argparse.ArgumentParser()
parser.add_argument("filename",help="the filename to create/open")
parser.add_argument("-a","--append",help="opens the file in append mode rather than w mode",action='store_true')
parser.add_argument("text",help="the text to write to the file")
parser.add_argument("-f","--format",action="store_true",help="to decide whether or not to replace .n with a newline or .t with a tab")
args=parser.parse_args()
text:str=args.text
filename:str=args.filename
if args.format:
    text=text.replace(".n","\n")
    text=text.replace(".t","\t")
if args.append:
    with open(filename,"a") as file:
        file.write(text)
else:
    with open(filename,"w") as file:
        file.write(text)