# tests/test_github_api.py
import pytest
from unittest.mock import patch
from handlers.pull_requests import get_pull_requests

@patch('handlers.pull_requests.requests.get')
def test_get_pull_requests_success(mock_get):
    # Mock response object
    mock_response = mock_get.return_value
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = [
        {'title': 'Fix bug', 'number': 1, 'html_url': 'http://example.com/pr/1'},
        {'title': 'Add feature', 'number': 2, 'html_url': 'http://example.com/pr/2'}
    ]

    prs = get_pull_requests('open')
    
    assert len(prs) == 2
    assert prs[0]['title'] == 'Fix bug'
    assert prs[1]['num'] == 2

@patch('handlers.pull_requests.requests.get')
def test_get_pull_requests_http_error(mock_get):
    mock_response = mock_get.return_value
    mock_response.raise_for_status.side_effect = Exception("HTTP Error")
    
    with pytest.raises(Exception, match="HTTP Error"):
        get_pull_requests('open')

