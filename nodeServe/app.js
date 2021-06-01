const path = require('path');
const cp = require('child_process');
const express = require('express');

const port = 3000;
const main1FilePath = '../test.py';
const main2FilePath = '../test.py';
const stopFilePath = '../test.py';

const app = express();

app.use(express.json());
app.use(express.urlencoded({
    extended: false
}));

app.use('/', express.static( path.join(__dirname, '/public/')))

app.post('/runPy', (req, res)=>{
    let key = req.body.pyFile.trim();
    let file = '';
    switch(key)
    {
        case 'main1':
            file = main1FilePath;
            break;
        case 'main2':
            file = main2FilePath;
            break;
        case 'stop':
            file = stopFilePath;
            break;
    }
    if (file)
        res.json({
            stdout: 'no such file'
        });
    
    let pyThread = cp.exec(`python ${ path.join(__dirname, file)}`, (err, stdout, stderr) =>{
        if (err){
            console.error(err);
            res.json({
                stdout: 'err'
            });
            return;
        }
        console.log('输出>');
        console.log(stdout);
        console.log('错误#');
        console.log(stderr);

        res.json({
            stdout
        });
    });

    pyThread.on('exit', (code) =>{
        // 可做退出处理
    });
});

app.use('/', (req, res)=>{
    res.sendFile( path.join(__dirname, '/view/index.html'));
});

app.listen(port, ()=>{
    console.log(`run at ${port}`);
});