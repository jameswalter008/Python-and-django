nums=[1,2,3,4,5,6,7,8,9,10]

#________filter way__________#
# def even(num):
#     return num%2==0

# evenumbs=list(filter(even,nums))
# print(evenumbs);

# nums=[num for num in nums if num%2==0]
# print(nums);

# evenNums=[]

# for num in nums:
#     if (num%2)==0:
#         evenNums.append(num);
# print(evenNums);

#___________lambda way___________#
evennums=list(filter(lambda num: num%2==0,nums))
print(evennums)