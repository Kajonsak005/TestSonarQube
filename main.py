def revert_string(string):
    if (len(string) < 1 or len(string) > 5000):
        raise Exception("String over length or less")
    result = ""
    for word in string.split(" "):
        result += word[::-1]+" "
    return result[:-1]


print(revert_string("Let's take LeetCode contest"))
