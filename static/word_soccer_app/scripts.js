// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function () {

    // Get elements
    const wordDiv = document.getElementById('word');
    const deleterDiv = document.getElementById('deleter');
    const removerDiv = document.getElementById('remover');
    const submitWord = document.getElementById('submit_word');

    let order_in_word;

    if (localStorage.getItem("order_in_word") !== null) {
        order_in_word = JSON.parse(localStorage.getItem("order_in_word")) || [];
    } else {
        order_in_word = new Array(11).fill(-1)
        localStorage.setItem("order_in_word", JSON.stringify(order_in_word));
    }

    // kliknutie na pismeno
    document.querySelectorAll('.let').forEach(one_letter => {
        one_letter.addEventListener('click', function () {
            if(one_letter.style.backgroundColor !== "red"){
                wordDiv.textContent += one_letter.textContent;
                one_letter.style.backgroundColor = "red";
                let order = one_letter.id.slice(1);
                order_in_word[Number(order)-1] = wordDiv.textContent.length-1;
            }
        });
    });

    // vymazanie 1 pismena
    deleterDiv.addEventListener('click', function () {
        const div = document.getElementById('word');
        let idx = order_in_word.indexOf(div.textContent.length-1);
        order_in_word[idx] = -1;
        document.getElementById('l'+ (idx+1).toString()).style.backgroundColor = "#359ec4";
        div.textContent = div.textContent.slice(0, -1);
    });

    // vymazanie celeho slova
    removerDiv.addEventListener('click', function () {
        document.getElementById('word').textContent = '';
        order_in_word.fill(-1);
        document.querySelectorAll('.let').forEach(one_letter => {
            one_letter.style.backgroundColor = "#359ec4";
         });

    });

    // aktualizacia premennej 'order_in_word' v localstorage
    localStorage.setItem("order_in_word", JSON.stringify(order_in_word));
});