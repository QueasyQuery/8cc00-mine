
from stringencoder import OneHotEncoder, LabelEncoder
import numpy as np

class TestEncoders:
    def test_onehot_encoder(self):
        encoder = OneHotEncoder(table='abc')
        encoded = encoder.encode('abc')
        assert np.all(encoded == np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    def test_onehot_decoder(self):
        encoder = OneHotEncoder(table='abc')
        encoded = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        decoded = encoder.decode(encoded)
        assert decoded == 'abc'
    
    def test_onehot_encoder_decoder(self):
        encoder = OneHotEncoder(table='abc')
        encoded = encoder.encode('abc')
        decoded = encoder.decode(encoded)
        assert decoded == 'abc'
    
    def test_label_encoder(self):
        encoder = LabelEncoder(table='abc')
        encoded = encoder.encode('abc')
        assert np.all(encoded == np.array([[0], [1], [2]]))
    
    def test_label_decoder(self):
        encoder = LabelEncoder(table='abc')
        encoded = np.array([0, 1, 2])
        decoded = encoder.decode(encoded)
        assert decoded == 'abc'
    
    def test_label_encoder_decoder(self):
        encoder = LabelEncoder(table='abc')
        encoded = encoder.encode('abc')
        decoded = encoder.decode(encoded)
        assert decoded == 'abc'