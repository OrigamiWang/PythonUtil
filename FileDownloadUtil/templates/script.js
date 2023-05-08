let form = document.getElementById("upload-form");
form.addEventListener("submit", function (event) {
    console.log("listen submit file...")
    event.preventDefault();
    let file = document.getElementById("file").files[0];
    let formData = new FormData();
    formData.append("file", file);
    fetch("/upload", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            //do something with data
        })
        .catch(error => {
            console.log(error)
            //handle error
        });
});