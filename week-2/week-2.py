# Q1:
def calculate(min, max):
    sum=0
    for x in range(min,max+1):
        sum=sum+x
    print(sum)

calculate(4,8)
calculate(1,3)

# Q2: 
def avg(data):
    sum = 0
    for i in range(len(data["employees"])):
        # print(data["employees"])
        # print(i)
        sum = sum + data["employees"][i]["salary"]
        # print(data["employees"][i]["salary"])
    print(sum)
#below is call def
avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
})

# print(avg["employees"][2]["salary"]) #50000
# print(range(len(avg["employees"]))) #[0,1,2]
# for i in range(len(avg["employees"])):
#   print(i) #0 change line 1 change line 2
# print(avg["employees"]) #print list [{'salary': 30000, 'name': 'John'}, {'salary': 60000, 'name': 'Bob'}, {'salary': 50000, 'name': 'Jenny'}]

# Q3: 1. calculate each element times each other 2. compare the max value by if
def maxProduct(nums):
    productList=[]
    for x in range(len(nums)): 
        for y in range(x+1, len(nums)):
            productList.append(nums[x] * nums[y])
    print(max(productList))
    # print(len(nums)) #4
    # print(range(len(nums))) #[0,1,2,3]

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1,2])
maxProduct([-1,0,2])
maxProduct([-1, -2, 0])

        # 5*20 5*2 5*6
        # 20*2 20*6
        # 2*6

# Q4:
def twoSum(nums, target):
    resultList=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            answer = nums[i]+nums[j]
            if answer == target:
                # array = [1,2]
                # array.extend([3,4]), it suit to add array=> [1,2,3,4]
                # array.append([3,4]), it suit to add element=>[1,2,[3,4]]
                resultList.extend([nums.index(nums[i]),nums.index(nums[j])])
                return resultList
result=twoSum([2, 11, 7, 15], 9)
print(result)
# 2+11 2+7 2+15 =>[0]+[1] [0]+[2] [0]+[3]
# 11+7 11+15 =>[1]+[2] [1]+[3]
# 7+15 =>[2]+[3]
# if result = 9, then append[i],[j] to resultList
