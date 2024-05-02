import numpy as np


class BaseStringEncoder:
    """
    Base class for string encoders.

    Parameters
    ----------
    table : str
        A string containing the unique characters that will be encoded.
    mat : np.array
        A matrix where each row corresponds to a character in table.
    force_unique_features : bool, default=True
        If True, mat should have unique rows.
    **kwargs
        Additional keyword arguments.
    """

    def __init__(self, table, mat, force_unique_features=True, **kwargs):

        # table should have the same amount of entries as the rows in mat
        if len(table) != mat.shape[0]:
            raise ValueError("Table length and matrix shape mismatch")

        # table should have unique characters
        if len(set(table)) != len(table):
            char_count = self._find_duplicate_chars(table)
            duplicates = [(char, count) for char, count in char_count.items() if count > 1]
            raise ValueError(
                "Table has duplicate characters:\n" + "\n".join(
                    [f"\t- {char}: {count}" for char, count in duplicates]
                    )
                )

        # mat should have unique rows if force_unique_features is True
        if force_unique_features and len(set([tuple(row) for row in mat])) != mat.shape[0]:
            raise ValueError("Matrix has duplicate rows")

        self._table = table
        self._mat = mat
        self._kwargs = kwargs

    def encode(self, string: str) -> np.array:
        """
        Encode a string into a numpy array.

        Args:
            string (str): The string to encode.
        Returns:
            np.array: Encoded string.
        """

        return np.array([self._mat[self._table.index(c)] for c in string])

    def decode(self, array: np.array) -> str:
        """
        Decode a numpy array into a string.

        Args:
            array (np.array): The array to decode.
        Returns:
            str: Decoded array.
        """
        
        return "".join([self._table[np.where(np.all(self._mat == row, axis=1))[0][0]] for row in array])
    
    @staticmethod
    def _find_duplicate_chars(x):
        result = {}
        for char in set(x):
            result[char]=x.count(char)
        return result

    def __str__(self):
        return self.__class__.__name__ + str(self._kwargs)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    