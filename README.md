# 婴儿喂养记录跟踪器

该项目是一个用于记录婴儿喂养数据的在线网页应用，支持亲喂和瓶喂记录。用户可以方便地添加、查看和删除喂养记录，并生成喂养曲线图。

## 功能

- **添加记录**：用户可以输入喂养时间、喂养方式（亲喂或瓶喂）和喂养量。
- **查看记录**：用户可以查看所有的喂养记录，并以图表形式展示喂养趋势。
- **删除记录**：用户可以选择删除特定的喂养记录。
- **数据存储**：所有记录存储在SQLite数据库中，确保数据的持久性。

## 技术栈

- **后端**：Flask
- **数据库**：SQLite
- **前端**：HTML, CSS, JavaScript

## 项目结构

```
feedrecord
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static
│   │   ├── css
│   │   │   └── styles.css
│   │   └── js
│   │       └── scripts.js
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── add_record.html
│   │   ├── view_records.html
│   │   └── delete_record.html
├── instance
│   └── baby_feeding_tracker.sqlite
├── .gitignore
├── config.py
├── requirements.txt
└── README.md
```

## 安装与运行

1. 克隆项目到本地：
   ```
   git clone <项目地址>
   cd feedrecord
   ```

2. 安装依赖：
   ```
   pip install -r requirements.txt
   ```

3. 运行应用：
   ```
   flask run
   ```

4. 打开浏览器，访问 `http://127.0.0.1:5000` 查看应用。
