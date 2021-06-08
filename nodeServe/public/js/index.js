$(() =>{
    const info = $('#info');

    $('.runBut').on('click', (e) =>{
        console.log('run', e.target.name);

        $.post('/runPy', {
            pyFile: e.target.name
        }, (data) =>{
            info.text(data.stdout);
        });
    });

    $('.killBut').on('click', (e) =>{

        $.post('/kill', {
            pyFile: e.target.name
        }, (data) =>{
            info.text(data.stdout);
        });
    });
});