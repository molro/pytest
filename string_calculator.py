# Step 1: Simple Calculator
# Create a simple String calculator with a single method:


def split_numbers(string_numbers):        
    custom_separator = ''
    comma_separator = ','
    newline_separator = '\n'

    def separate_numbers(string_numbers, separator):
        separated_numbers = string_numbers.split(newline_separator)              
        joined_numbers = separator.join(separated_numbers)
        separated_numbers = joined_numbers.split(separator)
        return separated_numbers
        
    if (len(string_numbers) > 3):
        if (string_numbers[0] and string_numbers[1]) == '/':
            custom_separator = string_numbers[2]
            string_numbers_filtered = string_numbers[3:]
            separated_numbers = separate_numbers(string_numbers_filtered, custom_separator)
            return separated_numbers
        else:
            separated_numbers = separate_numbers(string_numbers, comma_separator)
            return separated_numbers
    else:             
        separated_numbers = separate_numbers(string_numbers, comma_separator)
        return separated_numbers

class StringCalculator:

    def __init__(self, string_numbers):
        self.numbers = string_numbers

    def Add(string_numbers):
        result = 0
        separated_numbers = split_numbers(string_numbers)
        print(separated_numbers,'dd')
        for num in separated_numbers:
            try:
                num_cache = int(num)
            except:
                result = 0
                return result
            else:
                result = result + num_cache
        return result