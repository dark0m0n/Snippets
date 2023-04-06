import requests

data = {
    'id': '3',
    'titel': 'ara_ara',
    'code': 'one_piece',
    'languege': 'Pug',
    'style': 'algol'    
}
response = requests.put("http://127.0.0.1:8000/snippet/4/", json=data)

print(response.content)
