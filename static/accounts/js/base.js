let number = 0,
body = document.querySelector('body')

document.querySelector('.BG-btn').addEventListener('click', function() {
changeBG();
})

function changeBG() {
if (number == 0) {
    body.style.backgroundImage = 'var(--colorful)';
    number = number +1;
}

else if (number == 1) {
    body.style.backgroundImage = 'var(--colorful2)';
    number = number +1;
}

else if (number == 2) {
    body.style.backgroundImage = 'var(--rainbow)';
    // body.style.animation = 'PastelRainbow 6s infinite alternate';
    number = number +1;
}

else if (number == 3) {
    body.style.backgroundImage = 'var(--default)';
    // body.style.animation = 'PastelRainbow 4s infinite alternate';
    number = number -3;
}
}