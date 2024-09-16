from fastapi.testclient import TestClient
from main import app 
from requests import HTTPError, Response

client = TestClient(app)


def test_fetch_top_stories_success(): 
    response = client.get("/")
    assert response.status_code == 200 
    stories = response.json() 
    assert len(stories) == 10 
    assert all("title" in story for story in stories)
    assert all("url" in story for story in stories)
    assert all("author" in story for story in stories)
    assert all("score" in story for story in stories)
    assert all("time" in story for story in stories)

def test_fetch_top_stories_failure(mocker): 
    mock_get = mocker.patch('requests.get', side_effect=HTTPError("Hackernews API might be down or unreachable."))
    response = client.get("/")
    assert response.status_code == 503 
    assert response.json() == {'detail': 'Hackernews API might be down or unreachable.'}
    mock_get.assert_called_once()

def test_invalid_endpoint():
    response = client.get("/stories")
    assert response.status_code == 404 

def test_empty_response(mocker): 
    mock_get = mocker.patch('requests.get')
    mock_get.side_effect=[Response()]
    mock_get.return_value.status_code = 200 
    mock_get.return_value._content = b'[]'