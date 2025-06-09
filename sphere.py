from sympy import polyhedron
import trimesh
import math

class equation(x,y,z,n):
   def  x(n):
        x1 = a * n^5 + b * n^4 + c * n^3 + d * n^2 + e * n + f
        x2 = a * n^4 + b * n^3 + c * n^2 + d * n + e * n^(-1) + f
   def  y(n):
        y1 = a * n^3 + b * n^2 + c * n + d * n^(-1) + e * n^(-2) + f
        y2 = a * n^2 + b * n + c * n^(-1) + d * n^(-2) + e * n^(-3) + f
   def  z(n):      
        z1 = a * n + b * n^(-1) + c * n^(-2) + d * n^(-3) + e * n^(-4) + f
        z2 = a * n^(-1) + b * n^(-2) + c * n^(-3) + d * n^(-2) + e * n^(-5) + f

class spacetime():
    def Hexadecimal(a,b,c,d,e,f):
         a = "00001011"
         b = "00001100"
         c = "00001101"
         d = "00001110"
         e = "00001111"
         f = "00010000"
    def space(X,Y,Z,Radius,theta,fai):
         this.X = Radius * math.cos(theta)
         this.Y = Radius * math.sin(fai)
         this.Z = Radius * math.cos(theta) * math.cos(fai)
    def time(x,y,z,n):
        return [
            a * math.sin(x + n) + b * math.cos(x - n) + c * math.sin(y + n) + d * math.cos(y - n) + e * math.sin(z + n) + f * math.cos(z - n),       
            a * math.asin(x + n) + b * math.acos(x - n) + c * math.asin(y + n) + d * math.acos(y - n) + e * math.asin(z + n) + f * math.acos(z - n),
            a * math.sinh(x + n) + b * math.cosh(x - n) + c * math.sinh(y + n) + d * math.cosh(y - n) + e * math.sinh(z + n) + f * math.cosh(z - n),
            a * math.tan(x + n) + b * math.atan(x - n) + c * math.tan(y + n) + d * math.atan(y - n) + e * math.tan(z + n) + f * math.atan(z - n)
        ]

class wiki():
    def polyhedron(Vertex,Edges,Faces):
        self.Vertex = [V]
        self.Edges = [E]
        self.Faces = [F]
        return V - E + F == 2

    def abcdef(Tetrahedron,Hexhedron,Octahedron,Dodecahedron,Icosahedron):
        this.dot = 0
        this.line = 1
        self.a = dotline
        self.b = Tetrahedron
        self.c = Hexhedron
        self.d = Octahedron
        self.e = Dodecahedron
        self.f = Icosahedron       
