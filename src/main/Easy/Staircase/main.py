import unittest
inputs = [
    6
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

def function(n):
    for i in range(n):
        print((n-i-1)*' '+(i+1)*'#')

if __name__ == '__main__':
    function(6)
    # test = Test()
    # test.testExactMatch(inputs,function,outputs)