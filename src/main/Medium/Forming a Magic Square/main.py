import unittest
inputs = [
    [[5,3,4],[1,5,8],[6,4,2]],
    [[4,9,2],[3,5,7],[8,1,5]],
    [[4,8,2],[4,5,7],[6,1,6]],
    [[8,3,4],[1,5,9],[6,7,2]],
    [[5,5,5],[5,5,5],[5,5,5]]
]
outputs=[
    7,
    1,
    4,
    0,
    20
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

possible_answers=[
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]

def function(s):
    possible_costs=[]
    for possible_answer in possible_answers:
        cost = 0
        for possible_answer_row, s_row in zip(possible_answer,s):
            for possible_answer_member, s_member in zip(possible_answer_row,s_row):
                cost += abs(possible_answer_member-s_member)
        possible_costs.append(cost)

    return min(possible_costs)

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)