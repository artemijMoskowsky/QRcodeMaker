let choosePlan = document.querySelectorAll("#choose-plan")

let viewModal = document.querySelector("#modal-window")

let subscribeInput = document.querySelector(".subscribe-input")

for (let i = 0; i < choosePlan.length; i++){
    choosePlan[i].addEventListener("click", (event)=>{
        viewModal.style.display = "flex"
        subscribeInput.value = choosePlan[i].value
        console.log(subscribeInput.value)
    })
}

document.getElementById("create-QRcode").onclick = function(){

    window.location.href = "http://127.0.0.1:8000/qrcodes/create_qrcode/";
};

