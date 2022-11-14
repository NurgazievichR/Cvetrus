window.addEventListener("scroll", () => {
  localStorage.setItem('scrollY', window.scrollY)
})

window.addEventListener('DOMContentLoaded', () => {
  window.scrollTo({
    top: localStorage.getItem('scrollY'),
    behavior: "instant"
  })
})