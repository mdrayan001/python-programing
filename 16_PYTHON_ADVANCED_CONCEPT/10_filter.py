# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False

a = [1,3,4,67,45,839,2134,0,9,8,7869,2,11,10,756,7,5]

new = list(filter(lambda x: x>9, a))
print(new)