ML - MNIST K-NN classification
-----------------------

Using the [MNIST](https://en.wikipedia.org/wiki/MNIST_database) subset provided by scikit-learn library.

MNIST is a computer vision dataset that consists of handwritten digits and labels for each image (which tells which digit it is)

k-NN classifier will be applied to the image dataset in order to recognize handwritten digits from the MNIST subset.


Understanding
-----------------------

75% of the dataset will be training and the rest testing;

10% of the training data will be allocated to validation, while the remaining 90% will remain as training data

*Accuracy* will show the most efficient k to be used.

*Evaluation on testing data* evaluates the performance of the model

Note that the number of neighbors cannot be bigger than the number of observations in the training data set

Installation
----------------------

* Clone this repo to your computer.
* Get into the folder using `cd Recognizing-handwritten-digits-KNN`.


Usage
----------------------
### Run
* `python MNIST_KNN_python.py`
