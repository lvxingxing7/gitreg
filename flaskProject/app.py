from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data_dir = {
    1: {'name': '卢达峰', 'lang': '18cm'},
    2: {'name': '陈桂涛', 'lang': '30cm'}
}


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('name')
    pwd = request.form.get('pwd')
    if user == 'yc' and pwd == 'yc':
        return redirect('/index')
    error = '请爬'
    return render_template('login.html', error=error)


@app.route('/index', endpoint='master')
def index():
    data = data_dir
    return render_template('index.html', data=data)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'GET':
        return render_template('edit.html')
    nid = int(request.form.get('nid'))
    new_name = request.form.get('name')
    new_lang = request.form.get('lang')
    data_dir[nid]['name'] = new_name
    data_dir[nid]['lang'] = new_lang
    return redirect(url_for('master'))


@app.route('/delete/<int:nid>')
def delete(nid):
    del data_dir[nid]
    return redirect(url_for('master'))


if __name__ == '__main__':
    app.run()





