"""
Erica Miller
2031854
"""


def selection_sort_descend_trace(num_list):
    list_size = len(num_list)

    for i in range(list_size - 1):
        max_index = i
        for j in range(i + 1, list_size):
            if num_list[j] > num_list[max_index]:
                max_index = j

        # Swap the found maximum element with the first element
        num_list[i], num_list[max_index] = num_list[max_index], num_list[i]

        # Output the list after each iteration of the outer loop
        print(" ".join(map(str, num_list)), end = " \n")


if __name__ == "__main__":
    # Read input list of integers
    input_list = list(map(int, input().split()))

    # Call the selection_sort_descend_trace function
    selection_sort_descend_trace(input_list)
