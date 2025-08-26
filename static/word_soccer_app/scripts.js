// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function () {

    // Get elements
    const wordDiv = document.getElementById('word');
    const deleterDiv = document.getElementById('deleter');
    const removerDiv = document.getElementById('remover');
    const submitWord = document.getElementById('submit_word');


    document.querySelectorAll('.let').forEach(one_letter => {
        one_letter.addEventListener('click', function () {
            if(one_letter.style.backgroundColor !== "red"){
                wordDiv.textContent += one_letter.textContent;
                one_letter.style.backgroundColor = "red";
            }
        });
    });


    deleterDiv.addEventListener('click', function () {
        const div = document.getElementById('word');
        div.textContent = div.textContent.slice(0, -1);
    });

    removerDiv.addEventListener('click', function () {
        document.getElementById('word').textContent = '';

        document.querySelectorAll('.let').forEach(one_letter => {
            one_letter.style.backgroundColor = "#359ec4";
         });
    });

    submitWord.addEventListener('click', function () {
        const word = document.getElementById('word');

    });


});