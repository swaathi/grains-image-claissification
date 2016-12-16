#!/usr/bin/env python
"""

Brain class.

"""

import os
import sys
from sys import argv
import pickle

# PyBrain imports
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain import TanhLayer

# Local imports
import image_operations as io

class Brain:
  """

  Constructor.
  Input: hidden_nodes - number of hidden nodes used in the neuralnetwork

  """
  def __init__(self, hidden_nodes = 30):
    """
    parameters to buildNetwork are inputs, hidden layers, output
    bias = true allows for a bias unit to be added in each neural net layer
    hiddenclass represents the method used by the hidden layer
    """
    self.classifier_neural_net = buildNetwork(12, hidden_nodes, 1, bias=True, hiddenclass=TanhLayer)
    # Initializing dataset for supervised regression training
    self.data_sets = SupervisedDataSet(12, 1)
    # classification_trainer uses backpropagation supervised training method for training the newural network
    self.classification_trainer = BackpropTrainer(self.classifier_neural_net, self.data_sets)

  """
  Method to add a sample image to the datasets for training the classifier
  """
  def add_image_to_train(self, image_file, group_id):
    tto = io.twelve_tone(image_file)
    print(tto)
    self.data_sets.addSample(tto, (group_id,))

  def train(self):
    #classification_trainer.trainUntilConvergence()
    #this will take forever (possibly literally in the pathological case)
    # for i in range(0, 30):
    #   self.classification_trainer.train()
    self.classification_trainer.trainUntilConvergence()

  def save(self, file_name="classifier.brain"):
    with open(file_name, 'wb') as file_pointer:
      pickle.dump(self.classifier_neural_net, file_pointer)

  def load(self, file_name="classifier.brain"):
    with open(file_name, 'rb') as file_pointer:
      self.classifier_neural_net = pickle.load(file_pointer)

  def classify(self, image_file):
    score = self.classifier_neural_net.activate(io.twelve_tone(image_file))
    print(score)

    if score < 1.5:
      return "chick-peas"
    else:
      return "green-peas"
