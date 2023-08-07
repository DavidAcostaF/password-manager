const passwordElement = document.getElementById("password");

passwordElement.addEventListener("keyup", validateCharactersPassword)

function validateCharactersPassword() {
    let upperCase = /[A-Z]/;
    let lowerCase = /[a-z]/;
    let number = /[0-9]/;
    let special = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
    let minCharacters = 12

    if (passwordElement.value.match(upperCase)) {
        document.getElementById("uppercase").classList.remove("invalid");
        document.getElementById("uppercase").classList.add("valid");
    } else {
        document.getElementById("uppercase").classList.remove("valid");
        document.getElementById("uppercase").classList.add("invalid");
    }

    if (passwordElement.value.match(lowerCase)) {
        document.getElementById("lowercase").classList.remove("invalid");
        document.getElementById("lowercase").classList.add("valid");

    } else {
        document.getElementById("lowercase").classList.remove("valid");
        document.getElementById("lowercase").classList.add("invalid");

    }

    if (passwordElement.value.match(number)) {
        document.getElementById("number").classList.remove("invalid");
        document.getElementById("number").classList.add("valid");

    } else {
        document.getElementById("number").classList.remove("valid");
        document.getElementById("number").classList.add("invalid");

    }

    if (passwordElement.value.match(special)) {
        document.getElementById("special").classList.remove("invalid");
        document.getElementById("special").classList.add("valid");

    } else {
        document.getElementById("special").classList.remove("valid");
        document.getElementById("special").classList.add("invalid");

    }

    if (passwordElement.value.length >= minCharacters) {
        document.getElementById("lenght").classList.remove("invalid");
        document.getElementById("lenght").classList.add("valid");

    } else {
        document.getElementById("lenght").classList.remove("valid");
        document.getElementById("lenght").classList.add("invalid");

    }

}


const showPassword = function () {
    let password = document.getElementById("password");
    let password2 = document.getElementById("password2");

    if (password.type === "password") {
        password.type = "text";
        password2.type = "text";
    } else {
        password.type = "password";
        password2.type = "password";
    }
}

const randomElement = document.getElementById("random");


function generateRandomPassword(length) {
    const characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{};':\"\\|,.<>/?";
    let password = "";

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters.charAt(randomIndex);
    }

    return password;
}


const generatePassword = function () {
    let password = document.getElementById("password");
    let password2 = document.getElementById("password2");

    const passwordRegex = /^[0-9,A-Z,a-z,!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]{12}$/;

    let generatedPassword = generateRandomPassword(12);
    while (!generatedPassword.match(passwordRegex)) {
        generatedPassword = generateRandomPassword(12);
    }

    password.value = generatedPassword;
    password2.value = generatedPassword;

    validateCharactersPassword();
}

randomElement.addEventListener("click", generatePassword);



function validatePassword(){
    

}