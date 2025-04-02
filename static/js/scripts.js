

let ham = document.getElementsByClassName('ham')[0]
let nav = document.getElementById('main-nav')
let nav2 = document.getElementById('second-nav')
let navHeight = nav.offsetHeight.toString()
let shops = document.getElementsByClassName('shop')
let abouts = document.getElementsByClassName('about')
let homes = document.getElementsByClassName('home')
let navItems = document.getElementsByClassName('nav-items')

let cartButtons=document.querySelector('#display-on')
function change(){
    
}

window.addEventListener('DOMContentLoaded',()=>{
    let dropMenu = document.getElementsByClassName('dropdown')
    for (const element of dropMenu) {
        element.addEventListener('click', function() {
            if (element.classList.contains('active')){
                element.classList.remove('active')
            }else{
                for (const element of dropMenu) {
                    element.classList.remove('active')
                    console.log('ccc')
                }
                element.classList.add('active')
            }
           
        })
    }
    
})

window.changeHam = function () {
    ham.classList.toggle('active')
    if (ham.classList.contains('active')) {
        nav2.style.left = '65%'

    }
    else {
        nav2.style.left = '100%'
    }
}
ham.addEventListener('click', () => {
    changeHam()
})


nav2.style.top = navHeight + 'px'

if (window.location.pathname!=='cart/') {
    let container = document.getElementsByClassName('container')[0]
    
    container.addEventListener('click', () => {
        if (ham.classList.contains('active')) {
            ham.classList.remove('active')
            nav2.style.left = '100%'
        }
    })
}



