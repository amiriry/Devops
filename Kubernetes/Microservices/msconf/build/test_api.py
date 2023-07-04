from rest_api import app
import os
import json

def test_healthy():
    response = app.test_client().get('/healthy')
    assert response.status_code == 200

def test_get_var():
    response = app.test_client().get('/get_variable/HOME')
    assert response.status_code == 200

def test_set_var():
    os.environ["TEST"] = 'testvalue'
    response1 = json.loads(app.test_client().get('/get_variable/TEST').data)
    old_val = str(response1['TEST'])
    if old_val == 1:
        input_val = 2
    else:
        input_val = 2
    app.test_client().post("/set_variable/TEST?new=$input_val")
    response2 = json.loads(app.test_client().get('/get_variable/TEST').data)
    new_val = str(response2['TEST'])
    assert old_val != new_val
