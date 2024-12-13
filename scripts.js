

let ham = document.getElementsByClassName('ham')[0]
let nav = document.getElementById('main-nav')
let nav2 = document.getElementById('second-nav')
let navHeight = nav.offsetHeight.toString()
let space = document.getElementsByClassName('space')[0]
space.style.height = navHeight + 'px'
let shops = document.getElementsByClassName('shop')
let abouts = document.getElementsByClassName('about')
let homes = document.getElementsByClassName('home')
let navItems = document.getElementsByClassName('nav-items')
let goback = document.querySelector('.pre-page')
let cartButtons=document.querySelector('#display-on')
window.addEventListener('DOMContentLoaded', () => {
    if (goback) {
        goback.style.left = '75%'
    }

})
window.ChangeGobackB = function () {
    if (window.location.pathname === "/zana-mall/shop.html") {
        window.location.pathname = "/zana-mall/index.html"
        setTimeout(() => {
            scrollY = 0
        }, 500)
    }
    else if (window.location.pathname === "/zana-mall/product.html") {
        window.location.pathname = "/zana-mall/shop.html"
    }
    else if (window.location.pathname === "/zana-mall/cart.html") {
        window.location.pathname = "/zana-mall/shop.html"
    }

    else {
        window.location.pathname = "/zana-mall/index.html"
    }
}
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

if (window.location.pathname!=='/zana-mall/cart.html') {
    let container = document.getElementsByClassName('container')[0]
    
    container.addEventListener('click', () => {
        if (ham.classList.contains('active')) {
            ham.classList.remove('active')
            nav2.style.left = '100%'
        }
    })
}

window.slice = function (a, n) {
    let secondS = ''
    for (let index = 0; index < a.length - n; index++) {
        secondS += a[index]
    }
    return secondS
}

if (window.location.pathname === '/zana-mall/shop.html' || window.location.pathname === '/zana-mall/index.html') {

    function showProduct(id) {
        window.location.href = "/zana-mall/product.html?id=" + id
    }

    let cards = document.getElementsByClassName('card-pro')
    for (const card of cards) {
        card.children[0].addEventListener('click', () => {
            console.log('p done')
            let id = card.attributes[0].textContent
            showProduct(id)
        })
        
    }
    if (window.location.pathname === '/zana-mall/shop.html') {
        for (const navItem of navItems) {
            navItem.classList.remove('active')
        }
        for (const shop of shops) {
            shop.classList.add('active')
        }
    } else {
        for (const navItem of navItems) {
            navItem.classList.remove('active')
        }
        for (const home of homes) {
            home.classList.add('active')
        }
    }
    /*function about addtoCart()*/ 
    
}

if (window.location.pathname === '/zana-mall/about.html') {
    for (const navItem of navItems) {
        navItem.classList.remove('active')
    }
    for (const about of abouts) {
        about.classList.add('active')
    }
}

if (window.location.pathname === 'zana-mall/cart.html') {
    for (const navItem of navItems) {
        navItem.classList.remove('active')
    }
    cartButtons.classList.add('active')
    console.log('done')
}
if (window.location.pathname === '/zana-mall/product.html') {
    for (const navItem of navItems) {
        navItem.classList.remove('active')
    }
    for (const shop of shops) {
        shop.classList.add('active')
    }
    document.addEventListener('DOMContentLoaded', () => {
        let params = new URLSearchParams(window.location.search);
        let id = params.get("id")
        let mainImg = `img/products/${id}-1.webp`
        let secondImg = slice(mainImg, 5) + "2.webp"
        
        document.getElementById('content').innerHTML = `
             <div class="products">
            <section class="product-container" id=${id}>
                <!-- left side -->
                <div class="img-card">
                    <div class="main-img">
                        <img src="${mainImg}" alt="" id="featured-image">
                    </div>
                    <!-- small img -->
                    <div class="small-card">
                        <img src="${mainImg}" alt="" class="small-Img">
                        <img src="${secondImg}" alt="" class="small-Img">
                    </div>
                </div>
                <!-- Right side -->
                <div class="product-info">
                    <h3>Men T-Shirt</h3>
                    <h5><span>Price: $70</span> <del> $150</del></h5>
                    <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa accusantium, aspernatur provident beatae corporis veniam atque facilis, consequuntur assumenda, vitae dignissimos iste exercitationem dolor eveniet alias eos ullam nesciunt voluptatum.</p>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore accusamus natus dolorum. Quaerat nulla quod doloremque, officia quis provident amet adipisci unde esse iure delectus, maxime inventore optio fuga nisi?</p>
        
                    <div class="sizes">
                        <p>Size:</p>
                        <select name="Size" id="size" class="size-option">
                            <option value="xxl">XXL</option>
                            <option value="xl">XL</option>
                            <option value="medium">Medium</option>
                            <option value="small">Small</option>
                        </select>
                    </div>
        
                    <div class="quantity">
                        <input type="number" value='1' min="1" name='form'>
                        <button class="add-to-cart">Add to Cart</button>
                    </div>
        
                    <div>
                        <p>Delivery:</p>
                        <p>Free standard shipping on orders over $35 before tax, plus free returns.</p>
                        <div class="delivery">
                            <p>TYPE</p> <p>HOW LONG</p> <p>HOW MUCH</p>
                        </div>
                        <hr>
                        <div class="delivery">
                            <p>Standard delivery</p> 
                            <p>1-4 business days</p> 
                            <p>$4.50</p>
                        </div>
                        <hr>
                        <div class="delivery">
                            <p>Express delivery</p> 
                            <p>1 business day</p> 
                            <p>$10.00</p>
                        </div>
                        <hr>
                        <div class="delivery">
                            <p>Pick up in store</p> 
                            <p>1-3 business days</p> 
                            <p>Free</p>
                        </div>
                    </div>
                </div>
            </section>
        </div>
        `
        setTimeout(() => {
            document.getElementById('loader').style.display = "none";
            document.getElementById('content').style.display = "block";


            let featuedImg = document.getElementById('featured-image');
            let smallImgs = document.getElementsByClassName('small-Img');

            smallImgs[0].addEventListener('click', () => {
                featuedImg.src = smallImgs[0].src;
                smallImgs[0].classList.add('sm-card')
                smallImgs[1].classList.remove('sm-card')

            });
            smallImgs[1].addEventListener('click', () => {
                featuedImg.src = smallImgs[1].src;
                smallImgs[0].classList.remove('sm-card')
                smallImgs[1].classList.add('sm-card')
            });
            document.getElementsByClassName('pre-page')[0].style.display='block'
            document.getElementsByClassName('loader')[0].style.height = 'auto'
        }, 1000);
    })

}

