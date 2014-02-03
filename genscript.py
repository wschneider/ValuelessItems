"""
CAUTION: ***PLEASE READ readme.txt BEFORE USING THIS SCRIPT***
Name   : Genscript.py
Author : Will Schneider
Email  : willschneider.513+VI@gmail.com
Purpose:
    This is the phase (1) script for this application. It takes
    all of the items in 'itemsheet.csv', and generates a .js
    file that will be used in the Chrome extension. 
"""

i = open("itemsheet.csv", "r")
o = open("highlight.js", "w")

head = """
var bigForm = document.getElementsByName("quickstock")[0];

//get all table elements
var rows = bigForm.getElementsByTagName("TR");

for(var i = 1;i<rows.length - 2;i++)
{
  // SKIP THE FIRST ROW AND THE LAST 2 ROWS
  //iterate over rows. Check the first TD element in the row 
  if(i%21 != 0){
    var cl = "vl_" + rows[i].firstChild.textContent;
    rows[i].setAttribute("class",cl);
  }
}

var litems = new Array();

"""

foot = """

for(var i = 0;i < litems.length; i++)
{
  var arr = document.getElementsByClassName("vl_" + litems[i]);

  for(var j = 0;j<arr.length;j++)
  {
    arr[j].setAttribute("bgcolor","green");
  }
}
"""

o.write(head)
#print(head)

for line in i:
    line = line.replace('\n', '')
    o.write("litems[litems.length] = \"" + line + "\";\n")
#   print("litems[litems.length] = " + line)

o.write(foot)
#print(foot)

i.close()
o.close()
