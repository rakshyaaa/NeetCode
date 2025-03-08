import heapq

def best_fit_decreasing_with_heap_tracking(items, box_capacity):
    # Step 1: Sort items in decreasing order
    items.sort(reverse=True)

    # Min-Heap to store (remaining capacity, box index)
    heap = []
    box_contents = []  # List to store items in each box

    for item in items:
        if heap and heap[0][0] >= item:  # If a box has enough space
            remaining_space, box_index = heapq.heappop(heap)  # Get the best box
            box_contents[box_index].append(item)  # Place item in the box
            heapq.heappush(heap, (remaining_space - item, box_index))  # Update heap
        else:
            # Create a new box
            box_index = len(box_contents)
            box_contents.append([item])  # New box stores the item
            heapq.heappush(heap, (box_capacity - item, box_index))  # Add to heap

    # Print the packed boxes
    for i, box in enumerate(box_contents):
        print(f"Box {i+1}: {box}")

    return len(box_contents)  # Number of boxes used

# Given list of items and box capacity
items = [2, 5, 6, 7, 1, 3, 8, 9]
box_capacity = 10

# Run the function
num_boxes = best_fit_decreasing_with_heap_tracking(items, box_capacity)
print(f"Total boxes used: {num_boxes}")
