document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem("loginSuccess") === "true") {
        showToast("✅ تسجيل الدخول ناجح!");
        localStorage.removeItem("loginSuccess");
    }
});
function showToast(message) {
    let toast = document.getElementById("toast");
    toast.innerHTML = `<p>${message}</p>`;
    toast.classList.add("show");
    setTimeout(() => {
        toast.classList.remove("show");
    }, 5000); 
}