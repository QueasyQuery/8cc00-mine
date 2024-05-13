from stringencoder import OneHotEncoder, LabelEncoder, BaseStringEncoder
import pytest
import numpy as np

class TestBaseExceptions:
    def test_matrix_shape(self):
        with pytest.raises(ValueError,match=r"Table length and matrix shape mismatch"):    
            _ = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [0, 0], [1, 1]]))
    
    def test_duplicate_chars(self):
        with pytest.raises(ValueError,match=r"Table has duplicate characters:.*"):    
            _ = BaseStringEncoder(table='abbc', mat=np.array([[1, 0], [0, 1], [1,1], [0, 0]]))
    
    def test_duplicate_rows(self):
        with pytest.raises(ValueError,match=r"Matrix has duplicate rows"):    
            _ = BaseStringEncoder(table='abcd', mat=np.array([[1, 0], [0, 1], [1,1], [1, 0]]))
    
    def test_no_exceptions_duplicate_rows(self):
        _ = BaseStringEncoder(table='abcd', mat=np.array([[1, 0], [0, 1], [1,1], [1, 0]]), force_unique_features=False)
    
class TestBaseAuxiliary:
    def test_duplicate_chars(self):
        encoder = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [1,1]]))
        assert encoder._find_duplicate_chars('abbc') == {'a': 1, 'b': 2, 'c': 1}

    def test_str_repr(self):
        encoder = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [1,1]]))
        assert str(encoder) == 'BaseStringEncoder{}' == repr(encoder)
    
    def test_str_repr_kwargs(self):
        encoder = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [1,1]]), extra_argument=False)
        assert str(encoder) == 'BaseStringEncoder{\'extra_argument\': False}' == repr(encoder)
    
    def test_eq(self):
        encoder1 = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [1,1]]))
        encoder2 = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [1,1]]))
        assert encoder1 == encoder2

    def test_eq_false(self):
        encoder1 = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [1,1]]))
        encoder2 = BaseStringEncoder(table='abc', mat=np.array([[1, 0], [0, 1], [0,0]]))
        assert encoder1 != encoder2

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
    
class TestEncodersAuxiliary:

    def test_str_repr_onehot(self):
        encoder = OneHotEncoder(table='abc')
        assert str(encoder) == 'OneHotEncoder{}' == repr(encoder)
    
    def test_str_repr_label(self):
        encoder = LabelEncoder(table='abc')
        assert str(encoder) == 'LabelEncoder{}' == repr(encoder)
