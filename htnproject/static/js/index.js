let configuration = {
    iceServers: [
        {
            'urls': 'stun:stun.l.google.com:19302'
        },
        {
            'urls': 'turn:numb.viagenie.ca',
            'credential': 'HTNProject',
            'username': 'HTNProject@mailpoof.com'
        },
    ]
};

let constraints = {
    'video': true,
    'audio': true
}

const roomName = JSON.parse(document.getElementById('room-name').textContent);
var socket = new WebSocket(
    "wss://" +
    location.host +
    "/ws/video/" +
    roomName
    + "/"
);
var connection = new RTCPeerConnection(configuration);

socket.onopen = event => {
    console.log('Opened socket!');
};

function createIceCandidate(event) {
    if (event.candidate) {
        socket.send(JSON.stringify({
            "type": "send_ice_candidate",
            "data": event.candidate
        }));
    }
}

function addStream(event) {
    remote.srcObject = event.stream;
}

connection.onicecandidate = createIceCandidate;
connection.onaddstream = addStream;

var local = document.getElementById("local");
var remote = document.getElementById("remote");
var stream;
navigator
    .mediaDevices
    .getUserMedia(constraints)
    .then(stream => {
        this.stream = stream;
    })
    .catch(error => console.error("Failed to get user media stream.", error));


document.querySelector('#room-name-submit').onclick = function (event) {
    handleNegotiationNeededEvent();
    console.log("Sending offer");
};

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    console.log(data);
    if (data['type'] == 'offer') {
        console.log();
        handleVideoOfferMessage(data)
        console.log('Got to send answer part.');
    } else if (data['type'] == 'answer') {
        console.log('Got to send offer part.');
    } else if (data['type'] == 'ice') {
        connection.addIceCandidate(new RTCIceCandidate(data));
    }
};

function handleNegotiationNeededEvent() {
    connection.createOffer()
    .then(offer => {
        return connection.setLocalDescription(offer);
    })
    .then(() => {
        socket.send(JSON.stringify({
            "type": "send_offer",
            "data": connection.localDescription
        }));
      })
      .catch(error => console.error("Error with offer sending", error));
}

function handleVideoOfferMessage(offer) {
    connection.onicecandidate = function (event) {
        socket.send(JSON.stringify({
            "type": "send_ice_candidate",
            "data": event.candidate
        }));
    }
    connection.onaddstream = function (event) {
        remote.srcObject = event.stream;
    }
    connection.setRemoteDescription(new RTCSessionDescription(offer));
    connection.createAnswer()
    .then(answer => {
        return connection.setLocalDescription(answer);
    })
    .then(() => {
        socket.send(JSON.stringify({
            "type": "send_answer",
            "data": connection.localDescription
        }));
    })

    .then(() => {
        const stream = new MediaStream();
        connection.addEventListener('track', async (event) => {
            stream.addTrack(event.track, stream);
        });
        remote.srcObject = stream;
    })
}

socket.onclose = event => {
    console.error('Chat socket closed unexpectedly');
};