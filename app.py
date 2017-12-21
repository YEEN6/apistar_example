from apistar import Include, Route
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
import json
import jwt
import logging


#show the log
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(message)s',
    filename='./apistar.log',
    level=logging.INFO
)


data = {
    'user_a' : {'pw' : '1111', 'info' : { 'age' : '20', 'gender' : 'man', 'address' : 'Seoul'}},
    'user_b' : {'pw' : '2222', 'info' : {'age' : '25', 'gender' : 'woman', 'address' : 'Busan'}},
    'user_c' : {'pw' : '3333', 'info' : {'age' : '23', 'gender' : 'woman', 'address' : 'Yongin'}}
}


def Auth(id, pw):
    if data[id]['pw'] == pw:
        return True
    else:
        return False

def encode(id):
    logging.info(data[id]['info'])
    return jwt.encode(data[id]['info'],'something', algorithm='HS256')

def welcome(id=None, pw=None):
    if id is None:
        return {'message' : 'input your id'}
    elif Auth(id, pw) == True:
        return {'message' : 'Why I cannot do this'}
    else:
        jwt = encode(id)
        logging.info(jwt)
        return jwt  

routes = [
    Route('/', 'GET', welcome),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(routes=routes)


if __name__ == '__main__':
    app.main()
