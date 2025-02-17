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
        modalWindowLogo.hidden = false
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

const hiddenColorMain = document.querySelector('#colorInputMain')
const hiddenColorBg = document.querySelector('#colorInputBg')
const colorInputQr = document.querySelector('#colorInputOne')
const colorInputBgQr = document.querySelector('#colorInputTwo')

const buttonColorQr = document.querySelector('#buttonColorQR')


buttonColorQr.addEventListener('click', ()=>{
    hiddenColorMain.value = colorInputQr.value
    hiddenColorBg.value = colorInputBgQr.value
    modalWindowColor.style.display = "none"
    bodyOpacity.style.opacity = '1'
    headerOpacity.style.opacity = '1'
    console.log(hiddenColorMain, hiddenColorBg)

})

// const addLogoInput = document.querySelector('#addLogoInput')
const hiddenLogoInput = document.querySelector('#logoInput')
const confirmLogoButton = document.querySelector('#confirmLogo')
let logoInputFile = document.querySelector('#addLogoInput')


confirmLogoButton.addEventListener('click', ()=>{
    let dataTransfer = new DataTransfer()
    // console.log(logoInputFile.files)
    dataTransfer.items.add(logoInputFile.files[0])
    hiddenLogoInput.files = dataTransfer.files
    modalWindowLogo.hidden = true
    bodyOpacity.style.opacity = '1'
    headerOpacity.style.opacity = '1'
})

