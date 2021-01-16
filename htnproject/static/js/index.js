var local = document.getElementById('local');
var remote = document.getElementById('remote');
var connection = new RTCMultiConnection();
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

document.querySelector('#session-submit').onclick = () => connection.openOrJoin(document.querySelector('#room-name').textContent);