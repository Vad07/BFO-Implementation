import math 
import random
from random import randint
import test

threshold  = 0;

flag = 0;

flag1 = 0;

last =255;

theta = [205, 78, 47, 165, 239, 178, 9, 175, 233, 123, 251, 216, 58, 26, 96, 199, 220, 15, 206, 83, 154, 235, 143, 245, 64, 79, 210, 63, 42, 82, 69, 134, 111, 50, 227, 229, 159, 156, 160, 145, 197, 124, 72, 228, 55, 77, 2, 189, 10, 18, 209, 122, 100, 20, 226, 129, 34, 37, 137, 200, 31, 240, 242, 62, 87, 136, 91, 59, 7, 106, 90, 135, 198, 27, 179, 158, 139, 241, 138, 144, 104, 211, 97, 148, 19, 108, 125, 192, 118, 46, 230, 12, 109, 161, 195, 221, 93, 246, 248, 196, 99, 225, 52, 120, 49, 188, 73, 67, 238, 207, 119, 163, 232, 43, 35, 254, 215, 21, 126, 127, 113, 41, 61, 75, 94, 172, 141, 89, 71, 219, 110, 45, 150, 234, 36, 112, 171, 131, 11, 237, 102, 32, 250, 54, 208, 4, 213, 29, 180, 243, 168, 60, 169, 201, 214, 13, 114, 116, 223, 23, 244, 185, 181, 84, 190, 247, 53, 28, 255, 6, 193, 253, 149, 167, 202, 17, 66, 22, 57, 191, 186, 44, 130, 14, 170, 1, 81, 105, 48, 88, 236, 155, 95, 25, 152, 166, 252, 38, 217, 5, 0, 157, 65, 176, 16, 140, 103, 76, 40, 121, 249, 173, 218, 24, 115, 183, 147, 68, 153, 231, 142, 3, 224, 187, 107, 177, 86, 51, 146, 132, 74, 133, 212, 56, 164, 174, 98, 203, 182, 30, 70, 39, 117, 80, 128, 33, 184, 8, 85, 222, 162, 194, 204, 151, 101, 92]
 
non_li = test.value_nonl(theta)

print non_li

fo = open("substitution.txt", "wb")


iterate = 0;


def nutrientsfunc(theta,flag,first,last):
	i = 0
	if flag==1:  
		J=0;
		
	else:
		J = math.floor(5*math.exp(-0.1*((theta[first]-15)^2+(theta[last]-20)^2))+2*math.exp(-0.08*((theta[first]-20)^2+(theta[last]-15)^2))+3*math.exp(-0.08*((theta[first]-25)^2+(theta[last]-10)^2)));
		if J > 255:
			J = J%255;
		#print J
	return J	

threshold = nutrientsfunc(theta,flag,1,255)

node = 0

miss = 0

S1 = 102;

S2 = 0;

diff = 0;
user_hits = input('Enter the maximum number of hits desired')

print user_hits

swim_length = 4

lower_limit = 0

upper_limit = 127

user_iter = input('Enter the max iterations to be performed')

print user_iter

empty_array = []

for i in range(255):

	empty_array.append(0);

x = random.randint(lower_limit,upper_limit)

print('the random number is',x)

#x=81;
while user_hits!= 0:

	# x = random.randint(lower_limit,upper_limit)


	for iterate in range(user_iter):


		t = theta[node] + nutrientsfunc(theta,flag,node,last);
		
		f = theta[node+x] + nutrientsfunc(theta,flag,node+x,last);
		
		diffrence = f - t;

	# iterate = iterate + 1;

		if diffrence > threshold: 


			temp = theta[node];

			theta[node] = theta[node+4];

			theta[node+4] = temp;

			node = node + 4;

			flag1 = 1;

		if node > 251:

			break;

	# if S2 > S1:

	# 	break;
	
	# else:

	# 	miss = miss + 1;
	non_lf = test.value_nonl(theta)

	# print non_lf

	if non_lf >= non_li:

		# print theta

		# print flag1

		# # fo.write(theta)

		# for item in theta:

  # 			fo.write("%s\n" % theta)


		# fo.write('\n\n')

		user_hits = user_hits - 1




# print is_bijective(empty_array)


print flag1

print theta

		
		
# for item in theta:

fo.write("%s\n" % theta)

fo.write('\n\n')

fo.close()

# print theta
			






