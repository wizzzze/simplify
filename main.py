from OpenGL.GL import *  
from OpenGL.GLU import *  
from OpenGL.GLUT import *  
from sys import argv
from Loader import Loader
from ObjLoader import ObjLoader

script,filePath = argv

loader = Loader();
files = loader.load(filePath);

# for file in files:
# 	print file

objLoader = ObjLoader("./models/123.obj");
fileContent = objLoader.load();
print fileContent
