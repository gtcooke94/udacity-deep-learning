""" Lesson 8.11 NumPy Quiz """
# Use the numpy library
import numpy as np


def prepare_inputs(inputs):
    # TODO: create a 2-dimensional ndarray from the given 1-dimensional list;
    #       assign it to input_array
    input_array = np.array([inputs])

    # TODO: find the minimum value in input_array and subtract that
    #       value from all the elements of input_array. Store the
    #       result in inputs_minus_min
    inputs_minus_min = input_array - np.min(input_array)

    # TODO: find the maximum value in inputs_minus_min and divide
    #       all of the values in inputs_minus_min by the maximum value.
    #       Store the results in inputs_div_max.
    inputs_div_max = inputs_minus_min / np.max(inputs_minus_min)

    # return the three arrays we've created
    return input_array, inputs_minus_min, inputs_div_max


def multiply_inputs(m1, m2):
    # TODO: Check the shapes of the matrices m1 and m2.
    #       m1 and m2 will be ndarray objects.
    #
    #       Return False if the shapes cannot be used for matrix
    #       multiplication. You may not use a transpose
    if m1.shape[1] == m2.shape[0]:
        return m1.dot(m2)
    elif m2.shape[1] == m1.shape[0]:
        return m2.dot(m1)
    else:
        return False


def find_mean(values):
    # TODO: Return the average of the values in the given Python list
    return np.array(values).mean()


def test_prepare_inputs():
    input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1, 2, 7])
    assert input_array.shape == (1, 3)
    assert (inputs_minus_min == np.array([[0, 3, 8]])).all()
    assert (inputs_div_max == np.array([[0, 3 / 8, 1]])).all()


def test_multiply_inputs():
    assert not multiply_inputs(
        np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1], [2], [3], [4]])
    )
    assert (
        multiply_inputs(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1], [2], [3]]))
        == np.array([[14], [32]])
    ).all()
    assert (
        multiply_inputs(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1, 2]]))
        == np.array([9, 12, 15])
    ).all()


def test_find_mean():
    return find_mean([1, 3, 4]) == 8 / 3


input_array, inputs_minus_min, inputs_div_max = prepare_inputs([-1, 2, 7])
print("Input as Array: {}".format(input_array))
print("Input minus min: {}".format(inputs_minus_min))
print("Input  Array: {}".format(inputs_div_max))

print(
    "Multiply 1:\n{}".format(
        multiply_inputs(
            np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1], [2], [3], [4]])
        )
    )
)
print(
    "Multiply 2:\n{}".format(
        multiply_inputs(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1], [2], [3]]))
    )
)
print(
    "Multiply 3:\n{}".format(
        multiply_inputs(np.array([[1, 2, 3], [4, 5, 6]]), np.array([[1, 2]]))
    )
)

print("Mean == {}".format(find_mean([1, 3, 4])))
