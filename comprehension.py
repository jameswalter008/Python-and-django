nums=[1,2,3,4,5,6,7,8,9,10]


# for num in nums:
#     if(num%2==0):
#         evendoublenums.append(num*2);
# print(evendoublenums);
evendoublenumbers=[num*2 for num in nums if num%2==0]
print(evendoublenumbers);