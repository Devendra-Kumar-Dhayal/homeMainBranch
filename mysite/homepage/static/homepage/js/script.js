
// section
let next = document.getElementById('next')
let prev = document.getElementById('prev')

next.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    console.log("button next pressed")
    document.querySelector('.slide').appendChild(items[0])
})

prev.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').prepend(items[items.length - 1])
})