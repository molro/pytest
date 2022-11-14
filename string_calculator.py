# Step 1: Simple Calculator
# Create a simple String calculator with a single method:

class StringCalculator:

    def __init__(self, string_numbers):
        self.numbers = string_numbers
# class StringCalculator {
#     int Add(string numbers);
# }
# The method can take 1 or 2 comma-separated numbers, and will return their sum.

# The method returns 0 when passed the empty string.
    def Add(string_numbers):
        result = 0
        separated_numbers = string_numbers.split(",")
        # print(separated_numbers,"d")
        for num in separated_numbers:
            try:
                num_cache = int(num)
            except:
                result = 0
                # print(result,"c")
                return result
            else:
                result = result + num_cache
            
        # print(result,"b")
        return result
# Example:

# Add("") // 0
# Add("4") // 4
# Add("1,2") // 3
# Start with the simplest test case of an empty string and move to 1 and two numbers.