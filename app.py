from markupsafe import escape
from flask import Flask, abort, render_template, request, url_for, flash, redirect
app = Flask(__name__)
import sqlite3
import os
app.secret_key = os.urandom(24).hex()

def get_db_connection():
	conn = sqlite3.connect('students.db')
	conn.row_factory = sqlite3.Row
	return conn

def get_post(post_id):
	conn = get_db_connection()
	post = conn.execute('SELECT * FROM students WHERE ID = ?', (post_id,)).fetchone()
	conn.close()
	if post is None:
		abort(404)
	return post

@app.route('/')
def homePage():
	conn = get_db_connection()
	students = conn.execute('SELECT * FROM students').fetchall()
	conn.close()
	
	return render_template('index.html', students=students)

@app.route('/create/', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		title = request.form['Student']
		content1 = request.form['ID']
		content2 = request.form['Score']
		if not title:
			flash('Student is required!')
		elif not content1:
			flash('ID is required!')
		elif not content2:
			flash('Score is required!')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)',
				(title, content1, content2))
			conn.commit()
			conn.close()
	return render_template('create.html')

@app.route('/<int:student>/edit/', methods=('GET', 'POST'))
def edit(student):
	post = get_post(student)
	if request.method == 'POST':
		title = request.form['Student']
		content1 = request.form['ID']
		content2 = request.form['Score']
		
		if not title:
			flash('Student is required!')
		elif not content1:
			flash('ID is required!')
		elif not content2:
			flash('Score is required!')
		else:
			conn = get_db_connection()
			conn.execute('UPDATE students SET Student = ?, ID = ?, Score = ?'
				'WHERE ID = ?', (title, content1, content2, student))
			conn.commit()
			conn.close()
	return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
	post = get_post(id)
	conn = get_db_connection()
	conn.execute('DELETE FROM students WHERE ID = ?', (id,))
	conn.commit()
	conn.close()
	return redirect('http://127.0.0.1:5000/')
