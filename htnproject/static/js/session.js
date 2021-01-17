var local = document.getElementById('local');
var remote = document.getElementById('remote');
var connection = new RTCMultiConnection();
const session = "{{ token|safe }}";
connection.socketUrl = connection.socketURL = 'https://rtcmulticonnection.herokuapp.com:443/';

connection.iceServers = [];
connection.iceServers.push({
    urls: 'stun:stun.l.google.com:19302'
});
connection.iceServers.push({
    urls: 'turn:numb.viagenie.ca:3478',
    credential: 'HTNProject',
    username: 'HTNProject@mailpoof.com'   
});

connection.session = {
    audio: true,
    video: true
};

connection.maxParticipantsAllowed = 2;

connection.sdpConstraints.mandatory = {
    OfferToReceiveAudio: true,
    OfferToReceiveVideo: true
};

connection.onstream = event => {
    event.mediaElement.controls = false;
    switch (event.type) {
        case 'local':
            local.appendChild(event.mediaElement);
            break;
        case 'remote':
            document.querySelector('#instructor-message').innerHTML = "";
            remote.appendChild(event.mediaElement);
            break;
    }
};

window.addEventListener("DOMContentLoaded", () => {
    connection.openOrJoin(session);
});

document.querySelector('#end-call').onclick = () => {
    // Perform validation later.
    // socket.send(JSON.stringify({
    //     "type": "remove_student_from_queue",
    //     "data": localStorage.getItem('submission')
    // }));
    setTimeout(() => location.replace('http://' + location.host + '/'), 500);
};

document.querySelector('#mute-microphone').onclick = () => {
    if (document.querySelector('#mute-microphone').textContent == 'Mute Microphone') {
        connection.attachStreams[0].mute('audio');
        document.querySelector('#mute-microphone').textContent = 'Unmute Microphone';
    } else {
        connection.attachStreams[0].unmute('audio');
        document.querySelector('#mute-microphone').textContent = 'Mute Microphone';
    }
};
