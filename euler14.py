longestIterationSequence = 0
longestIterationSequenceNumber = 0

def collatzSequence(number):
	iteration = number 
	sequenceLength = 1
	while iteration != 1: #if even, divide in half and continue, if odd, multiply by 3, then add 1, then continue.
		if iteration % 2 == 0:
			iteration /= 2
			sequenceLength += 1
			continue
		if iteration % 2 != 0:
			iteration = (iteration * 3)+1
			sequenceLength += 1
			continue
	return sequenceLength

for number in range(1,1000000):
	iterationSequenceLength = collatzSequence(number)
	if iterationSequenceLength > longestIterationSequence: #if longer sequence is found, print new sequence and corresponding number
		longestIterationSequence = iterationSequenceLength
		longestIterationSequenceNumber = number
	print("Number: %s \t Collatz sequence length: %s \t Highest sequence: %s from number %s" % (number, iterationSequenceLength, longestIterationSequence,longestIterationSequenceNumber))

print("Longest collatz sequence is %s from number %s" % (longestIterationSequence,longestIterationSequenceNumber))
