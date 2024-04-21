document.addEventListener('DOMContentLoaded', function() {
    const productDivs = document.querySelectorAll('.product');
    const form = document.getElementById('cart-form');

    // Обработчик клика для кнопки сброса
    const resetButton = document.getElementById('reset-button');
    resetButton.addEventListener('click', function() {
        const quantityElements = document.querySelectorAll('.product-quantity');
        quantityElements.forEach(element => {
            if (element) {
                element.innerText = 0;
            }
        });

        // Удаление скрытых полей формы, исключая поле с CSRF токеном
        const hiddenInputs = form.querySelectorAll('input[type="hidden"]');
        hiddenInputs.forEach(input => {
            if (input && input.name !== 'csrfmiddlewaretoken') { // Проверяем, что это не поле CSRF токена
                input.parentNode.removeChild(input);
            }
        });
    });

    // Кликер + обработчик формы
    productDivs.forEach(productDiv => {
        productDiv.addEventListener('click', function() {
            const productId = this.dataset.productId;
            const quantityElement = document.querySelector('.product-quantity[data-product-id="' + productId + '"]');
            let quantity = parseInt(quantityElement.innerText);

            // Увеличение значения в карточке
            quantityElement.innerText = ++quantity;

            // Создание или обновление скрытого поля для продукта
            let input = form.querySelector(`input[name="product_${productId}"]`);
            if (!input) {
                input = document.createElement('input');
                input.type = 'hidden';
                input.name = `product_${productId}`;
                form.appendChild(input);
            }
            input.value = quantity;
        });
    });
});