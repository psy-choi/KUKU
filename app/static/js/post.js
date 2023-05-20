const customSelect = document.querySelector(".custom-select");
const selectedOption = customSelect.querySelector(".selected-option");
const options = customSelect.querySelector(".options");
const select = customSelect.querySelector("select");

selectedOption.addEventListener("click", () => {
  options.style.display = options.style.display === "none" ? "block" : "none";
});

options.addEventListener("click", (event) => {
  const selectedValue = event.currentTarget.getAttribute("data-value");
  const selectedText = event.currentTarget.innerHTML;
  selectedOption.innerHTML = selectedText;
  select.value = selectedValue;
  options.style.display = "none";
});
