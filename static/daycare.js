//loop over the daycares in daycare list from Yelp API
const eventBtn = document.querySelector("#save");

eventBtn.addEventListener("click", (evt) => {
  evt.preventDefault();

  const formInputs = {
    name: document.querySelector("#name").innerHTML,
    phone: document.querySelector("#phone").innerHTML,
    rating: document.querySelector("#rating").innerHTML,
    address: document.querySelector("#street").innerHTML,
    minAge: document.querySelector("#agelow").innerHTML,
    maxAge: document.querySelector("#agehigh").innerHTML,
    language1: document.querySelector("#language1").innerHTML,
    language2: document.querySelector("#language2").innerHTML,
    potty: document.querySelector("#potty").innerHTML,
    fee: document.querySelector("#fee").innerHTML,
  };

  fetch("/saved_daycares", {
    method: "POST",
    body: JSON.stringify(formInputs),
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((responseJson) => {
      alert(responseJson.status);
    });
});
