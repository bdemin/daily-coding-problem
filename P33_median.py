# Compute the running median of a sequence of numbers. That is, given a stream
# of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers.

# For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2


def return_median(sequence):
    center = sequence[0]
    print(center)

    num_list = []
    num_list.append(center)
    
    for i in range(1, len(sequence)):
        if sequence[i] > center:
            num_list.append(sequence[i]) # Add larger item to the right side
        else:
            num_list.insert(0, sequence[i]) # Add smaller item to the left side

        half_len = int(len(num_list)/2)
        center = num_list[half_len]

        if len(num_list) % 2 == 0: # Even
            median = (num_list[half_len-1] + num_list[half_len])/2
        else:
            median = num_list[half_len] # Odd
        print(median)


sequence = [2, 1, 5, 7, 2, 0, 5]
return_median(sequence)