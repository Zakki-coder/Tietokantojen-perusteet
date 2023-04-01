import bikes

distance_of_user = bikes.distance_of_user("user123")
print("Test 1:", bikes.distance_of_user("user123"))
assert distance_of_user == 130160, "Distance of user should be 130160"

speed_of_user = bikes.speed_of_user("user123")
print("Test 2:", speed_of_user)
assert speed_of_user == 17.35, "Speed of user should be 17.35"

duration_in_each_city = bikes.duration_in_each_city("2021-06-01")
print("Test 3:", duration_in_each_city)
assert duration_in_each_city == [('city1', 58655), ('city2', 60947), ('city3', 59470), ('city4', 57488), ('city5', 59829), ('city6', 59925), ('city7', 57403), ('city8', 59354), ('city9', 59749), ('city10', 59296)], "Differences in arrays"

users_in_city = bikes.users_in_city("city5")
print("Test 4:", users_in_city)
assert users_in_city == 43102, "Users in city should be 43102"
# print("Test 5:", bikes.trips_on_each_day("city5"))
# print("Test 6:", bikes.most_popular_start("city5"))