// Get the search input element
const search = document.querySelector('.search');
const container = document.querySelector('.trending');

// Define the animation properties
const searchAnim = anime({
  targets: search,
  translateX: '50px',
  duration: 2000,
  autoplay: false,
  width: '83%'
});

const animation1 = anime({
  targets: container,
  duration: 1000,
  height: '92vh',
  width: '20%',
  borderRadius: '16px',
  autoplay: false
});

const animation2 = anime({
  targets: container,
  duration: 1000,
  height: '5.3vh',
  width: '3%',
  borderRadius: '16px',
  autoplay: false
});

let isAnimating = false;
let currentAnimation = animation1;

// Start the search animation when the page loads
window.addEventListener("load", () => {
  searchAnim.play();
});

// Toggle between animations on click
container.addEventListener("click", () => {
  if (!isAnimating) {
    currentAnimation.play();
  } else {
    animation2.play();
  }
  isAnimating = !isAnimating;
});
