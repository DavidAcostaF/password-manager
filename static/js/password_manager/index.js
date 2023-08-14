function showPassword(id, iconEye) {
    element = document.getElementById(id);
    if (element.type === "password") {
        element.type = "text";
        iconEye.children[0].classList.remove("fa-eye");
        iconEye.children[0].classList.add("fa-eye-slash");

    } else {
        element.type = "password";
        iconEye.children[0].classList.remove("fa-eye-slash");
        iconEye.children[0].classList.add("fa-eye");
    }

}


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


async function postData(url, body) {
    if (body != null) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,

            },
            body: JSON.stringify(body)
        })

    }

}

async function createPassword() {
    let password = document.getElementById("password-input");
    let title = document.getElementById("title-input");

    if (password.value != "" && title.value != "") {
        let body = {
            "password": password.value,
            "title": title.value
        }
        response = await postData("/create_password/", body);
        console.log(response)
    }


}


