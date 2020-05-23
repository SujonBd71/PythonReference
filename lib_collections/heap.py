#if heap is constucted using tuple heap will automatically transfer sorting when there is a tie in first attribute

# Python code to demonstrate working of 
# heapify(), heappush() and heappop() 

# importing "heapq" to implement heap queue 
import heapq 
import heapPrint

def basicOperation():
    # initializing list 
    li = [5, 7, 9, 1, 3] 

    # using heapify to convert list into heap 
    heapq.heapify(li) 

    # printing created heap 
    print ("The created heap is : ",end="") 
    print (list(li)) 

    # using heappush() to push elements into heap 
    # pushes 4 
    heapq.heappush(li,4) 

    # printing modified heap 
    print ("The modified heap after push is : ",end="") 
    print (list(li)) 

    print(len(li))
    # using heappop() to pop smallest element 
    print ("The popped and smallest element is : ",end="") 
    print (heapq.heappop(li)) 
    print(len(li))


    # maxheap , any funcion with underscore is private , they shouldn't be used, as they can
    # be changed anytime without notice

    print()
    print("####### max heap")

    heapq._heapify_max(li)

    print(li[0])


def UserDefindedDataTypes():
    import heapq
    import heapPrint
    heap = []
    heapq.heappush(heap, (0,'one', 1))
    heapq.heappush(heap, (1,'two', 11))
    heapq.heappush(heap, (1, 'two', 2))
    heapq.heappush(heap, (1, 'one', 3))
    heapq.heappush(heap, (1,'two', 3))
    heapq.heappush(heap, (1,'one', 4))
    heapq.heappush(heap, (1,'two', 5))
    heapq.heappush(heap, (1,'one', 1))
    # show_tree(heap)


def UserDefiedSorting():
    # your custom function. Here, comparing tuples a and b based on their 2nd element
    def new_cmp_lt(self,a,b):
        if a[0] != b[0] :
            return a[0] < b[0]
        else:
            return a[1] < b[1]

    #override the existing "cmp_lt" module function with your function
    heapq.cmp_lt=new_cmp_lt
   
    heap = []
    heapq.heappush(heap, (0,'one', 1))
    heapq.heappush(heap, (1,'two', 11))
    heapq.heappush(heap, (10, 'two', 2))
    heapq.heappush(heap, (1, 'one', 3))
    heapq.heappush(heap, (11,'two', 3))
    heapq.heappush(heap, (11,'one', 4))
    heapq.heappush(heap, (1,'two', 5))
    heapq.heappush(heap, (1,'one', 1))
    heapPrint.show_tree(heap)

    while(len(heap) > 0):
        print(heapq.heappop(heap))


# UserDefindedDataTypes()
UserDefiedSorting()