__author__ = 'Robert Navas'
__version__ = '1.0.0'


def absolute_error(true_function, approximation):

    return true_function - approximation


def relative_error(true_function, approximation):

    return true_function - approximation / true_function


if __name__ == '__main__':


    print(absolute_error(12.67, 11.472))