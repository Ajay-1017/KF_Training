import { apiRequest, getJson } from "./api.js";

const form = document.getElementById("login-form");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const message = document.getElementById("message");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const email = emailInput.value.trim();
    const password = passwordInput.value;

    if (!email || !password) {
        message.textContent = "Email and password are required";
        return;
    }

    if (password.length < 8) {
        message.textContent = "Password must be at least 8 characters";
        return;
    }

    const formData = new URLSearchParams();
    formData.append("username", email);
    formData.append("password", password);

    try {
        const response = await apiRequest("/users/token", {
            method: "POST",
            body: formData
        });

        const data = await getJson(response);

        if (!response.ok) {
            message.textContent = data.detail || "Login failed";
            return;
        }

        // The JWT is NOT stored by JavaScript.
        // The backend put it in an HttpOnly cookie.
        window.location.href = `users.html?public_id=${data.publicId}`;
        
    } catch (error) {
        message.textContent = "Unable to connect to server";
    }
});
