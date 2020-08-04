const nickName = document.querySelector(".statSearch");
const toggleBtn = document.querySelector(".statButton");
const menu = documnet.querySelector("nav_menu");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
});
