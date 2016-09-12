#!/usr/bin/env python3
import os
import glob
import argparse
parser = argparse.ArgumentParser()
parser.description="Script to generate termux colorschemes preview. This will generate a markdown file to be used with Jekyll."
parser.epilog="Example: ./termux-color-preview.py ~/dev/termux-styling > ~/dev/termux.github.io/add-on-styling-color-preview.md"
parser.add_argument('folder', nargs='?',  default='../termux-styling', help='Termux Styling folder. Defaults to ../termux-styling')
options = parser.parse_args()

codeexample="""
require "gem"

string = "base16"
symbol = :base16
fixnum = 0
float  = 0.00
array  = Array.new
array  = ['chris', 85]
hash   = {"test" => "test"}
regexp = /[abc]/

# This is a comment
class Person
  
  attr_accessor :name
  
  def initialize(attributes = {})
    @name = attributes[:name]
  end
  
  def self.greet
    "hello"
  end
end

person1 = Person.new(:name => "Chris")
print Person::greet, " ", person1.name, "\\n"
puts "another #{Person::greet} #{person1.name}"
"""
def colorblock(colors, colorname):
	try:
		color=colors[colorname]
	except KeyError:
		color='none'
	return '<div class="preview-color" style="background-color:'+color+'"></div>';

def returncolor(colors, colorname):
	try:
		color=colors[colorname]
	except KeyError:
		color='none'
	return color;
