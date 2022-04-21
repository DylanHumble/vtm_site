def test_index_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200
        assert b"Welcome to VTM!" in res.data
        assert b"Vertical Tank Maintenance" in res.data

def test_about_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200
        assert b"About VTM" in res.data
        assert b"About Vertical Tank Maintenance" in res.data

def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (GET)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 302


def test_estimate_route(app, client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' route is requested (POST)
    THEN check that the response is valid
    """
    with app.test_client() as test_client:
        total_estimate = {"radius":"180", "height":"360"}
        res = test_client.get('/estimate', data=total_estimate)
        assert res.status_code == 200
