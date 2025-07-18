'''
#Question1
bio = input("Enter your bio")
print(len(bio))

bio1 = bio.split()

print(bio1[0:20])
print(len(bio1))
bio2 = bio1[-20:]
print(bio2)

#Question2
Total_bill = float(input("Enter the Total bill: "))

user = int(input("Total the number of people: "))

bill_per_person = Total_bill / user

print(f"Every one is suppose to pay the sum of ${bill_per_person}")

#Qusetion3

Fav_movie = input("What's your fav. movie: ")
number_movie_watch = float(input("Number of times watched?: "))

print(f"I've watched {Fav_movie} {number_movie_watch} times")
print(Fav_movie.upper())
print(Fav_movie[-3:])

#Question4

Day1_step = float(input("Enter Day 1 steps: "))
Day2_step = float(input("Enter Day 2 steps: "))
Day3_step = float(input("Enter Day 3 steps: "))

Total_steps = Day1_step + Day2_step + Day3_step
numbers_of_days = 3
average_step = Total_steps / numbers_of_days

print(f" You walk a total of {Total_steps:,} steps in 3 days. that's an average of {average_step:,} per day.")
'''
# Question5

password = (input("Enter user password: "))
print(password[0] +  password[-1])

length = len(password)
star = password[0] + ((length - 2 ) * ("*")) + password[-1] 
print(star)
