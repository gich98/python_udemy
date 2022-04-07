# # List Comprehension
# numbers = [1, 2, 3]
# # new_list = [new_item for item in list]
# new_list = [(n + 1) for n in numbers]
# # Conditional List Comprehension
# new_list = [new_item for item in list if test]

# # Dictionary Comprehension
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # new_dict = {key: value for (key, value) in dict.items() if test}
# weather_f = {day: round(((temp * 1.8) + 32), 1) for (day, temp) in weather_c.items()}

# import pandas
#
# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98],
# }
#
# student_df = pandas.DataFrame(student_dict)
#
# # Loop through a data frame
# # for (key, value) in student_df.items():
# #     print(value)
#
# # Loop through rows of a data frame
# for (index, row) in student_df.iterrows():
#     print(row)
