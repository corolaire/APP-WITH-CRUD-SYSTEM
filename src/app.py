from flask import Flask , render_template,request,redirect,url_for #import flask library. this file is the view with endpoint of our app.
import os # to have access from directories,render_template is a modulo from flask
import database as db 

template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__))) #for config the root of the file
template_dir=os.path.join(template_dir,'src','templates')

#initialize la app
app=Flask(__name__,template_folder=template_dir)#to run app

#root of application 
@app.route('/')
def home(): #going to make a cursor to access to database
    cursor=db.database.cursor() #to connect database,cursor.execute--->indicas que vas a hacer una consulta
    cursor.execute("SELECT * FROM users") #---> consulta que te traiga todo de la tabla usuario con un select
    #we get the data from database in a structure
    myresult=cursor.fetchall() #data will be contain here like tuple
    #we convert this tuple into other structure
    insertobject=[] # we leave it empty(this will be filled with the data that the query gives me)
    columnnames=[column[0]for column in cursor.description] #me trae cada columna , y recorre con un for ,con description accedemos a los nombres de columnas
    for record in myresult: #x cada dato que contenga myresult
        insertobject.append(dict(zip(columnnames,record))) # for each column name its data
    cursor.close()
    return render_template('index.html',data=insertobject)

@app.route('/user',methods=['post']) #this endpoint will save  user in database
def add_user():
    username=request.form['username']   #form es xq es de un formulario,username es el campo que viene en la request
    name=request.form['name']
    password=request.form['password']
    
    if username and name and password: #if we have all this data in the request from client we can consult in database
        cursor=db.database.cursor() #remember: open connection with database 
        sql="INSERT INTO users (username,name,password)VALUES(%s,%s,%s)"
        #arriba se abre consulta del tipo insert , nombre tabla , campos con los valores
        data=(username,name,password)
        cursor.execute(sql,data)#la consulta la paso asi con los valores que contiene data q en definitiva son los necesarios
        db.database.commit()#se materializa la consulta
    return redirect(url_for('home') )#actualiza los datos de esta consulta

@app.route("/delete/<string:id>")#elimina registro a travez de su id
def delete(id):
    cursor=db.database.cursor()
    sql='DELETE FROM  users WHERE id=%s)'#la consulta es de borrado, me va a borrar si coincide el id q te pasan con id del dato
    data=(id)
    cursor.execute(sql,data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit /<string:id>',methods=['post'])#actualiza
def edit(id):
    username=request.form['username']   #form es xq es de un formulario,username es el campo que viene en la request
    name=request.form['name']
    password=request.form['password']
    cursor=db.database.cursor()
    sql='UPDATE FROM users SET username=%s ,name=%s , password=%s WHERE id=%s'
    data=(username,name,password,id)
    cursor.execute(sql,data)
    db.database.commit()
    return redirect(url_for('home'))    
    
    
        
    
    

 


if __name__=='__main__':#condition 
    app.run(debug=True,port=4000)#to run the app !!!!
    
    

 