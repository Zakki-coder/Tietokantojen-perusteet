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

trips_on_each_day = bikes.trips_on_each_day("city5")
print("Test 5:", trips_on_each_day)
assert trips_on_each_day == [('2021-06-01', 3362), ('2021-06-02', 3345), ('2021-06-03', 3313), ('2021-06-04', 3276), ('2021-06-05', 3376), ('2021-06-06', 3365), ('2021-06-07', 3351), ('2021-06-08', 3355), ('2021-06-09', 3284), ('2021-06-10', 3324), ('2021-06-11', 3272), ('2021-06-12', 3399), ('2021-06-13', 3308), ('2021-06-14', 3287), ('2021-06-15', 3266), ('2021-06-16', 3376), ('2021-06-17', 3321), ('2021-06-18', 3390), ('2021-06-19', 3320), ('2021-06-20', 3319), ('2021-06-21', 3303), ('2021-06-22', 3429), ('2021-06-23', 3234), ('2021-06-24', 3305), ('2021-06-25', 3260), ('2021-06-26', 3350), ('2021-06-27', 3196), ('2021-06-28', 3222), ('2021-06-29', 3252), ('2021-06-30', 3439)], "Arrays not matching"

most_popular_start = bikes.most_popular_start("city5")
print("Test 6:", most_popular_start)
assert most_popular_start == ('stop419', 1073), "Should be ('stop419', 1073)"