import pickle
import random
import numpy as np

try:
    import torch
    torch_available = True
except ImportError:
    torch_available = False


def save_checkpoint(savepath, use_torch=False, **kwargs):
    """
    Saves objects to a pickle. Pickles the state_dict of pytorch modules.
    Pickles also the state of random number generators for `random`, `numpy` and, if available, `torch`.

    For loading you can either use
    ```
    with open('path/to/checkpoint.pkl', 'rb') as f:
        checkpoint = pickle.load(f)
    ```
    or to make use of torch's `map_location` in distributed settings:
    ```
    map_location = {'cuda:%d' % 0: 'cuda:%d' % rank}
    checkpoint = torch.load('path/to/checkpoint.pkl, map_location)
    ```

    This loads the checkpoints into a dict. You can restore torch parameters using `load_state_dict`.
    To update the state of random number generators you can use

    ```
    torch.set_rng_state(checkpoint['torch_rng_state'])
    np.random.set_state(checkpoint['np_rng_state'])
    random.setstate(checkpoint['random_rng_state'])
    ```

    Args:
        savepath (str): path for the checkpoint file.
        use_torch (bool): Whether to use torch.save() or the pickle module.
        kwargs: objects to checkpoint, e.g. models, epoch, optimizers, ...
    """
    savedict = {}
    for k, v in kwargs.items():
        if hasattr(v, 'state_dict'):
            savedict[k] = v.state_dict()
        else:
            savedict[k] = v
    if torch_available:
        savedict['torch_rng_state'] = torch.get_rng_state()
    savedict['np_rng_state'] = np.random.get_state()
    savedict['random_rng_state'] = random.getstate()

    if use_torch and not torch_available:
        raise ValueError(f"Asked to use torch.save but torch is not installed.")

    if use_torch:
        torch.save(savedict, savepath)
    else:
        with open(savepath, 'wb') as f:
            pickle.dump(savedict, f)

