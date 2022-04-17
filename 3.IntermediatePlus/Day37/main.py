import requests
import datetime as dt

USERNAME = "vincenzo"
TOKEN = "tokentokentoken"
GRAPH_ID = "graph1"
current_date = dt.datetime.now().strftime("%Y%m%d")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
PIXEL_PUT_DELETE_ENDPOINT = f"{PIXEL_ENDPOINT}/{current_date}"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Python Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "kuro",
}

pixel_body = {
    "date": current_date,
    "quantity": "200",
}

pixel_update_body = {
    "quantity": "10000",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create User
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# Create Graph
# response_graph = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response_graph.text)

# Create Pixel
# response_pixel = requests.post(url=PIXEL_ENDPOINT, json=pixel_body, headers=headers)
# print(response_pixel.text)
# Update Pixel
# response_pixel_put_delete = requests.put(url=PIXEL_PUT_DELETE_ENDPOINT, json=pixel_update_body, headers=headers)
# print(response_pixel_put_delete.text)
# Delete Pixel
# response_pixel_put_delete = requests.delete(url=PIXEL_PUT_DELETE_ENDPOINT, headers=headers)
# print(response_pixel_put_delete.text)
