# this program will generate lists and lengths


long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 10)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)

#completed range() = big_range
big_range_length = len(big_range)
print(big_range_length)

#change the range(), generates big_range and skips 100 steps instead of 10

big_range = range(2, 3000, 100)
big_range_length = list(big_range)
print(big_range_length)