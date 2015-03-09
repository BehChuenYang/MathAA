print'MADE BY BEH CHUEN YANG:PROTECTED UNDER GNU GPL SO NO ONE CAN COPY AND PASS OFF AS THEIR OWN'
print 'DISCLAIMER: When looking at the code, please forgive the fact that Python ignores 0. As such I had to add 1 to every piece of String(A-E).Also, you can only run the program once before having to run it again.'
a=int(raw_input('Enter the first digit.'))
b=int(raw_input('Now enter the second.'))
c=int(raw_input('Now enter the third.'))
d=int(raw_input('Now enter the last.'))
e=1
A=9
B=10
C=2
D=3
StringA=A*a+e
StringB=B*b+e
StringC=C*c+e
StringD=D*d+e
StringE=StringA+StringB+StringC+StringD
if StringE %11==4:
     print 'The last letter is A!' 
     
elif StringE %11==7:
     print 'The last letter is Y!'

elif StringE %11==10:
     print 'The last letter is W!'

elif StringE %11==2:
     print 'The last letter is U!'

elif StringE %11==5:
     print 'The last letter is D!'

elif StringE %11==8:
     print 'The last letter is B!'

elif StringE %11==0:
     print 'The last letter is Z!'

elif StringE %11==3:
     print 'The last letter is X!'

elif StringE %11==6:
     print 'The last letter is V!'

elif StringE %11==9:
     print 'The last letter is E!'

elif StringE %11==1:
     print 'The last letter is C!'
x=raw_input('Do you want to know how I did it?(Type(Python is case-sensitive) Yes or No)')
if x=='Yes':
     print 'Look at the code using Python Shell!'

elif x=='No':
     print 'Ok...'
else:
      pass
     
#This is the end
