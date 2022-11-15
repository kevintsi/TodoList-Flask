console.log("Begin");

const nb_tasks = document.getElementsByClassName("task_check").length
const progress_bar = document.getElementById("progress")
var nb_checked_task = 0

function handleChange(checkbox) {
    var label = document.getElementById("task" + checkbox.id)
    if (checkbox.checked) {
        nb_checked_task++
        progress_bar.style.width = Math.round(calcul_pourcentage()) + "%"
        label.style.textDecoration = "line-through"
    } else {
        nb_checked_task--
        progress_bar.style.width = Math.round(calcul_pourcentage()) + "%"
        label.style.textDecoration = "none"
    }


    var new_width = parseInt(progress_bar.style.width.split("%")[0])

    if (new_width >= 80) {
        progress_bar.style.backgroundColor = "green"
    } else if (new_width > 50 && new_width < 80) {
        progress_bar.style.backgroundColor = "orange"
    } else {
        progress_bar.style.backgroundColor = "red"
    }
    if (new_width == 0) {
        progress_bar.innerHTML = ''
    } else {
        progress_bar.innerHTML = new_width + "%"
    }
}

function calcul_pourcentage() {
    return nb_checked_task / nb_tasks * 100
}