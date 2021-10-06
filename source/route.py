from flask import (
    redirect,
    request,
    session,
    render_template,
    url_for,
    Blueprint,
)

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        return redirect(url_for('.chat'))
    return render_template('home.html')

@main.route('/join_room', methods=['GET', 'POST'])
def join_room():
    name = request.form['user_name']
    key = request.form['room_key']
    if not name:
        error = "A username must be provided."
        return render_template('home.html', join_err=error)
    if not key:
        error = "A room key must be provided."
        return render_template('home.html', join_err=error)
    return render_template(chat.html)
    # Not yet implementing user persistence on re-entry
    #session['user_name'] = name

@main.route('/make_room', methods=['GET', 'POST'])
def make_room():
    name = request.form['user_name']
    room = request.form['room_name']
    cap = request.form['capacity']
    note = request.form['note']
    if not name:
        error = "A username must be provided."
        return render_template('home.html', make_err=error)
    return render_template(chat.html)
    # Not yet implementing user persistence on re-entry
    #session['user_name'] = name

@main.route('/chat')
def chat():
    name = session.get('user_name', None)
    if not name:
        return redirect('/')
    return render_template('chat.html')


@main.route('/canvas')
def canvas():
    return render_template('canvas.html')



