function domReady(fn) {
    if (
        document.readyState === "complete" ||
        document.readyState === "interactive"
    ) {
        setTimeout(fn, 1000);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

domReady(function () {


    function onScanSuccess(decodeText) {
        sendQRCodeToServer(decodeText);
    }

    let htmlscanner = new Html5QrcodeScanner(
        "my-qr-reader",
        {fps: 10, qrbox: 250}
    );
    htmlscanner.render(onScanSuccess);
});

function sendQRCodeToServer(decodeText) {
    fetch('/qr-scanner/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        },
        body: JSON.stringify({decoded: decodeText})
    })
        .then(response => response.json())
        .then(data => {
            if (data.redirect_url) {

                window.location.href = data.redirect_url;
            }
        })
        .catch(error => console.error('Error:', error));
}

function getCSRFToken() {
    let cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i].trim();
        if (cookie.startsWith('csrftoken=')) {
            return cookie.split('=')[1];
        }
    }
    return '';
}
