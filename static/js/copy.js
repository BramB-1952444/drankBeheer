function copy() {
    var text = "BE10 9733 6252 4804";
    navigator.clipboard.writeText(text).then(
        function () {
            alert("Rekening nummer gekopieerd");
        },
        function (err) {
            alert("Kon rekening nummer niet kopieren");
        }
    );
}
