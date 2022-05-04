import server
import mock
def test_socketReceive():
    mock_socket = mock.Mock()
    mock_socket.recv.side_effect = ["5   ".encode(), "name".encode()]
    result = server.recvMsg(mock_socket)
    assert result == 'name'

def test_socketReceiveInvalid():
    mock_socket = mock.Mock()
    mock_socket.recv.side_effect = ["5   ", "name"]
    result = server.recvMsg(mock_socket)
    assert result == False
    
def test_socketReceiveInvalid2():
    mock_socket = mock.Mock()
    mock_socket.recv.side_effect = ["", "name"]
    result = server.recvMsg(mock_socket)
    assert result == False
def test_socketReceiveInvalid3():
    mock_socket = mock.Mock()
    mock_socket.recv.side_effect = ["5  "]
    result = server.recvMsg(mock_socket)
    assert result == False
