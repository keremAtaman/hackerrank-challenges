import unittest
inputs = [
    [[17,28,30],[99,16,8]],
    [[0,0,0],[0,0,0]],
    [[1,1,1],[0,1,1]]
]
outputs=[
    [2,1],
    [0,0],
    [1,0]
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
            self.assertEqual(function(inputs[i][0],inputs[i][1]),expectedOutputs[i])

def function(a,b):
    result = [0,0]
    for i in range(len(a)):
        if a[i]>b[i]:
            result[0] +=1
        elif b[i] > a[i]:
            result[1]+=1
    return result

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)