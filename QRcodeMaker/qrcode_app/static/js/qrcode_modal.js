const modalColor = document.querySelector('#modal-color-button')
const modalWindowColor = document.querySelector('.modal-window-color')
const bodyOpacity = document.querySelector('.main-input')
const headerOpacity = document.querySelector('header')
const footerOpacity = document.querySelector('footer')


modalColor.addEventListener("click", () =>{
        modalWindowColor.style.display = "flex"
        bodyOpacity.style.opacity = '0.5'
        headerOpacity.style.opacity = '0.5'
        footerOpacity.style.opacity = '0.5'
})

const modalLogo = document.querySelector('#modal-logo-button')
const modalWindowLogo = document.querySelector('.modal-window-logo')

modalLogo.addEventListener("click", () =>{
        modalWindowLogo.hidden = false
        bodyOpacity.style.opacity = '0.5'
        headerOpacity.style.opacity = '0.5'
        footerOpacity.style.opacity = '0.5'
    })

const modalDesign = document.querySelector('#modal-design-button')
const modalWindowDesign = document.querySelector('.modal-window-design')

modalDesign.addEventListener("click", () =>{
        modalWindowDesign.style.display = "flex"
        bodyOpacity.style.opacity = '0.5'
        headerOpacity.style.opacity = '0.5'
        footerOpacity.style.opacity = '0.5'
})

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
    footerOpacity.style.opacity = '1'
    console.log(hiddenColorMain, hiddenColorBg)

})

const hiddenLogoInput = document.querySelector('#logoInput')
const confirmLogoButton = document.querySelector('#confirmLogo')
let logoInputFile = document.querySelector('#addLogoInput')


confirmLogoButton.addEventListener('click', ()=>{
    let dataTransfer = new DataTransfer()
    dataTransfer.items.add(logoInputFile.files[0])
    hiddenLogoInput.files = dataTransfer.files
    modalWindowLogo.hidden = true
    bodyOpacity.style.opacity = '1'
    headerOpacity.style.opacity = '1'
    footerOpacity.style.opacity = '1'
})

const designCircle = document.querySelector('#designCircle')
const designSquare = document.querySelector('#designSquare')
const designBorder = document.querySelector('#designBorder')
const hiddenDesign = document.querySelector('#designHiddenInput')

const confirmDesign = document.querySelector('#confirmDesign')



designCircle.addEventListener('click', ()=>{
    console.log('circle')
    designCircle.value = 'circle'
    hiddenDesign.value = designCircle.value
    console.log(hiddenDesign)
})

designSquare.addEventListener('click', ()=>{
    console.log('square')
    designCircle.value = 'square'
    hiddenDesign.value = designCircle.value
    console.log(hiddenDesign)
})

designBorder.addEventListener('click', ()=>{
    console.log('border')
    designCircle.value = 'border'
    hiddenDesign.value = designCircle.value
    console.log(hiddenDesign)
})

confirmDesign.addEventListener('click', ()=>{
    modalWindowDesign.style.display = "none"
    bodyOpacity.style.opacity = '1'
    headerOpacity.style.opacity = '1'
    footerOpacity.style.opacity = '1'
    hiddenColorBg.value = colorInputBgQr.value
})

// let downloadPNGbutton = document.querySelector('#downloadPNG')
// let imagePNG = document.querySelector('.main-qrcode')

// downloadPNGbutton.addEventListener('click', ()=>{

// })