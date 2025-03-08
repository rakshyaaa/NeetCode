import heapq

def best_fit_decreasing_heap(items, box_capacity):
    # Sort items in descending order  -> this takes O(n log n) time
    items.sort(reverse=True)
    
    #min-heap to track remaining space in each box
    heap = []

    
    for item in items: #finding box in a heap takes O(n)
        found_box = False
        
        # Search for a suitable box with the least leftover space
        for i in range(len(heap)):
            if heap[i] >= item:
                heap[i] -= item  # Update the box's remaining space
                heapq.heapify(heap) # Re-heapify to maintain order -> reheapifying takes O(log n) time
                print(heap)
                found_box = True
                break
        
        if not found_box:
            heapq.heappush(heap, box_capacity - item)  # Start a new box

    
    return len(heap)


items = [2, 5, 6, 7, 1, 3, 8, 9]
box_capacity = 10

# Run Algorithm
num_boxes = best_fit_decreasing_heap(items, box_capacity)
print(f"minimum boxes required: {num_boxes}")
 