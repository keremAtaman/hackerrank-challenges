import unittest
inputs = [
    [3,9],
    [17,24],
    [9,9],
    [24,49]
]
outputs=[
    2,
    0,
    1,
    3
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

def function(input_):
    import math
    a:int = input_[0]
    b:int = input_[1]
    #find the least number whose square is geq to a
    lower_square = math.ceil(math.sqrt(a))
    #find the highest number whose square is leq to b
    upper_sqare = math.floor(math.sqrt(b))
    #find all the #s between a and b
    return upper_sqare-lower_square+1

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)
    print("Done")