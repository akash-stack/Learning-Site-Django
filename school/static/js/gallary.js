const carouselSlide = document.querySelector('.carousel-slide');
const carouselSlide = document.querySelectorAll('.carousel-slide img');

//Buttons

const prevBtn = document.querySelector('#prevBtn');
const nextBtn = document.querySelector('#nextBtn');

//counter
let counter = 1;
const = carouselImages[0].clientWidth;

carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';

//button style
nextBtn.addEventListener('click', () => {
carouselSlide.style.transition= "transform 0.4s ease-in-out";
counter++;
carouselSlide.style.transform = 'translateX(' + (-size * counter) + 'px)';
});
