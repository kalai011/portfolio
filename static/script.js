
var typed = new Typed('#typing', {
    strings: [
        'Python Developer',
        'Full Stack Developer'
    ],
    typeSpeed: 70,
    backSpeed: 40,
    loop: true
});

AOS.init({
    duration: 1000
});

particlesJS('particles-js', {
    particles: {
        number: { value: 80 },
        size: { value: 3 },
        color: { value: '#38bdf8' },
        line_linked: {
            enable: true,
            color: '#38bdf8'
        },
        move: {
            speed: 2
        }
    }
});
