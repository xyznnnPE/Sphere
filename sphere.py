from sympy import polyhedron
import trimesh
import math

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
    def time(x,y,z,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12):
        return [
            a * math.sin(x + t1) + b * math.cos(x - t1) + c * math.sin(y + t2) + d * math.cos(y - t2) + e * math.sin(z + t3) + f * math.cos(z - t3),       #t123
            a * math.asin(x + t4) + b * math.acos(x - t4) + c * math.asin(y + t5) + d * math.acos(y - t5) + e * math.asin(z + t6) + f * math.acos(z - t6), #t456
            a * math.sinh(x + t7) + b * math.cosh(x - t7) + c * math.sinh(y + t8) + d * math.cosh(y - t8) + e * math.sinh(z + t9) + f * math.cosh(z - t9), #t789
            a * math.tan(x + t10) + b * math.atan(x - t10) + c * math.tan(y + t11) + d * math.atan(y - t11) + e * math.tan(z + t12) + f * math.atan(z - t12) #t101112
        ]

class wiki():
    def __init__polyhedron(Vertex,Edges,faces):
        self.Vertex = [V]
        self.Edges = [E]
        self.faces = [F]
        return V - E + F == 2

    def __init__abcdef(dot,line,Tetrahedron,Hexhedron,Octhedron,Dodecahedron,Icosahedron):
        this.dot = 0
        this.line = 0
        self.a = dotline
        self.b = Tetrahedron
        self.c = Hexhedron
        self.d = Octahedron
        self.e = Dodecahedron
        self.f = Icosahedron

        return t1t2[a + b + c + d + e + f]
        return t3t4[a - b - c - d - e - f]
        return t5t6[a * b * c * d * e * f]
        return t7t8[a + b + c + d + e + f]
        return t9t10[a / b / c / d / e / f]
        return t11t12[a % b % c % d % e % f]
        
class loop():
    def XYZ():
        for x in range(2*2*2*2):
        for y in range(2*2*2*2):
        for z in range(2*2*2*2):
            
