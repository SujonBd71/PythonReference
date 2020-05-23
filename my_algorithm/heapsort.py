
def heap_sort():
    import copy
    index = -1
    data = []
    
    def __swim__(ind):
        if ind <= 1:
            return
        p = ind >>1
        if (p >=1) and (data[ind] < data[p]):
            data[ind], data[p] = data[p], data[ind]
            __swim__(p)
        
    def __sink__(ind):
        if ind >= len(data) - 1:
            return
        
        l = ind<<1
        r = l + 1
        mi = l
        
        if l >=len(data):
            return

        if (r < len(data)) and (data[r] < data[l]):
            mi = r
        if data[mi] < data[ind]:
            data[mi], data[ind] = data[ind], data[mi]
            __sink__(mi)

    def push(x):
        nonlocal index
        if (index == -1):
            data.append(x)
            index = index + 1
        
        data.append(x)
        index = index + 1
        __swim__(index)

    def pop_min():
        # print(data)
        top = data[1]
        if (len(data) > 2):
            data[1], data[-1] = data[-1], data[1]
        
        # print(top)
        data.pop()
        __sink__(1)
        return top

    def pop_item(x):
        pass

    def Diff(li1, li2): 
        return (list(set(li1) - set(li2))) 

    def test():
        import random
        nums = [random.randrange(5, 10000000) for i in range(200000)]
        nums2 = copy.deepcopy(nums)
        nums.sort()

        soreted_nums = []
        for x in nums2:
            push(x)
        
        while len(data) > 1:
            soreted_nums.append(pop_min())

        for i in range(len(nums)):
            if nums[i] != soreted_nums[i]:
                print("not equal")
                break
   
    test()

heap_sort()
