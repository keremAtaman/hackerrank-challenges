import unittest
inputs = [
    [[100,90,90,80],[70,80,105]],
    [[100,100,50,40,20,10],[5,25,50,120]]
]
outputs=[
    [4,3,1],
    [6,4,2,1]
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

def function(in_):
    return climbingLeaderboard(in_[0],in_[1])

#ranked is in descending order and player is in ascending order
def climbingLeaderboard(ranked, player):
    score_set = []
    last_added_element = None
    for i in ranked:
        if last_added_element != i:
            score_set.append(i)
            last_added_element = i
    result = []
    worst_rank_score = score_set[-1]
    best_rank_score = score_set[0]
    num_scores = len(score_set)
    last_place = num_scores + 1
    score_set_index = -1
    player_previous_score = -1
    player_previous_rank = last_place
    player_rank = -1
    for score in player:
        #player had the best score in previous iteration, so they must have the best score in this one
        if player_previous_rank == 1:
            player_rank = 1
        elif score >= best_rank_score:
            player_rank = 1
        elif score < worst_rank_score:
            player_rank = last_place
        elif score == player_previous_score:
            player_rank = player_previous_rank
        #this is a new score that is geq worst score and less than best score, this score can exactly be one of the scores
        else:
            #keep iterating until we hit a score in ranked geq current player score
            while(score > score_set[score_set_index]):
                score_set_index -=1
            #current score equals an entry in the dictionary
            if score == score_set[score_set_index]:
                player_rank = num_scores + score_set_index +1
            #current score is less than a dictionary entry
            else:
                player_rank = num_scores + score_set_index +2

        result.append(player_rank)
        player_previous_rank = player_rank
        player_previous_score = score
   
    return result

if __name__ == '__main__':
    test = Test()
    test.testExactMatch(inputs,function,outputs)
    print("Done")