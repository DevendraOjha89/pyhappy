import bankapp

def test_public_funds():
    assert "public" == bankapp.public_funds()