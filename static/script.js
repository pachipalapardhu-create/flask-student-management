document.getElementById("studentForm").addEventListener("submit", function(e){

    e.preventDefault();

    let data = {
        sno: document.getElementById("sno").value,
        name: document.getElementById("name").value,
        age: document.getElementById("age").value,
        mobile: document.getElementById("mobile").value
    };

    fetch("/student", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })

    .then(response => response.json())

    .then(result => {
        document.getElementById("message").innerHTML = result.message;
    });

});