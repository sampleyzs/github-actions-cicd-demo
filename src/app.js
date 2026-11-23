import { add } from "./math.js";

const form = document.querySelector("#calculator");
const numberA = document.querySelector("#number-a");
const numberB = document.querySelector("#number-b");
const result = document.querySelector("#result");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const a = Number(numberA.value);
  const b = Number(numberB.value);

  result.textContent = `${a} + ${b} = ${add(a, b)}`;
});