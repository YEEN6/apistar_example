from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
import json

user = [
	{'name' : 'A', 'age' : '20', 'gender' : 'man', 'address' : 'Seoul'},
	{'name' : 'B', 'age' : '25', 'gender' : 'woman', 'address' : 'Busan'},
	{'name' : 'C', 'age' : '23', 'gender' : 'woman', 'address' : 'Yongin'}
]


def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    #return {'message': 'Welcome to API Star, %s!' % name}
    myj = json.dumps(user, indent=4)
    if name is 'A':
        return user[0]
    if name is 'B':
        return user[1]
    if name is 'C':
        return user[2]
    
    return myj


routes = [
    Route('/', 'GET', welcome),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
