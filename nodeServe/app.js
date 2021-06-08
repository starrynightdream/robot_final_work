const path = require('path');
const cp = require('child_process');
const express = require('express');

const mutil = require('./util');

const port = 3000;
const main1FilePath = '../main.py';
const main2FilePath = '../test.py';
const stopFilePath = '../stop.py';

const ejs = require('ejs')


const app = express();
const threadObj = {};
const pythonFiles = {};


const init = async () =>{
    let files = await mutil.findAllFileLike('../', ['py']);
    for (let file of files){
        let fileN = file.split('\\');
        fileN = fileN[ fileN.length - 1];
        fileN = fileN.split('.')[0];
        pythonFiles[fileN] = file;
    }
}
init();

app.set('views', path.join(__dirname, '/view')); 
app.engine('html', ejs.renderFile);
app.set('view engine', 'html');

app.use(express.json());
app.use(express.urlencoded({
    extended: false
}));

app.use('/', express.static( path.join(__dirname, '/public/')))

app.post('/runPy', (req, res)=>{
    let key = req.body.pyFile.trim();
    console.log(key)
    let file = pythonFiles[key];

    // switch(key)
    // {
    //     case 'main1':
    //         file = main1FilePath;
    //         break;
    //     case 'main2':
    //         file = main2FilePath;
    //         break;
    //     case 'stop':
    //         file = stopFilePath;
    //         break;
    // }
    if (!file){
        res.json({
            stdout: 'no such file'
        });
        return;
    }
    
    
    // const command = `python ${ path.join(__dirname, file)}`;

    let pt = cp.spawn('python', [ path.join(__dirname, file)]);

    pt.stdout.on('data', (data) =>{
        console.log('stdout # ' , data);
    });

    pt.on('close', (code) =>{
        console.log(`thread ${key} close ${code}`);
    });
    
    pt.on('exit', (code) =>{
        console.log(`thread ${key} exit ${code}`);
        threadObj[key] = null;
    });

    threadObj[key] = pt;

    res.json({
        stdout: `run ${key}`
    });
});

app.post('/kill', (req, res) =>{
    let key = req.body.pyFile.trim();
    let file = pythonFiles[key];
    // switch(key)
    // {
    //     case 'main1':
    //         file = main1FilePath;
    //         break;
    //     case 'main2':
    //         file = main2FilePath;
    //         break;
    //     case 'stop':
    //         file = stopFilePath;
    //         break;

    // }
    if (!(file && threadObj[key])){
        res.json({
            stdout: 'no such thread'
        });
        return ;
    }
   
    threadObj[key].kill();
    threadObj[key] = null;

    res.json({
        stdout: 'kill success'
    });
});

app.use('/', async (req, res)=>{
    // 需要对文件夹内的python脚本做统计，而后再返回渲染的页面
    // res.render('index', {files: ['main1', 'main2', 'stop']});
    res.render('index', {files: Object.keys(pythonFiles)});
});

app.listen(port, ()=>{
    console.log(`run at ${port}`);
});