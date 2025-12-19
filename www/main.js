$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: 'bounseIn',
        },
        out: {
            effect: 'bounseOut',
            delayScale: 1.5,
        }
    });
});