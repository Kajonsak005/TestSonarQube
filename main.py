def revert_string(string):
    result = ""
    for word in string.split(" "):
        result += word[::-1]+" "
    return result[:-1]


print(revert_string("Let's take LeetCode contest"))
