from apistar import Include, Route, annotate, render_template, Response, http
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.renderers import HTMLRenderer
import json
import jwt
import logging


#show the log
logging.basicConfig(
	format='%(asctime)s [%(levelname)s] %(message)s',
	filename='./apistar.log',
	level=logging.INFO
)

#set static datas
data = {
	'user_a' : {'pw' : '1111', 'info' : {'id' : 'user_a', 'age' : '20', 'gender' : 'man', 'address' : 'Seoul'}},
	'user_b' : {'pw' : '2222', 'info' : {'id' : 'user_b', 'age' : '25', 'gender' : 'woman', 'address' : 'Busan'}},
	'user_c' : {'pw' : '3333', 'info' : {'id' : 'user_c', 'age' : '23', 'gender' : 'woman', 'address' : 'Yongin'}}
}


def auth(id, pw):
	if data[id]['pw'] == pw:
		return True
	else:
		return False

def encode(id):
	logging.info(data[id]['info'])
	return jwt.encode(data[id]['info'],'something', algorithm='HS256')

def get_info(token):
	#if not(type(token) == string):
	#	return Error
	info = jwt.decode(token, 'something', algorithms=['HS256'])
	return info

@annotate(renderers=[HTMLRenderer()])

def login(username: str):
	return render_template('index.html', username=username)

@annotate(renderers=[HTMLRenderer()])

def login_info(id=None, pw=None):
	logging.info('hi')
	logging.info('%s,%s'%(id,pw))
	jwt_data = encode(id)
	logging.info(jwt_data)
	return render_template('login_info2.html', jwt=jwt_data.decode('utf-8'))
	#return render_template('login_info.html')

def welcome(id=None, pw=None):
	if id is None:
		return {'message' : 'input your id'}
	elif auth(id, pw) == True:
		jwt = encode(id)
		logging.info(jwt)
		return jwt.decode("utf-8")
	else:
		return 'Login Fail'

def auth_jwt(token=None):
	if token is None:
		return 'Error' 
	else:
		return get_info(token) 

@annotate(renderers=[HTMLRenderer()])

def user_info(jwt_data=None):
	logging.info("jwt : %s"%jwt_data)
	info = jwt.decode(str.encode(jwt_data), 'something', algorithms=['HS256'])
	logging.info(info)
	return render_template('login_info2.html', user_info=json.dumps(info))

routes = [
	Route('/', 'GET', welcome),
	Route('/login', 'GET', login),
	Route('/login_info', 'GET', login_info),
	Route('/user_info' , 'GET', user_info),
	Route('/jwt', 'GET', auth_jwt),
	Include('/docs', docs_urls),
	Include('/static', static_urls)
]

settings = {
	'TEMPLATES': {
		'ROOT_DIR': 'templates',	# include the 'tmeplates/'directory.
		'PACKAGE_DIRS': ['apistar']	# include the built-in apistar templates.
		}
	}


app = App(routes=routes, settings=settings)


if __name__ == '__main__':
	app.main()
