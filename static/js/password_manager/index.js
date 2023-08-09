function showPassword(id,iconEye){
    element = document.getElementById(id);
    if(element.type === "password"){
        element.type = "text";
        iconEye.children[0].classList.remove("fa-eye");
        iconEye.children[0].classList.add("fa-eye-slash");

    }else{
        element.type = "password";
        iconEye.children[0].classList.remove("fa-eye-slash");
        iconEye.children[0].classList.add("fa-eye");
    }

}