from OpenGL.GL import *  
from OpenGL.GLU import *  
from OpenGL.GLUT import *  
from sys import argv

script,filePath = argv
if(os.path.exists(filePath)):
	if(os.path.isdir(filePath)):

	elif(os.path.isfile(filePath)):
		