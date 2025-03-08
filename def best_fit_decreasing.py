def best_fit_decreasing(items, box_capacity):
    # Sort items in descending order  -> this takes O(n log n) time
    items.sort(reverse=True)
    
    boxes = []
    
    for item in items: 
        found_box = False
        
        for box in boxes:
            if sum(box) + item <= box_capacity:
                box.append(item)
                found_box = True
                break
        
        if not found_box:
            boxes.append([item])  

    
    return boxes


items = [2, 5, 6, 7, 1, 3, 8, 9]
box_capacity = 10

# Run Algorithm
num_boxes = best_fit_decreasing(items, box_capacity)
print(f"minimum boxes required: {num_boxes}")
 