output=""
header=""
nav=""
header+="---\n"
header+="layout: page\n"
header+="title: Preview of color schemes\n"
header+="---\n"
path = options.folder+'/app/src/main/assets/colors/'
for infile in glob.glob( os.path.join(path, '*.properties') ):
	colorname=os.path.basename(infile).split(".")[0]
	title=colorname.replace("-"," ").title()
	output+='<h3 id="'+colorname+'">'+title+'</h3>'
	nav+='* ['+title+'](#'+colorname+')\n'
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
		output+='<div class="preview-color-block">'
		output+='<div class="preview-color-row">'
		output+=colorblock(colors, 'foreground')
		for i in range(0,7):
			output+=colorblock(colors,'color'+str(i))
		output+='</div>'
		output+='<div class="preview-color-row">'
		output+=colorblock(colors, 'background')
		for i in range(8,15):
			output+=colorblock(colors, 'color'+str(i))
		output+='</div>'
		output+='</div>'
		output+='<style>'
		output+=".codeexample-"+colorname+" .highlight code, .codeexample-"+colorname+" .highlight pre{color:"+returncolor(colors, 'foreground')+";background-color:"+returncolor(colors, 'background')+"}"
		output+=".codeexample-"+colorname+" .highlight .hll{background-color:"+returncolor(colors, 'color8')+"}"
		output+=".codeexample-"+colorname+" .highlight .c{color:"+returncolor(colors, 'color7')+"}"
		output+=".codeexample-"+colorname+" .highlight .err{color:"+returncolor(colors, 'color10')+";background-color:"+returncolor(colors, 'color8')+"}"
		output+=".codeexample-"+colorname+" .highlight .g{color:"+returncolor(colors, 'color7')+"}"
		output+=".codeexample-"+colorname+" .highlight .k{color:"+returncolor(colors, 'color4')+"}"
		output+=".codeexample-"+colorname+" .highlight .l{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .n{color:"+returncolor(colors, 'foreground')+"}"
		output+=".codeexample-"+colorname+" .highlight .o{color:"+returncolor(colors, 'color11')+"}"
		output+=".codeexample-"+colorname+" .highlight .x{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .p{color:"+returncolor(colors, 'color15')+"}"
		output+=".codeexample-"+colorname+" .highlight .cm{color:"+returncolor(colors, 'color7')+"}"
		output+=".codeexample-"+colorname+" .highlight .cp{color:"+returncolor(colors, 'color7')+"}"
		output+=".codeexample-"+colorname+" .highlight .c1{color:"+returncolor(colors, 'color7')+"}"
		output+=".codeexample-"+colorname+" .highlight .cs{color:"+returncolor(colors, 'color2')+";font-weight:bold}"
		output+=".codeexample-"+colorname+" .highlight .gd{color:"+returncolor(colors, 'color2')+"}"
		output+=".codeexample-"+colorname+" .highlight .ge{color:"+returncolor(colors, 'color5')+";font-style:italic}"
		output+=".codeexample-"+colorname+" .highlight .gr{color:"+returncolor(colors, 'color2')+"}"
		output+=".codeexample-"+colorname+" .highlight .gh{color:"+returncolor(colors, 'foreground')+";font-weight:bold}"
		output+=".codeexample-"+colorname+" .highlight .gi{color:"+returncolor(colors, 'color11')+"}"
		output+=".codeexample-"+colorname+" .highlight .go{color:"+returncolor(colors, 'color8')+"}"
		output+=".codeexample-"+colorname+" .highlight .gp{color:"+returncolor(colors, 'foreground')+";font-weight:bold}"
		output+=".codeexample-"+colorname+" .highlight .gs{color:"+returncolor(colors, 'color5')+";font-weight:bold}"
		output+=".codeexample-"+colorname+" .highlight .gu{color:"+returncolor(colors, 'color5')+";font-weight:bold}"
		output+=".codeexample-"+colorname+" .highlight .gt{color:"+returncolor(colors, 'color12')+"}"
		output+=".codeexample-"+colorname+" .highlight .kc{color:"+returncolor(colors, 'color9')+"}"
		output+=".codeexample-"+colorname+" .highlight .kd{color:"+returncolor(colors, 'color11')+"}"
		output+=".codeexample-"+colorname+" .highlight .kn{color:"+returncolor(colors, 'color4')+";font-weight:bold}"
		output+=".codeexample-"+colorname+" .highlight .kp{color:"+returncolor(colors, 'color2')+"}"
		output+=".codeexample-"+colorname+" .highlight .kr{color:"+returncolor(colors, 'color10')+"}"
		output+=".codeexample-"+colorname+" .highlight .kt{color:"+returncolor(colors, 'color7')+"}"
		output+=".codeexample-"+colorname+" .highlight .ld{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .m{color:"+returncolor(colors, 'color13')+"}"
		output+=".codeexample-"+colorname+" .highlight .s{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .na{color:"+returncolor(colors, 'color2')+"}"
		output+=".codeexample-"+colorname+" .highlight .nb{color:"+returncolor(colors, 'color12')+"}"
		output+=".codeexample-"+colorname+" .highlight .nc{color:"+returncolor(colors, 'color12')+"}"
		output+=".codeexample-"+colorname+" .highlight .no{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .nd{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .ni{color:"+returncolor(colors, 'color9')+"}"
		output+=".codeexample-"+colorname+" .highlight .ne{color:"+returncolor(colors, 'color3')+";font-weight:bold}"
		output+=".codeexample-"+colorname+" .highlight .nf{color:"+returncolor(colors, 'color12')+"}"
		output+=".codeexample-"+colorname+" .highlight .nl{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .nn{color:"+returncolor(colors, 'color12')+"}"
		output+=".codeexample-"+colorname+" .highlight .nx{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .py{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .nt{color:"+returncolor(colors, 'color2')+"}"
		output+=".codeexample-"+colorname+" .highlight .nv{color:"+returncolor(colors, 'foreground')+"}"
		output+=".codeexample-"+colorname+" .highlight .ow{color:"+returncolor(colors, 'color11')+"}"
		output+=".codeexample-"+colorname+" .highlight .w{color:"+returncolor(colors, 'color5')+"}"
		output+=".codeexample-"+colorname+" .highlight .mf{color:"+returncolor(colors, 'color13')+"}"
		output+=".codeexample-"+colorname+" .highlight .mh{color:"+returncolor(colors, 'color13')+"}"
		output+=".codeexample-"+colorname+" .highlight .mi{color:"+returncolor(colors, 'color13')+"}"
		output+=".codeexample-"+colorname+" .highlight .mo{color:"+returncolor(colors, 'color13')+"}"
		output+=".codeexample-"+colorname+" .highlight .sb{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .sc{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .sd{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .s2{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .se{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .sh{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .si{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .sx{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .sr{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .s1{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .ss{color:"+returncolor(colors, 'color14')+"}"
		output+=".codeexample-"+colorname+" .highlight .bp{color:"+returncolor(colors, 'color12')+"}"
		output+=".codeexample-"+colorname+" .highlight .vc{color:"+returncolor(colors, 'color12')+"}"
		output+=".codeexample-"+colorname+" .highlight .vg{color:"+returncolor(colors, 'foreground')+"}"
		output+=".codeexample-"+colorname+" .highlight .vi{color:"+returncolor(colors, 'color11')+"}"
		output+=".codeexample-"+colorname+" .highlight .il{color:"+returncolor(colors, 'color13')+"}"
		output+='</style>'
		output+='<div class="codeexample codeexample-'+colorname+'">'
		output+='{% highlight ruby%}'
		output+=codeexample
		output+='{% endhighlight %}'
		output+="</div>"
print(header)
print(nav)
print(output)
