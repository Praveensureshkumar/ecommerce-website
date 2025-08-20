function updatePrices() {
    let totalPrice = 0;
    let totalItems = 0;
    let totalOfferPrice = 0;
    let deliveryCharges = 0;
    let maxDelivery = 0;
  
    document.querySelectorAll('.card.cart-item').forEach(card => {
      const price = parseFloat(card.dataset.price);
      const quantity = parseInt(card.querySelector('input.quantity').value);
      const original_price = parseFloat(card.dataset.originalprice);
      const productTotal = price * quantity;
  
      totalItems += quantity;
      totalPrice += productTotal;
      totalOfferPrice += original_price * quantity;
  
      // ₹50 delivery charge if total per product is <= ₹500
      if (productTotal <= 500) {
        deliveryCharges += 50;
      }
  
      maxDelivery += 50;
    });
  
    const discount = totalOfferPrice - totalItems;
    const extraDiscount = totalPrice > 1000 ? 100 : 0;
    const promiseFee = 99;
    const finalAmount = totalPrice - extraDiscount + deliveryCharges + promiseFee;
    const totalSavings = discount + extraDiscount + (deliveryCharges === 0 ? maxDelivery : 0);
  
    document.querySelector('.total-price').textContent = `₹${totalPrice}`;
    document.querySelector('.discount').textContent = `– ₹${discount}`;
    document.querySelector('.extra_discount').textContent = `– ₹${extraDiscount}`;
  
    const deliveryEl = document.querySelector('.delivery');
    if (deliveryCharges === 0) {
      deliveryEl.innerHTML = `<s>₹${maxDelivery}</s> <span style="color:green;">Free</span>`;
    } else {
      deliveryEl.textContent = `₹${deliveryCharges}`;
    }
  
    document.querySelector('.promise_fee').textContent = `₹${promiseFee}`;
    document.querySelector('.final_amount').textContent = `₹${finalAmount}`;
    document.querySelector('.total_savings').textContent = `You will save ₹${totalSavings} on this order`;
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    updatePrices();
  
    document.querySelectorAll('.card.cart-item').forEach(card => {
      const input = card.querySelector('input.quantity');
      const increaseBtn = card.querySelector('button.increase');
      const decreaseBtn = card.querySelector('button.decrease');
  
      increaseBtn.addEventListener('click', () => {
        let qty = parseInt(input.value);
        if (qty < 10) {
          input.value = qty + 1;
          updatePrices();
        }
      });
  
      decreaseBtn.addEventListener('click', () => {
        let qty = parseInt(input.value);
        if (qty > 1) {
          input.value = qty - 1;
          updatePrices();
        }
      });
  
      input.addEventListener('change', () => {
        let qty = parseInt(input.value);
        if (isNaN(qty) || qty < 1) qty = 1;
        if (qty > 10) qty = 10;
        input.value = qty;
        updatePrices();
      });
    });
  });
  