"""
single neuron network


       O -output node
       | -weight
       O -input node

input_node * weight = output_node
"""
import numpy as np
training_rate = .1 #tells how fast the network can train too fast and it is usually less accurate, too slow and it takes too long to train the network
inputNode = .5 #creates the input node of the network
weight = .5 #creates the weight connecting the input node and the output node
outputNode = 0 #creates the output node of the network
expectedOutput = 1 #tells the network what output we want from it
for i in range(10): #training loops, lets the network run multiple times to improve its accuracy
    for j in range(100):
        outputNode = inputNode*weight #Computes the output node by multiplying the input by the weight
        loss = outputNode-expectedOutput #the loss function, determines how well or how poorly the network is performing
        weight = weight-loss*inputNode*training_rate #Weights are adjusted to lower the loss
    outputNode = inputNode*weight #computes the output of the network
    print("weight: ",weight) #shows how the weight has been changed
    print("output: ",outputNode) #shows how the output is coming closer to the expected output
    print("loss: ",loss) #shows how the loss decreases over time