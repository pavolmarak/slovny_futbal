// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function () {

    // Get elements
    const targetDiv = document.getElementById('word');
    const deleterDiv = document.getElementById('deleter');
    const removerDiv = document.getElementById('remover');


    document.querySelectorAll('.let').forEach(element => {
        element.addEventListener('click', function () {
            targetDiv.textContent += element.textContent;
        });
    });


    deleterDiv.addEventListener('click', function () {
        const div = document.getElementById('word');
        div.textContent = div.textContent.slice(0, -1);
    });

    removerDiv.addEventListener('click', function () {
        document.getElementById('word').textContent = '';
    });


});