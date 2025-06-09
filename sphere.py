
import math

class equation():
   def Hexadecimal(a,b,c,d,e,f):
         a = 1/7
         b = 2/7
         c = 3/7
         d = 4/7
         e = 5/7
         f = 6/7
   def  x(a,b,c,d,e,f,n):
        x + n = a * n^5 + b * n^4 + c * n^3 + d * n^2 + e * n + f
        x - n = a * n^4 + b * n^3 + c * n^2 + d * n + e * n^(-1) + f
   def  y(a,b,c,d,e,f,n):
        y + n = a * n^3 + b * n^2 + c * n + d * n^(-1) + e * n^(-2) + f
        y - n = a * n^2 + b * n + c * n^(-1) + d * n^(-2) + e * n^(-3) + f
   def  z(a,b,c,d,e,f,n):      
        z + n = a * n + b * n^(-1) + c * n^(-2) + d * n^(-3) + e * n^(-4) + f
        z - n = a * n^(-1) + b * n^(-2) + c * n^(-3) + d * n^(-2) + e * n^(-5) + f

class spacetime():
    def Hexadecimal(A,B,C,D,E,F):
         A = "00001011"
         B = "00001100"
         C = "00001101"
         D = "00001110"
         E = "00001111"
         F = "00010000"
    def space(X,Y,Z,Radius,theta,fai):
         X = Radius * math.cos(theta)
         Y = Radius * math.sin(fai)
         Z = Radius * math.cos(theta) * math.cos(fai)
    def time(A,B,C,D,E,F,X,Y,Z,N):
        return [
            A * math.sin(X + N) + B * math.cos(X - N) + C * math.sin(Y + N) + D * math.cos(Y - N) + E * math.sin(Z + N) + F * math.cos(Z - N),       
            A * math.asin(X + N) + B * math.acos(X - N) + C * math.asin(Y + N) + D * math.acos(Y - N) + E * math.asin(Z + N) + F * math.acos(Z - N),
            A * math.sinh(X + N) + B * math.cosh(X - N) + C * math.sinh(Y + N) + D * math.cosh(Y - N) + E * math.sinh(Z + N) + F * math.cosh(Z - N),
            A * math.tan(X + N) + B * math.atan(X - N) + C * math.tan(Y + N) + D * math.atan(Y - N) + E * math.tan(Z + N) + F * math.atan(Z - N)
        ] 
