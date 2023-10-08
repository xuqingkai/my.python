from bottle import route, run, template


from test1 import test11
from test2 import test211
from test import test4
from test.test5 import test55

@route('/')
def index():
    return '<b>Hello 123</b>!'
    
@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)
    
@route('/nihao/<name>')
def nihao(name):
    return template('<b>Nihao {{name}}</b>!', name=name)



@route('/test111')
def test1_test11_test111():
    test_value=test11.test111()
    return test_value
    
@route('/test112')
def test1_test11_test112():
    test_value=test11.test112()
    return test_value
    
@route('/test211')
def test2_test211():
    test_value=test221()
    return test_value

@route('/test441')
def test_test4_test441():
    test_value=test4.test441()
    return test_value


@route('/test551')
def test_test5_test55_test551():
    test_value=test55.test551()
    return test_value
    
run(host='0.0.0.0', port=8088)
