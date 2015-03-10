Made by: Beh Chuen Yang                                                                         Protected by:GNU GPL v2.0
1.	List down all the last letters used and write down the total number of last letters.
Ans:11.A,B,C,D,E,U,V,X,Y,Z.
2.	Find a possible set of values for the different weights. Show how you arrived at the answer.
Weights:
A=9
B=10
C=2
D=3
Working:
Since digits 0,1,7,3, outputs a letter A,
And the digit with the corresponding weight A is 0,
We cannot find the value of A yet. But, we can find the values of weights B,C, and D respectively.
The largest possible weight is 10, as MOD 11 only allows for remainders of up to 10.
The smallest possible weight is 1, as if a weight is 0, then the formula WILL NOT work.
Thus,
Let B=1,C=2 and D=3,
Then the code 0,1,7,3, would be as follows,
(0 is ignored as we don’t know A. Anyway, its 0. (Anything x 0=0.))
((1x1)+(7x2)+(3x3))MOD11=2 and not 0 which is the remainder value of A.
Let’s assume that the very first weight here, or B, is wrong.
Thus the rest as follows,
((2x1)+(7x2)+(3x3))MOD11=3 which is not 0.
((3x1)+(7x2)+(3x3))MOD11=4 which is still not 0. 
And so on, so forth, until…
When we reach where the weight B is 10,
((10x1)+(7x2)+(3x3))MOD11=0 which is finally the corresponding remainder value for A.
Let’s try and find the weight A using another number: 4523, which ALSO has an output of A, and the corresponding remainder is ALSO 0.
So let’s assume that the weight A is 1, then the code 4,5,2,3 would be as follows,
((1x4)+(10x5)+(2x2)+(3x3))MOD11=1 and not 0.
Thus let’s assume weight A is wrong like what we did with weight B,
Then we shall go on like what we did when trying to find Weight B.
((2x4)+(10x5)+(2x2)+(3x3))MOD11=5 and not 0.
((3x4)+(10x5)+(2x2)+(3x3))MOD11=9 and not 0.
So on, so forth until when the weight A is assumed to be 9,
((9x4)+(10x5)+(2x2)+(3x3))MOD11=0 finally.
Thus, the weight A is 9.
And as for C and D? A similar method can be applied. Let’s use 4523 again.
This would be what happened if C=1, and D=2(They have to be different.):
((4x9)+(5x10)+(2x1)+(3x2))MOD11=6 which is FAR from the 0 that is A’s corresponding remainder value.
What if it was slightly bigger?(C=4,D=5)Then it would be as follows:
((4x9)+(5x10)+(2x4)+(3x5))MOD11=10. It is still quite far.
Thus, a possible value of the weights C and D is 2 and 3 respectively.
The list of remainder values are as follows:
0 to A,1 to D,2 to V,3 to Y, 4 to B, 5 to E,6 to W,7 to Z, 8 to C,9 to U, and 10 to X.
2c.Based on what you have investigated, find out the last letter of the following code (Show your working)
(i):4395:A	Working:((4x9)+(3x10)+(9x2)+(5x3))MOD11=(36+30+18+15)MOD11
								        =0(or A)
(ii):4461:Y	Working:((4x9)+(4x10)+(6x2)+(1x3))MOD11=(36+40+12+3)MOD11
								        =3(or Y)
3.	List AT LEAST 2 examples where some organizations use check digit system to generate last letter or check digit and briefly explain how it is being used.
Credit card companies (e.g. Diners Club, et cetera.) and barcodes. They both utilize the check digit system to verify the integrity of the credit card and to verify the price of the item being purchased.(Credit cards also utilize the Luhn algorithm which is used to generate the credit card numbers)
4.	Using the Excel file (or any other file) that you have created, find out the last letter of the following code:(working is not necessary)
(i)2156:(D)
(ii)9078:(U)
5.	What did you learn in the process of doing this assignment that had influenced the way you think about Mathematics?(You should elate your response with the mathematical concepts discussed in this assignment)
I learnt that the check digit system can be used for security purposes and that it serves well as a way to check for genuity in many systems.
