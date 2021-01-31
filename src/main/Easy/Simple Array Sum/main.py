import unittest
inputs = [
    [0,1,2,3],
    [-1]
]
outputs=[
    6,
    -1
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

def function(ar):
    result = 0
    for i in ar:
        result += i
    return result

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)