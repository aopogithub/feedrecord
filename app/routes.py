from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import app
from .models import db, FeedingRecord
from .forms import FeedingRecordForm

app = Blueprint('app', __name__)

@app.route('/')
def index():
    records = FeedingRecord.query.all()
    labels = [record.timestamp.strftime('%Y-%m-%d %H:%M:%S') for record in records]
    data = [record.amount for record in records]
    return render_template('index.html', records=records, labels=labels, data=data)

@app.route('/add', methods=['GET', 'POST'])
def add_record():
    form = FeedingRecordForm()
    if form.validate_on_submit():
        new_record = FeedingRecord(
            feeding_type=form.feeding_type.data,
            amount=form.amount.data,
            notes=form.notes.data,
            timestamp=datetime.now()  # 设置为当前时间
        )
        db.session.add(new_record)
        db.session.commit()
        flash('记录添加成功！', 'success')
        print(f"Added record: {new_record}")  # 调试信息
        return redirect(url_for('app.index'))
    else:
        print("Form validation failed")  # 调试信息
        print(form.errors)  # 打印表单错误信息
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