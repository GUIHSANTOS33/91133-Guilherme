document.getElementById("loginForm").addEventListener("submit", function(event){
    event.preventDefault;

const username = document.getElementById("username").value;
const password = document.getElementById("password").value;


if (!username || !password){
alert("Por favor, preencha todos os campos.");
return
}

if (password.length < 8){
    alert("Insira uma senha com pelo menos 8 caracteres.");
return
}
    
// Salvar o nome do usuário
localStorage.setItem("username", username)
window.location.href="painel.html"; // Abre uma nova página 
alert("Login bem sucedido!"); // Pop-up de sucesso
});

    