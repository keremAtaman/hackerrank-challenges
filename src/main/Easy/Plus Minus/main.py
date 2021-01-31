import unittest
inputs = [
    [-4, 3, -9, 0, 4, 1]
]
outputs=[
    [0.500000,0.333333,0.166667]
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
            self.assertEqual(function(inputs[i]),expectedOutputs[i])

def function(arr):
    result = [0,0,0]
    len_ = len(arr)
    for i in arr:
        if i >0:
            result[0]+=1
        elif i<0:
            result[1]+=1
        else:
            result[2]+=1
    for i in range(3):
        print(round(result[i]/len_,6))


def helper(decimalToRound,numDecimalPlaces):
    return round(decimalToRound,numDecimalPlaces)

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)