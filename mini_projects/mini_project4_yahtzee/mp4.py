"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
http://www.codeskulptor.org/#user40_QoIJJrSzT9_34.py
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand
    
    Returns an integer score 
    """
    hand_val={}
    for dval in tuple(sorted(hand)):
        hand_val[dval]=hand_val.get(dval, 0) + dval
    return max(hand_val.values())

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    rolls=gen_all_sequences((range(1,num_die_sides+1)), num_free_dice)
    tot_hand_score=0.0
    for new_hand in rolls:
        full_hand=held_dice+new_hand
        full_hand_score=score(full_hand)
        tot_hand_score += full_hand_score
    return tot_hand_score/len(rolls)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    power_set = [()]
    for dice in hand:
        for subset in power_set:
            power_set = power_set + [subset+(dice,)]
    return set(power_set)


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    current_val=float('-inf')
    holding_hands=gen_all_holds(hand)
    for hold_hand in holding_hands:
        evalue=expected_value(hold_hand, num_die_sides, len(hand)-len(hold_hand))
        if evalue > current_val:
            current_val=evalue
            result=(current_val,(hold_hand))
    return result


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    #num_die_sides = 6
    #hand = (1, 1, 1, 5, 6)
    #hand =  (2,3,3,3,4)
    #print score(hand)
    #expected_value((2,2),6,2)
    #expected_value((6,6),6,1)
    #expected_value((1,), 6, 5)
    #expected_value((2, 4), 6, 3)
    #expected_value((5, 5), 6, 4)
    #print gen_all_holds((1,2,3,3,4))
    #print gen_all_holds((1,))
    #print gen_all_holds((4, 6))
    #hand_score, hold = strategy(hand, num_die_sides)
    #print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    #print gen_all_sequences((1,2), 2)
    print strategy((1,), 6)
    
#run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    




