// بازیابی cart از localStorage یا مقداردهی اولیه به آرایه خالی
let cart = JSON.parse(localStorage.getItem('cart')) || [];
let nav = document.getElementById('main-nav')
let nav2 = document.getElementById('second-nav')
let navHeight = nav.offsetHeight.toString()
nav2.style.top = navHeight + 'px'
let space = document.getElementsByClassName('space')[0]
space.style.height = navHeight + 'px'

// ذخیره کردن cart در localStorage
window.saveCart = function () {
    localStorage.setItem('cart', JSON.stringify(cart));
};
window.updateCartCount = function () {
    const count = cart.reduce((total, item) => total + Number(item.quantity), 0);
    const countElement = document.getElementById('cart-count');
    if (countElement) {
        countElement.textContent = count;
    }
};

// بازیابی cart از localStorage
window.getCart = function () {
    return JSON.parse(localStorage.getItem('cart')) || [];
};

// افزودن محصول به سبد خرید
window.addToCartPage = function (productId, name, price, quantity = 1) {

    const existingProduct = cart.find(item => item.id === productId);
    if (existingProduct) {
        existingProduct.quantity += Number(quantity);
    } else {
        cart.push({ id: productId, name, price, quantity });
    }
    saveCart();
    updateCartCount();

    toastr.success(`${quantity} x ${name} added to your cart!`);
};

// به‌روزرسانی تعداد محصول
window.updateQuantity = function (productId, newQuantity) {
    const product = cart.find(item => item.id === productId);
    if (product) {
        if (newQuantity <= 0) {
            // حذف محصول اگر تعداد کمتر یا مساوی صفر باشد
            removeFromCart(productId);
        } else {
            product.quantity = newQuantity;
            saveCart();
            displayCart('cart-container');
            updateCartCount();
        }
    }
};

// حذف محصول از سبد خرید
window.removeFromCart = function (productId) {
    cart = cart.filter(item => item.id !== productId); // حذف محصول از آرایه
    saveCart(); // ذخیره آرایه به‌روزرسانی‌شده در localStorage
    displayCart('cart-container'); // به‌روزرسانی نمایش سبد خرید
    updateCartCount(); // به‌روزرسانی نشانگر تعداد محصولات
};


// نمایش محصولات در سبد خرید
window.displayCart = function (containerId) {

    const cart = getCart(); // دریافت اطلاعات سبد خرید از localStorage
    const container = document.getElementById(containerId);
    container.innerHTML = ''; // پاک کردن محتوای قبلی

    if (cart.length === 0) {
        container.textContent = 'Your cart is empty.';
        return;
    }

    let total = 0;

    cart.forEach(item => {
        const itemTotal = item.price * item.quantity;
        total += itemTotal;

        // ایجاد div برای هر محصول
        const itemDiv = document.createElement('div');
        itemDiv.className = 'cart-item';

        itemDiv.innerHTML = `
        <span>${item.name} - $${item.price}</span>
        <input type="number" value="${item.quantity}" min="1" 
            onchange="updateQuantity('${item.id}', parseInt(this.value))">
        <button onclick="removeFromCart('${item.id}')">Remove</button>
      `;

        container.appendChild(itemDiv);
    });

    // نمایش قیمت کل
    const totalDiv = document.createElement('div');
    totalDiv.id = 'total';
    totalDiv.textContent = `Total: $${total}`;
    container.appendChild(totalDiv);
};


// به‌روزرسانی تعداد محصولات در نشانگر


// مقداردهی اولیه هنگام بارگذاری صفحه
document.addEventListener('DOMContentLoaded', () => {
    updateCartCount();

    // اگر صفحه سبد خرید است، سبد خرید را نمایش دهد
    if (window.location.pathname.includes('cart.html')) {
        displayCart('cart-container');
    }
});


if (window.location.pathname === '/zana-mall/index.html' || window.location.pathname === '/zana-mall/') {
    console.log('zzz')
    let addToCarts = document.querySelectorAll('.add-to-cart')
    addToCarts.forEach(button => {
        button.addEventListener('click', () => {
            // اطلاعات محصول را از عناصر HTML مرتبط دریافت کنید
            const productElement = button.closest('.card-pro');
            const productId = productElement.getAttribute('data-id');
            const productName = productElement.getAttribute('data-name');
            const productPrice = parseFloat(productElement.getAttribute('data-price'));

            // افزودن محصول به سبد خرید
            addToCartPage(productId, productName, productPrice);
        });
    })

}

if (window.location.pathname === '/zana-mall/shop.html') {
        console.log('zzz')
        let addToCarts = document.querySelectorAll('.add-to-cart')
        addToCarts.forEach(button => {
            button.addEventListener('click', () => {
                console.log('zzz')
                // اطلاعات محصول را از عناصر HTML مرتبط دریافت کنید
                const productElement = button.closest('.card-pro');
                const productId = productElement.getAttribute('data-id');
                const productName = productElement.getAttribute('data-name');
                const productPrice = parseFloat(productElement.getAttribute('data-price'));

                // افزودن محصول به سبد خرید
                addToCartPage(productId, productName, productPrice);
            });
        })

    }
    if (window.location.pathname === '/zana-mall/product.html') {
        console.log('zzz')
        setTimeout(() => {
            let addToCart = document.querySelector('.add-to-cart')
            let price = document.getElementsByClassName('product-info')[0].children[1].children[0].textContent.slice(8)
            let params = new URLSearchParams(window.location.search);
            let productId = params.get("id")
            let productName = document.getElementsByClassName('product-info')[0].children[0].textContent
            addToCart.addEventListener('click', () => {
                let proNumber = document.getElementsByClassName('quantity')[0].children[0].value
                addToCartPage(productId, productName, price, proNumber);
            })
        }, 1200);

    }
