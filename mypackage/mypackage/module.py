import numpy as np
import matplotlib.pyplot as plt


def foo(t, amplitude, period):
    """
    y = foo(t, amplitude, period)
    generate a sinusoid given an amplitude and period.

    """
    y = amplitude * np.sin(2 * np.pi * t / period)
    return y


class MyClass():
    """
    class that can generate a sinusoid given an amplitude and period.

    """

    def __init__(self, amplitude, period):
        self.amplitude = amplitude
        self.period = period

    def foo(self, t):
        """
        method that returns a sinusoid for a given array t
        """
        return self.amplitude * np.sin(2 * np.pi * t / self.period)


def myplot(t, y):
    """
    helper function to plot funciton with labels
    """
    plt.plot(t, y)
    plt.ylabel('y(t)')
    plt.xlabel('t=time (seconds)')


test_obj = MyClass(amplitude=1, period=0.2)
