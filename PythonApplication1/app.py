#Exc 1 - Print text below in similar formating
#
#twinkle, twinkle, little star,
#	how i wonder what you are! 
#		up above the world so high,   		
#		like a diamond in the sky. 
#twinkle, twinkle, little star, 
#	how i wonder what you are

row_1 = "Twinkle, twinkle, little star,"
row_2 = "\n\tHow i wonder what you are"
row_3 = "\n\t\tUp above the world so high,"
row_4 = "\n\t\tLike a diamond in the sky."

res = row_1 + row_2 + '!' + row_3 + row_4 + '\n' + row_1 + row_2
print(res)