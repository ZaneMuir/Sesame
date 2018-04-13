import SpikeUnit
import numpy as np

def gaussian_kernel(sigma):
    return lambda tau: np.sum(1/(sigma*np.sqrt(2*np.pi))*np.exp(-tau**2/(2*sigma**2)))

def causal_kernel(alpha):
    return lambda tau: np.sum([i for i in (alpha**2) * tau * np.exp(- alpha * tau) if i > 0])

def kernel(name, **args):
    if name == "gaussian":
        return gaussian_kernel(**args)
    elif name == "causal":
        return causal_kernel(**args)
    else:
        raise NameError("unkown kernel: "+str(name))

def check_and_convert_to_ndarray(subject):
    if isinstance(subject,SpikeUnit.SpikeUnit):
        target = subject.spike_train
    elif isinstance(subject,list):
        target = np.array(subject)
    elif isinstance(subject, np.array):
        target = subject
    else:
        raise ValueError("type of to is not supported: "+str(type(to)))
    return target


def generate_linear_filter(to, kernel):
    target = check_and_convert_to_ndarray(to)
    return lambda t: kernel(target - t)


def apply_linear_filter(to, kernel, x_range=None, step=10000):
    target = check_and_convert_to_ndarray(to)
    linear_filter = generate_linear_filter(to, kernel)

    if x_range == None:
        x_range = np.linspace(0, target[-1], step)
    return x_range, np.array(list(map(linear_filter, x_range)))
