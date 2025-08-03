import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

def test_shorten_url(client):
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert 'short_code' in data
    assert 'short_url' in data

def test_shorten_url_invalid(client):
    response = client.post('/api/shorten', json={"url": "invalid_url"})
    assert response.status_code == 400

def test_redirect_and_analytics(client):
    # Create short URL
    response = client.post('/api/shorten', json={"url": "https://example.com"})
    short_code = response.get_json()['short_code']

    # Redirect (should be 302)
    redirect_resp = client.get(f'/{short_code}')
    assert redirect_resp.status_code == 302

    # Check analytics
    analytics_resp = client.get(f'/api/analytics/{short_code}')
    data = analytics_resp.get_json()
    assert data['clicks'] == 1
