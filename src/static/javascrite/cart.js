function increase() {
    const input = document.getElementById("quantity");
    let value = parseInt(input.value);
    if (value < 10) {
      input.value = value + 1;
    }
  }
  
  function decrease() {
    const input = document.getElementById("quantity");
    let value = parseInt(input.value);
    if (value > 1) {
      input.value = value - 1;
    }
  }
  