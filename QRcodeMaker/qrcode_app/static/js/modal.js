const modalColor = document.querySelectorAll('#modal-color-button')
const modalWindowColor = document.querySelector('.modal-window-color')
const bodyOpacity = document.querySelector('.main-input')
const headerOpacity = document.querySelector('header')


for (let button = 0; button < modalColor.length; button++){
    modalColor[button].addEventListener("click", () =>{
        modalWindowColor.style.display = "flex"
        bodyOpacity.style.opacity = '0.5'
        headerOpacity.style.opacity = '0.5'
    })
}

const modalLogo = document.querySelectorAll('#modal-logo-button')
const modalWindowLogo = document.querySelector('.modal-window-logo')

for (let button = 0; button < modalLogo.length; button++){
    modalLogo[button].addEventListener("click", () =>{
        modalWindowLogo.style.display = "flex"
        bodyOpacity.style.opacity = '0.5'
        headerOpacity.style.opacity = '0.5'
    })
}

const modalDesign = document.querySelectorAll('#modal-design-button')
const modalWindowDesign = document.querySelector('.modal-window-design')

for (let button = 0; button < modalDesign.length; button++){
    modalDesign[button].addEventListener("click", () =>{
        modalWindowDesign.style.display = "flex"
        bodyOpacity.style.opacity = '0.5'
        headerOpacity.style.opacity = '0.5'
    })
}