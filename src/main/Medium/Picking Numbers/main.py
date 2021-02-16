import unittest
inputs = [
    [1,1,2,2,4,4,5,5,5],
    [4,6,5,3,3,1],
    [1,2,2,3,1,2]
]
outputs=[
    5,
    3,
    5
]

class Test(unittest.TestCase):
    def testExactMatch(self,inputs, function, expectedOutputs):
        """Tests if each entry of inputs passed to the function maps to corresponding entry of expectedOutputs
        Essentiallty, this function does function(inputs[i]) == outputs[i]

        Args:
            inputs (list): The set of inputs, where inputs[0] is the first set of inputs
            function (function): The function that maps inputs to outputs
            expectedOutputs (list): The set of expected outputs, where expectedOutputs[0] is the first set of expected outputs
        """
        for i in range(len(inputs)):
            function_output =function(inputs[i]) 
            self.assertEqual(function_output,expectedOutputs[i],"For the input " +str(inputs[i])+" the expected value was " 
            + str(outputs[i]) + " but got " + str(function_output)+ " instead")

def function(a):
    #sort the array
    a.sort()
    current_streak = 0
    longest_streak = 0
    lowest_value_of_current_streak = a[0]
    for element in a:
        if lowest_value_of_current_streak +1 >= element:
            current_streak +=1
        else:
            if current_streak>longest_streak:
                longest_streak = current_streak
            current_streak = 1
            lowest_value_of_current_streak = element
    #ensure if the last element was a part of the longest streak, it updates the longest streak #
    if current_streak>longest_streak:
        longest_streak = current_streak
    return longest_streak

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)