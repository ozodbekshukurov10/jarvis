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

    // Siri Wave configuration
      var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: 'ios9',
    amplitude: 1,
    speed: 0.30,
    audiostart: true
  });

 // Siri message animation
$('.siri-message').textillate({
    loop: true,
    sync: true,
    in: {
        effect: 'fadeInUp',   // to‘g‘ri nom
        sync: true,
    },
    out: {
        effect: 'fadeOutUp',  // to‘g‘ri nom
        sync: true,
    }
});


// mic button click event
$("#MicBtn").click(function () {

    eel.playAssistantSound()

    $("#Oval").attr("hidden", true);      // yashirish
    $("#siriwave").attr("hidden", false); // ko‘rsatish

});

});

