from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import app
from .models import db, FeedingRecord
from .forms import FeedingRecordForm
from datetime import datetime
from collections import defaultdict

app = Blueprint('app', __name__)

@app.route('/')
def index():
    records = FeedingRecord.query.all()
    # 初始化字典来存储每天的亲喂和瓶喂总量
    daily_totals = defaultdict(lambda: {'breast': 0, 'bottle': 0})
    for record in records:
        date_str = record.timestamp.strftime('%Y-%m-%d')
        if record.feeding_type == 'breast':
            daily_totals[date_str]['breast'] += record.amount
        else:
            daily_totals[date_str]['bottle'] += record.amount

    # 准备图表数据
    labels = sorted(daily_totals.keys())
    breast_data = [daily_totals[date]['breast'] for date in labels]
    bottle_data = [daily_totals[date]['bottle'] for date in labels]
    
    return render_template('index.html', records=records, labels=labels, breast_data=breast_data, bottle_data=bottle_data)

@app.route('/add', methods=['GET', 'POST'])
def add_record():
    form = FeedingRecordForm()
    unit = '分钟' if form.feeding_type.data == 'breast' else '毫升'
    if form.validate_on_submit():
        new_record = FeedingRecord(
            feeding_type=form.feeding_type.data,
            amount=form.amount.data,
            notes=form.notes.data,
            timestamp=datetime.now(),  # 设置为当前时间
            unit=unit
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
    daily_totals = defaultdict(lambda: {'breast': 0, 'bottle': 0, 'records': []})
    
    for record in records:
        date_str = record.timestamp.strftime('%Y-%m-%d')
        if record.feeding_type == 'breast':
            daily_totals[date_str]['breast'] += record.amount
        else:
            daily_totals[date_str]['bottle'] += record.amount
        daily_totals[date_str]['records'].append(record)
    
    return render_template('view_records.html', daily_totals=daily_totals)

@app.route('/delete/<int:record_id>', methods=['GET', 'POST'])
def delete_record(record_id):
    record = FeedingRecord.query.get_or_404(record_id)
    if request.method == 'POST':
        db.session.delete(record)
        db.session.commit()
        flash('记录删除成功！', 'success')
        return redirect(url_for('app.view_records'))
    return render_template('delete_record.html', record=record)