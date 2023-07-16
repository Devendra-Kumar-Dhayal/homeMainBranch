
// section
let next = document.getElementById('nextButton')
let prev = document.getElementById('prevButton')

next.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    console.log("button next pressed")
    document.querySelector('.slide').appendChild(items[0])
})

prev.addEventListener('click', function(){
    let items = document.querySelectorAll('.item')
    document.querySelector('.slide').prepend(items[items.length - 1])
})