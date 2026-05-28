// 引入Express框架，是Node.js流行的Web服务器框架
const express = require('express');

// 引入sqlite3模块，用于操作SQLite本地数据库
const sqlite3 = require('sqlite3').verbose();

// 引入body-parser用于处理请求体数据（json等）
const bodyParser = require('body-parser');

// 引入cors模块，允许前端跨域请求（前后端分离开发时必备）
const cors = require('cors');

const app = express();

// 使用CORS中间件，允许跨域访问
app.use(cors());

// 用于解析带Content-Type: application/json的POST请求体
app.use(bodyParser.json());

// 创建SQLite数据库文件（不存在时新建，存在则连接）
const db = new sqlite3.Database('./tickets.db');

// 初始化数据库表。如果表不存在则创建一个tickets表
db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT, // 工单唯一ID，自动递增
    name TEXT,                // 姓名字段，文本类型
    student_id TEXT,          // 学号，文本类型（不用number，兼容各种格式）
    repair_item TEXT,         // 维修项目描述
    estimate_time TEXT,       // 预计维修时间
    device_model TEXT,        // 电脑型号
    status TEXT               // 当前维修状态
  )`);
});

// 【接口1】新建工单。前端表单POST数据至此接口，数据写入数据库
app.post('/api/ticket', (req, res) => {
  // 解构前端请求体的各字段
  const { name, student_id, repair_item, estimate_time, device_model, status } = req.body;

  // 插入SQL语句，注意用?参数防止SQL注入
  db.run(
    `INSERT INTO tickets (name, student_id, repair_item, estimate_time, device_model, status) VALUES (?, ?, ?, ?, ?, ?)`,
    [name, student_id, repair_item, estimate_time, device_model, status],
    function(err) {
      if (err) return res.status(500).json({ error: err.message }); // 有错返回500和错误信息
      res.json({ id: this.lastID }); // 插入成功，返回刚插入工单的ID
    }
  );
});

// 【接口2】获取所有工单。前端GET请求拉取全部工单用于集中展示
app.get('/api/tickets', (req, res) => {
  db.all(`SELECT * FROM tickets`, [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows); // 返回所有工单对象数组
  });
});

// 【接口3】（可选）根据工单ID更新状态（目前只更新status字段）
app.put('/api/ticket/:id', (req, res) => {
  const { status } = req.body;
  db.run(
    `UPDATE tickets SET status = ? WHERE id = ?`,
    [status, req.params.id],
    function(err) {
      if (err) return res.status(500).json({ error: err.message });
      res.json({ changes: this.changes }); // 返回受影响行数
    }
  );
});

// 启动Express服务器，监听3001端口
app.listen(3001, () => {
  console.log('Server running at http://localhost:3001');
});