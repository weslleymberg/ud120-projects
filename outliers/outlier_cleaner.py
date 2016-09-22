#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    grouped_data = zip(ages, net_worths, predictions)

    calculated_error = [(age, net_worth, (net_worth-prediction)**2) for age, net_worth, prediction in grouped_data]

    calculated_error.sort(key=lambda (x,y,error): error)

    cleaned_data = calculated_error[:int(len(calculated_error)*0.9)]
    print len(cleaned_data)

    return cleaned_data

