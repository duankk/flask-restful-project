# flask-restful-project
storage flask restful project

window:
  set FALSK_APP = restdemo:create_app()
  flask run
  
database:
  flask db init
  flask db migrate
  flask db upgrade
  
connect mysql information:
  SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/oms?charset=utf8'
