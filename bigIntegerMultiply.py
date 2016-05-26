def add(first_number, second_number):
	len_first = len(first_number)
	len_second = len(second_number)
	# make sure both the number are some length
	if len_first <= len_second:
		first_number = "0"*(len_second - len_first) + first_number
		len_first = len(first_number)
	else:
		second_number = "0" * (len_first - len_second) + second_number
		len_second = len(second_number)
	
	assert(len_first == len_second)

	sum_value = ""
	value_left_last_i_i = 0
	for i in range(len_first-1,-1,-1):
		sum_i_i = int(first_number[i]) + int(second_number[i])
		sum_i_i += value_left_last_i_i
		value_left_last_i_i = int(sum_i_i / 10)
		sum_value = str(sum_i_i % 10) + sum_value

	# in case there are value in value_left_last_i_i
	if value_left_last_i_i > 0:
		sum_value = str(value_left_last_i_i) + sum_value

	return sum_value


def multiply(first_number, second_number):
	each_multiply = []
	for i in range(len(second_number)-1, -1, -1):
		
		value_i = int(second_number[i])
		
		# add zeros to the end to align the numbers properly
		num_zeros = len(second_number) - i - 1
		value_i_all_j = "0" * num_zeros

		# store the value for value_i_j / 10, which is should be added to the next multiply value
		value_left_last_i_j = 0
		
		for j in range(len(first_number)-1, -1, -1):
			value_i_j = value_i * int(first_number[j])
			value_i_j += value_left_last_i_j
			value_left_last_i_j = int(value_i_j / 10)
			value_i_all_j = str(value_i_j % 10) + value_i_all_j
		
		# in case there is value in value_left_last_i_j
		if value_left_last_i_j  > 0:
			value_i_all_j = str(value_left_last_i_j) + value_i_all_j

		each_multiply.append(value_i_all_j)
	

	value_sum = each_multiply[0]
	for i in range(1,len(each_multiply)):
		value_sum = add(value_sum, each_multiply[i])

	return value_sum


if __name__ == '__main__':
	first_number = "1234567890123341232423424242"
	second_number = "3487827478787492894719841"
	print multiply(first_number, second_number)