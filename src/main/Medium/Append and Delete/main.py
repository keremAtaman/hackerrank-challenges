import unittest
inputs = [
    ["test","test2",0],
    ["test","test",0],
    ["hackerhappy","hackerrank",9],
    ["aba","aba",7],
    ["ashley","ash",2],
    ["","ab",1]
]
outputs=[
    "No",
    "Yes",
    "Yes",
    "Yes",
    "No",
    "No"
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
    s:str = input_[0]
    t:str = input_[1]
    k:int = input_[2]
    #see how many of the first characters of the strings match
    numSameBeginningChars = 0
    for sChr,tChr in zip(s,t):
        if sChr == tChr:
            numSameBeginningChars+=1
        else:
            break

    minNumChanges = len(s)+len(t) - 2*numSameBeginningChars
    if  minNumChanges== k:
        return "Yes"
    #we have enough deletes to wipe first one and put in second one
    elif len(s) + len(t) <=k:
        return "Yes"
    #we have enough changes to add/remove chars after the minimum # of changes required has been made
    elif k>=minNumChanges and ((k-minNumChanges)%2 == 0):
        return "Yes"
    else:
        return "No"
    

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)
    print("Done")