// При нажатии на кнопку скачать
document.querySelector('.download-button').addEventListener('click', function() {
    var modal = document.getElementById('download-modal');
    modal.classList.add('download-modal-open'); // Добавляем класс modal-open к элементу
});

document.querySelector('.download-button2').addEventListener('click', function() {
    var modal = document.getElementById('download-modal');
    modal.classList.add('download-modal-open'); // Добавляем класс modal-open к элементу
});

document.querySelector('.download-button3').addEventListener('click', function() {
    var modal = document.getElementById('download-modal');
    modal.classList.add('download-modal-open'); // Добавляем класс modal-open к элементу
});

// При нажатии на кнопку закрыть
document.querySelector('.close-download-button').addEventListener('click', function() {
    var modal = document.getElementById('download-modal');
    modal.classList.remove('download-modal-open'); // Удаляем класс modal-open у элемента
});

document.querySelector('.close-download-button2').addEventListener('click', function() {
    var modal = document.getElementById('download-modal');
    modal.classList.remove('download-modal-open'); // Удаляем класс modal-open у элемента
});
