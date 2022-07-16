 /*navbar*/
 const toggleMenu = document.querySelector('.toggle');
 const navigation = document.querySelector('.navigation');
 toggleMenu.onclick = function() {
         toggleMenu.classList.toggle('active');
         navigation.classList.toggle('active');
     }
     /*animate header*/
 let stars = document.getElementById('stars');
 let moon = document.getElementById('moon');
 let mountains_behind = document.getElementById('mountains_behind');
 let mountains_front = document.getElementById('mountains_front');
 let text = document.getElementById('text');
 let btn = document.getElementById('btn');
 let header = document.querySelector('header');

 window.addEventListener('scroll', function() {
     let value = window.scrollY;
     stars.style.left = value * 0.25 + 'px';
     moon.style.top = value * 1.05 + 'px';
     mountains_behind.style.top = value * 0.5 + 'px';
     mountains_front.style.top = value * 0 + 'px';

     text.style.top = 50 + value * -0.5 + '%';
     btn.style.marginTop = value * 1.5 + 'px';
     header.style.top = value * 0.5 + 'px';
 })