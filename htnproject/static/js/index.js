const constraints  = {
    video: true,
    audio: true
}

async function getVideo() {
    var video = document.querySelector('video');
    const stream = await navigator
    .mediaDevices
    .getUserMedia(constraints)
    .then(stream => {
        video.srcObject = stream;
        console.log("Successfully fetched stream");
    })
    .catch(error => {
        console.log("Failed to fetch stream", error);
    })
    video.srcObject = stream;
}

window.addEventListener("DOMContentLoaded", () => {
    getVideo();
});