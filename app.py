from bottle import route, run, template

from test import test0
from test1 import test11
from test2 import test21
from test.test4 import test4

@route('/')
def index():
    return '<b>Hello 123</b>!'
    
@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)
    
@route('/nihao/<name>')
def nihao(name):
    return template('<b>Nihao {{name}}</b>!', name=name)

@route('/test0')
def test_test0_test00_test000():
    test_value=test0.test000()
    return test_value

@route('/test1')
def test1_test11_test111():
    test_value=test11.test111()
    return test_value
    
@route('/test12')
def test1_test11_test112():
    test_value=test11.test112()
    return test_value
    
@route('/test2')
def test2_test21():
    test_value=test21()
    return test_value

@route('/test4')
def test_test4_test44_test441():
    test_value=test4.test441()
    return test_value
    
run(host='0.0.0.0', port=8088)
