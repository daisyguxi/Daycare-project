//loop over the daycares in daycare list from Yelp API
const eventBtn = document.querySelector("#save");
// const handleClick = () => {
//   alert(`Stop clicking me!`);
// };
// button.addEventListener("click", handleClick);

// eventBtn.addEventListener("click", (evt) => {
//   console.log(evt);
// });

eventBtn.addEventListener("click", (evt) => {
  evt.preventDefault();

  const formInputs = {
    name: document.querySelector("#name").value,
    phone: document.querySelector("#phone").value,
    rating: document.querySelector("#rating").value,
    address: document.querySelector("#street").value,
    minAge: document.querySelector("#agelow").value,
    maxAge: document.querySelector("#agehigh").value,
    language1: document.querySelector("#language1").value,
    language2: document.querySelector("#language2").value,
    potty: document.querySelector("#potty").value,
    fee: document.querySelector("#fee").value,
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
