from stringencoder import OneHotEncoder

if __name__ == "__main__":
    encoder = OneHotEncoder(table='helo')
    encoded = encoder.encode('hello')
    decoded = encoder.decode(encoded)
    assert decoded == 'hello'

    print("All tests passed!")