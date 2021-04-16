try:
    import torch
except ImportError:
    raise ImportError("Please install torch to use this module.")


class DebugDataset(torch.utils.data.Dataset):


    def __init__(self, dataset, size, replication=1) -> None:
        """
        Wrapper to subset any torch dataset so the potentially large dataset
        can seamlessly replaced for debugging purposes.

        Args:
            dataset (torch.utils.data.Dataset): the dataset to wrap
            size (int): size of the subset
            replication (int): how often to repeat the same data. Allows longer epochs.
                Reported dataset size: size * replication. Default: 1.
        """
        super().__init__()
        self.replication = replication
        self.size = size
        self.data = []

        assert size > 0
        if size == 1:
            raise Warning('Training on just one instance can cause issues when using batch normalization.')

        loader = torch.utils.data.DataLoader(dataset, batch_size=1, num_workers=4, collate_fn=lambda x: x)
        for i, b in enumerate(loader):
            if i < size:
                self.data.append(b[0])
            else:
                break
    

    def __len__(self):
        return len(self.data) * self.replication
    

    def __getitem__(self, index):
        return self.data[index % self.size]