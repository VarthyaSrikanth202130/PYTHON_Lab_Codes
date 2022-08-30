""" Function to return all permutations of a given string
_____________________ PYTHON Lab-2 _____________________ """

# Declaring a function to print all permutations
def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    # finds next lexicographic string and returns next_list
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                # Appending the permutations to the list
                next_list.append(new_str)
    return next_list

# Driver code
string = input("Please enter a string of length 3: ")
permutations = permute_string(string)
print(permutations)
