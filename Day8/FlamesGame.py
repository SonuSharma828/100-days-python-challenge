# Function to remove matching characters between two lists
def remove_match_char(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            # Check if characters from both lists match
            if list1[i] == list2[j]:
                # Store the matching character
                c = list1[i]
                # Remove the matching character from both lists
                list1.remove(c)
                list2.remove(c)
                # Combine modified lists with a separator and return along with a flag to proceed
                list3 = list1 + ["*"] + list2
                return [list3, True]
    # If no matches, return the combined lists and flag as False
    list3 = list1 + ["*"] + list2
    return [list3, False]

# Main program
if __name__ == "__main__":
    # Input for the first person and cleaning it up
    P1 = input("Enter the first person Name: ")
    P1 = P1.lower().replace(" ", "")
    p1 = list(P1)

    # Input for the second person and cleaning it up
    P2 = input("Enter the second person Name: ")
    P2 = P2.lower().replace(" ", "")
    p2 = list(P2)

    proceed = True

    # Process to remove matching characters between names until no matches remain
    while proceed:
        result = remove_match_char(p1, p2)
        con_list = result[0]
        proceed = result[1]
        star_index = con_list.index("*")
        # Splitting list at "*" to separate unmatched characters
        p1 = con_list[:star_index]
        p2 = con_list[star_index + 1:]
        count = len(p1) + len(p2)  # Count remaining characters

    # List of relationship outcomes based on count
    result1 = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]

    # Determine the relationship result by reducing the list based on count
    while len(result1) > 1:
        split_index = (count % len(result1) - 1)
        if split_index >= 0:
            right = result1[split_index + 1:]
            left = result1[:split_index]
            result1 = right + left
        else:
            result1 = result1[:len(result1) - 1]

    # Output the final relationship result
    print("The relationship between {} and {} is {}".format(P1, P2, result1[0]))
  
