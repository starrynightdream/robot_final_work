$(() =>{
    const info = $('#info');
    $('#main1').on('click', (e)=>{
        // 调用main1
        $.post('/runPy',{
            pyFile: 'main1'
        }, (data)=>{
            info.text(data.stdout);
        });
    });
    $('#main2').on('click', (e)=>{
        // 调用main2
        $.post('/runPy',{
            pyFile: 'main2'
        }, (data)=>{
            info.text(data.stdout);
        });
    });
    $('#stop').on('click', (e)=>{
        // 调用stop
        $.post('/runPy',{
            pyFile: 'stop'
        }, (data)=>{
            info.text(data.stdout);
        });
    });
});