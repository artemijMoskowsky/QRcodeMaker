let deleteCardList = document.querySelectorAll('.delete-card')
let modalBg = document.querySelector('.bg-modal-delete')
const bodyOpacity = document.querySelector('.main-for-qrcodes')
const headerOpacity = document.querySelector('header')
const footerOpacity = document.querySelector('footer')

let yesDelete = document.querySelector('#yesDelete')
let noDelete = document.querySelector('#noDelete')

let buttonId = null

deleteCardList.forEach(del => {
    del.addEventListener('click', ()=>{
        console.log('click')
        buttonId = del.value
        modalBg.style.display = "flex"
        bodyOpacity.style.opacity = '0.5'
        headerOpacity.style.opacity = '0.5'
        footerOpacity.style.opacity = '0.5'
    })
})

yesDelete.addEventListener('click', ()=>{
    console.log('yes')
    modalBg.style.display = "none"
    bodyOpacity.style.opacity = '1'
    headerOpacity.style.opacity = '1'
    footerOpacity.style.opacity = '1'
    console.log(buttonId);
    yesDelete.value = buttonId
})

noDelete.addEventListener('click', ()=>{
    console.log('no')
    modalBg.style.display = "none"
    bodyOpacity.style.opacity = '1'
    headerOpacity.style.opacity = '1'
    footerOpacity.style.opacity = '1'
})