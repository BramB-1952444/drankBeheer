function copy() {
    const rekening = 'BE77 7370 6284 6242';
    navigator.clipboard.writeText(rekening).then(
        function () {
            alert('Rekening nummer gekopieerd');
        },
        function (err) {
            alert('Kon rekening nummer niet kopieren');
        }
    );
}
