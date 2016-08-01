#!/usr/bin/env python3
import os
import glob
import argparse
parser = argparse.ArgumentParser()
parser.description="Script to generate termux colorschemes preview. This will generate a markdown file to be used with Jekyll."
parser.epilog="Example: ./termux-color-preview.py ~/dev/termux-styling > ~/dev/termux.github.io/add-on-styling-color-preview.md"
parser.add_argument('folder', nargs='?',  default='../termux-styling', help='Termux Styling folder. Defaults to ../termux-styling')
options = parser.parse_args()

def printcolor(colors, colorname):
	try:
		color=colors[colorname]
	except KeyError:
		color='none'
	print('<div class="preview-color" style="background-color:'+color+'"></div>')
	return;

print("---")
print("layout: page")
print("title: Preview of color schemes")
print("---")
path = options.folder+'/app/src/main/assets/colors/'
for infile in glob.glob( os.path.join(path, '*.properties') ):
	colorname=os.path.basename(infile).split(".")[0]
	title=colorname.replace("-"," ").title()
	print('<h3 id="'+colorname+'">'+title+'</h3>')
	with open (infile, "r") as curfile:
		colorfile=curfile.read()
		colors={}
		lines=colorfile.split('\n')
		for line in lines:
			line=line.rstrip().lstrip()
			if line[:1]!="#":
				if ":" in line: 
					splitline=line.split(':')
				if "=" in line: 
					splitline=line.split('=')
				if splitline!=['']:
					colors[splitline[0].rstrip()]=splitline[1].lstrip()
		print('<div class="preview-color-block">')
		print('<div class="preview-color-row">')
		printcolor(colors, 'foreground')
		for i in range(0,7):
			printcolor(colors,'color'+str(i))
		print('</div>')
		print('<div class="preview-color-row">')
		printcolor(colors, 'background')
		for i in range(8,15):
			printcolor(colors, 'color'+str(i))
		print('</div>')
		print('</div>')
