import math
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length
    """
    
    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                temp.add(tuple(new_seq))
        ans = temp
    return ans

#Question 1
#print len(gen_all_sequences((0,1),5))

#Question 2
#print (gen_all_sequences((1,2),2))
#print (gen_all_sequences((3,4),2))


#Question 6:
#def gen_permutations(outcomes, num_trials):
#	ans = []
#	states=gen_all_sequences(outcomes, num_trials)
#	for item in states:
#		if len(item)==len(set(item)):
#			ans.append(item)
#	return ans

#outcome = set(["a", "b", "c", "d", "e", "f"])
#permutations = gen_permutations(outcome, 4)
#permutation_list = list(permutations)
#permutation_list.sort()
#print "Answer is", permutation_list[100]

#Another approach

def gen_permutations(outcomes, length):
    """
    Iterative function that generates set of permutations of
    outcomes of length num_trials
    No repeated outcomes allowed
    """
    ans = set([()])

    for dummy_idx in range(length):
	temp = set()
	for seq in ans:
       	    for item in outcomes:
                new_seq = list(seq)
                if item not in new_seq:
                    new_seq.append(item)
                    temp.add(tuple(new_seq))
        ans = temp
    return ans

#outcome = set(["a", "b", "c", "d", "e", "f"])
#permutations = gen_permutations(outcome, 4)
#permutation_list = list(permutations)
#permutation_list.sort()
#print "Answer is", permutation_list[100]


#Question 3
def expected_value():
    '''
    fair four-sided die (with faces numbered 1-4) is rolled twice
    returns expected value of the product of the two die rolls
    '''
    states = gen_all_sequences((1, 2, 3, 4), 2)
    product = 0
    
    for item in states:
        product += item[0] * item[1]
    return product * 1.0 / len(states)

#print 'Expected value:', expected_value()

#Question 4
def ascnd_desc():
	'''
	what is the probability that this five-digit string consists of five
	consecutive digits in either ascending or descending order (e.g; "34567" or "43210")
	'''
	vals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	state = gen_all_sequences(vals, 5)
	count = 0

	for item in state:
		if all(earlier + 1 == later for earlier, later in zip(item, item[1:])):
			print item
			count += 1
	return count*2.0 /len(state)
print 'Question 4 Probability :', ascnd_desc()

#Question 5:
def permutations():
	'''
	what is the probability that this five-digit string consists of five
	consecutive digits in either ascending or descending order (e.g; "34567" or "43210")
	'''
	vals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	state = gen_permutations(vals,5)
	count = 0

	for item in state:
		if all(earlier + 1 == later for earlier, later in zip(item, item[1:])):
			print item
			count += 1
	return count*2.0 /len(state)
print 'Question 5 Probability :', permutations()


#Question 9
def cards_comb():
	'''
	what is the probability of being dealt a five card hand where all five cards are of the same suit?
	'''
	same_suit=4.0*math.factorial(13) / (math.factorial(13-5)*math.factorial(5))
	total_possibilities=math.factorial(52) / (math.factorial(52-5)*math.factorial(5))
	return same_suit / total_possibilities

#print "Cards combinations:", cards_comb()

def sequence_all():
	'''
	what is the probability that this five-digit string consists of five
	consecutive digits in either ascending or descending order (e.g; "34567" or "43210")
	'''
	possibilities = gen_all_sequences((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), 5)
	count = 0
    
	for item in possibilities:
		for element in item:
			if all(earlier + 1 == later for earlier, later in zip(item, item[1:])):
				count += 1
	# counter kept track of each element in item (thus 30 / 5), also must count
	# both ascending and descending sequences (thus 6 * 2)
	count /= len(item)
	return count * 2.0 / len(possibilities)

#print 'Question 4 answer:', sequence_all()

