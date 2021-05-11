import pickle
import unittest

from rtb import save_checkpoint

"""
Prerequisits
"""

import torch

class Model(torch.nn.Module):

    def __init__(self) -> None:
        super().__init__()
        self.linear1 = torch.nn.Linear(100, 1)
        self.relu = torch.nn.ReLU()
    

    def forward(self, x):
        return self.relu(self.linear1(x))


model = Model()
input = torch.ones(1, 100)

path = "/tmp/checkpoint.pkl"

class TestCheckpointing(unittest.TestCase):

    def test_load_pickle(self):
        result_before = model(input).item()
        save_checkpoint(path, use_torch=False, model=model, e=1)

        torch.nn.init.uniform_(model.linear1.weight)

        with open(path, 'rb') as f:
            checkpoint = pickle.load(f)

        model.load_state_dict(checkpoint['model'])
        
        self.assertEqual(model(input).item(), result_before)
        self.assertEqual(checkpoint['e'], 1)


    def test_load_torch(self):
        result_before = model(input).item()
        save_checkpoint(path, True, model=model, e=5)

        torch.nn.init.uniform_(model.linear1.weight)

        checkpoint = torch.load(path)

        model.load_state_dict(checkpoint['model'])
        
        self.assertEqual(model(input).item(), result_before)
        self.assertEqual(checkpoint['e'], 5)


if __name__ == '__main__':
    unittest.main()