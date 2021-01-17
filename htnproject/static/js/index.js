var session = Math.random().toString(36).slice(2);
document.querySelector('#session-submit').onclick = () => {
    let first_name = document.querySelector('#first-name');
    let course = document.querySelector('#course-code');
    let pin = document.querySelector('#school-pin');

    var submission = {
        "first_name": first_name.value,
        "course": course.value,
        "pin": pin.value
    }
    // Perform validation later.
    socket.send(JSON.stringify({
        "type": "add_student_to_queue",
        "data": submission
    }));
    localStorage.setItem('submission', submission);
};

var socket = new WebSocket(
    (location.protocol == "https:" ? "wss" : "ws") + "://" +
    location.host +
    "/ws/video/" +
    session +
    "/"
);

socket.onopen = event => {
    console.log('We are connected!');
};

socket.onmessage = event => {
    let data = JSON.parse(event['data']);
    switch (data['status']) {
        case 'success':
            setTimeout(() => location.replace('/session/' + session), 500); // assume that connection is secure because webrtc won't work without it.
            break;
        case 'failure':
            // Create Toast Or Alert
            break;
    }
}

socket.onclose = event => {
    socket.send(JSON.stringify({
        "type": "remove_student_from_queue",
        "data": JSON.parse(localStorage.getItem('submission'))
    }));
    console.log('We are now closing the connection!');
};