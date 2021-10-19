import src.logic as src

def test_logic(mocker):
    
    mocker.patch('os.path.isfile', side_effect=Exception)
    assert src.calcuration('add',2,5) == 7

