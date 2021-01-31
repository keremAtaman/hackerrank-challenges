import unittest
inputs = [
    [[1,2,3],[4,5,6],[9,8,9]]
]
outputs=[
    2
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
    #get the # of rows and cols of the matrix
    len_ = len(arr[0])
    #check if the matrix is empty
    if len_ == 0:
        return 0
    firstDiagonal:int = 0
    secondDiagonal:int = 0
    for i in range(len_):
        firstDiagonal+= arr[i][i]
        secondDiagonal+=arr[i][len_-1-i]
    return abs(firstDiagonal-secondDiagonal)


if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)