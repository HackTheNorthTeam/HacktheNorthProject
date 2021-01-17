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

connection.mediaConstraints = {
    audio: true,
    video: {
        mandatory: {
            minWidth: 360,
            maxWidth: 720,
            minHeight: 360,
            maxHeight: 720,
            minAspectRatio: 1.66
        },
    }
}

connection.maxParticipantsAllowed = 2;

connection.sdpConstraints.mandatory = {
    OfferToReceiveAudio: true,
    OfferToReceiveVideo: true
};

connection.onstream = event => {
    switch (event.type) {
        case 'local':
            local.appendChild(event.mediaElement);
            break;
        case 'remote':
            remote.appendChild(event.mediaElement);
            break;
    }
};

window.addEventListener("DOMContentLoaded", () => {
    connection.openOrJoin(session);
});

document.querySelector('#end-call').onclick = () => {
    // Perform validation later.
    socket.send(JSON.stringify({
        "type": "remove_student_from_queue",
        "data": localStorage.getItem('submission')
    }));
    setTimeout(() => location.replace('http://' + location.host + '/bye/'));
};