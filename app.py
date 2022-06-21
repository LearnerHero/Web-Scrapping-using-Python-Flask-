from flask import Flask,request,redirect,url_for,render_template
from bs4 import BeautifulSoup
import pip._vendor.requests

app=Flask(__name__)

@app.route('/')
def index():  
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def result():
    num=request.form.get('number')
    url="https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+num
    req=pip._vendor.requests.get(url)
    temp=BeautifulSoup(req.content,"html.parser")
    return render_template('result.html',temp=temp,num=num)
    
if __name__=='__main__':
    app.run()