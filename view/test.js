var express = require('express');
var app = express();

var py_shell = require('python-shell');
var py_options = {
    mode : 'text',
    pythonPath : '',
    pythonOptions : ['-u'],
    scriptPath: '' // py 파일 경로, nodejs 파일과 경로 같아서 생략
};

app.use( function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:5500');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, content-type');
    res.setHeader('Access-Control-Allow-Credentials', true);
    // CORS 허용을 위한 헤더 설정들
    next();
    // 비동기 처리 때문에 넣는것, 위 setHeader들이 다 설정된 후에 요청을 받음
});

app.listen(8080, function() {
    'use strict';
    console.log('server running on port 8080');
});

app.get('/', function (req, res) {
    py_shell.run('sample.py', py_options, function(err, results) {
        if (err) throw err;
        res.json(results);
    });
});