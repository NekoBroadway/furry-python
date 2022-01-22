#Exc 1 - Print text below in similar formating
#
#Twinkle, twinkle, little star,
#	How i wonder what you are! 
#		Up above the world so high,   		
#		Like a diamond in the sky. 
#Twinkle, twinkle, little star, 
#	How i wonder what you are

row_1 = "Twinkle, twinkle, little star,"
row_2 = "\n\tHow i wonder what you are"
row_3 = "\n\t\tUp above the world so high,"
row_4 = "\n\t\tLike a diamond in the sky."

res = row_1 + row_2 + '!' + row_3 + row_4 + '\n' + row_1 + row_2
print(res)