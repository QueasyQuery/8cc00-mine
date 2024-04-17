from stringencoder import OneHotEncoder, LabelEncoder

if __name__ == "__main__":
    encoder = OneHotEncoder(table='helo')
    encoded = encoder.encode('hello')
    decoded = encoder.decode(encoded)
    assert decoded == 'hello'

    encoder_2 = LabelEncoder(table='helo')
    encoded_2 = encoder_2.encode('hello')
    decoded_2 = encoder_2.decode(encoded_2)
    assert decoded_2 == 'hello'

    print("All tests passed!")