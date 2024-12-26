from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import app
from .models import db, FeedingRecord
from .forms import FeedingRecordForm

app = Blueprint('app', __name__)

@app.route('/')
def index():
    records = FeedingRecord.query.all()
    return render_template('templates/index.html', records=records)

@app.route('/add', methods=['GET', 'POST'])
def add_record():
    form = FeedingRecordForm()
    if form.validate_on_submit():
        new_record = FeedingRecord(
            feeding_type=form.feeding_type.data,
            amount=form.amount.data,
            date=form.date.data
        )
        db.session.add(new_record)
        db.session.commit()
        flash('记录添加成功！', 'success')
        return redirect(url_for('app.index'))
    return render_template('add_record.html', form=form)

@app.route('/view')
def view_records():
    records = FeedingRecord.query.all()
    return render_template('view_records.html', records=records)

@app.route('/delete/<int:record_id>', methods=['GET', 'POST'])
def delete_record(record_id):
    record = FeedingRecord.query.get_or_404(record_id)
    if request.method == 'POST':
        db.session.delete(record)
        db.session.commit()
        flash('记录删除成功！', 'success')
        return redirect(url_for('app.view_records'))
    return render_template('delete_record.html', record=record)