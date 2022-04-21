import app

def test_calculate_estimate():
     """
     GIVEN a user enters a radius and height
     WHEN that radius and height is passed to this function
     THEN the total_estimate is accurately calculated
     """
     assert app.calculate_estimate(180,360) == "141,300.00"