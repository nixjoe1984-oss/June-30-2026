class pair:
    def twosum(self,nums,target):
        dict={}
        for i, num in enumerate(nums):
            if target - num in dict:
                return(dict[target-num],i)
            dict[num]=i
l1=[10,20,30,40,50,60,70]
print(list(enumerate(l1)))
value=int(input("Enter sum for which you want to make this search: "))
print("Index 1: %d, Index 2: %d" %pair().twosum((10,20,30,40,50,60,70),value))