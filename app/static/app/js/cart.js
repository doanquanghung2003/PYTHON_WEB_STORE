// var updateBtns = document.getElementsByClassName('update-cart');
var price, quantity,total_price;

function updateOrder(e) {
  var productId = e.dataset.product;
  var action = e.dataset.action;
  console.log("productId", productId, "action", action);
  console.log("user", user);
  if (user === "AnonymousUser") {
    console.log("user not login");
  } else {
    updateUserOrder(productId, action);
  }
}

function updateUserOrder(product_id, action) {
  console.log(action);
  console.log("user logged in,success add");
  var url = "/update_item/";
  // fetch(url, {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/json",
  //     "X-CSRFToken": csrftoken,
  //   },
  //   body: JSON.stringify({ productId: product_id, action: action }),
  // })
  //   .then((response) => {
  //     return response.json();
  //   })
  //   .then((data) => {
  //     console.log("data", data)
  //     location.reload()
  //   })
  $.ajax({
    type:'POST',
    url: url,
    data: JSON.stringify({
      productId: product_id, 
      action: action
    }),
    success: response => {
      console.log('done: ', response)
      // location.reload()
    },
    error: error => {
      console.log('error: ',error)
    }
  })
}