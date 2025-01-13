let choosePlan = document.querySelectorAll("#choose-plan")

let viewModal = document.querySelector("#modal-window")

for (let i = 0; i < choosePlan.length; i++){
    choosePlan[i].addEventListener("click", (event)=>{
        viewModal.style.display = "flex"
    })
}