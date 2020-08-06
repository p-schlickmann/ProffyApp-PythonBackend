document.querySelector('#add-time').addEventListener('click', addElement)

function addElement() {
    const newField = document.querySelector('.schedule-item').cloneNode(true)
    const fields = newField.querySelectorAll("input")

    for (var field of fields){
        field.value = ''
    }
    
    document.querySelector('#schedule-items').appendChild(newField)
}

function removeField(el){
    var len = document.querySelectorAll(".schedule-item").length
    if (len == 1){
        return
    }else{
    var element = el.parentElement.parentElement
    element.remove()
}
}