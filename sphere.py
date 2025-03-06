from sympy import polyhedron
import trimesh
import math

class spacetime():
    def Hexadecimal():
         a = "00001011"
         b = "00001000"
         c = "00001110"
         d = "00001110"
         e = "00001111"
         f = "00010000"
    def space(X,Y,Z,Radius,theta,fai):
         this.X = Radius * theta
         this.Y = Radius * fai
         this.Z = Radius * theta * fai
    def time(x,y,z,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12):
        return [
            a * sin(x + t1) + b * cos(x - t1) + c * sin(y + t2) + d * cos(y - t2) + e * sin(z + t3) + f * cos(z - t3),       #t123
            a * asin(x + t4) + b * acos(x - t4) + c * asin(y + t5) + d * acos(y - t5) + e * asin(z + t6) + f * acos(z - t6), #t456
            a * sinh(x + t7) + b * cosh(x - t7) + c * sinh(y + t8) + d * cosh(y - t8) + e * sinh(z + t9) + f * cosh(z - t9), #t789
            a * tan(x + t10) + b * atan(x - t10) + c * tan(y + t11) + d * atan(y - t11) + e * tan(z + t12) + f * atan(z - t12) #t101112
        ]

class wiki():
    def __init__polyhedron(Vertex,Edges,faces):
        self.Vertex = [V]
        self.Edged = [E]
        self.faces = [F]
        return V - E + F == 2

    def __init__abcdef(dotline,Tetrahedron,Hexhedron,Octhedron,Dodecahedron,Icosahedron):
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
        return t1t2[a + b + c + d + e + f]
        return t3t4[a / b / c / d / e / f]
        return t5t6[a % b % c % d % e % f]

      
        
