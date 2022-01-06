// Q1:
function calculate(min,max){
    let sum=0
        for (let i=min; i<=max; i++){
            sum = sum +i    
        }
    console.log(sum);
}
calculate(1,3)
calculate(4,8)
    // console.log(data.employees[0].salary);
    // console.log(data.employees.length);
// Q2:
function avg(data){
    let sum = 0
        for (let i =0; i< data.employees.length; i++){
            sum = sum+ data.employees[i].salary
    }
    console.log(sum);
}
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
});

//Q3:
function maxProduct(nums){
    let newArray = []
    for(let i=0 ; i<nums.length; i++){
        for (let j=i+1; j<nums.length; j++){
           let result = nums[i] * nums[j]
            newArray.push(result)
        }
    }
    console.log(Math.max(...newArray))
    // console.log(newArray)
};
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])
// 5*20 5*2 5*6 =>[0]*[1] [0]*[2] [0]*[3]
// 20*2 20*6 =>[1]*[2] [1]*[3]
// 2*6 =>[2]*[3]
// first variable is 0 to 2
// second variable is first+1 to array.length

//Q4:
function twoSum(nums, target){
let resultList = []
    for (let i =0; i<nums.length; i++){
        for (let j=i+1; j<nums.length; j++){
            let answer = nums[i]+nums[j]
            // a = 1, print(a) =1 a==1, check a equal 1 or not
                if (target == answer){
                resultList.push(nums.indexOf(nums[i]), nums.indexOf(nums[j]))
                return resultList
            }
        }
    }
}
let result = twoSum([2,11,7,15], 9);
console.log(result)

//  2+11 2+7 2+15 =>[0]+[1] [0]+[2] [0]+[3]
//  11+7 11+15 =>[1]+[2] [1]+[3]
//  7+15 =>[2]+[3]
//  if result = 9, then push[i],[j] to resultList
