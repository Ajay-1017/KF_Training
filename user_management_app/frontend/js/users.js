import { apiRequest, getJson } from "./api.js";

const container = document.getElementById("user-card");
const message = document.getElementById("message");
const logoutButton = document.getElementById("logout");

const params = new URLSearchParams(window.location.search);
const publicId = params.get("public_id");

if (!publicId) {
    window.location.href = "login.html";
}

logoutButton.addEventListener("click", async function () {
    try {
        await apiRequest("/logout", {
            method: "POST"
        });
    } finally {
        window.location.href = "login.html";
    }
});

async function loadCurrentUser() {
    try {
        const response = await apiRequest(`/users/${publicId}`);
        const user = await getJson(response);

        if (!response.ok) {
            message.textContent = user.detail || "Failed to load user";
            window.location.href = "login.html";
            return;
        }

        if (user.userInfo.role === "admin") {
            showAdminPage(user);
        } else {
            showProfile(user);
        }
    } catch (error) {
        window.location.href = "login.html";
    }
}

function showProfile(user) {
    container.innerHTML = "";

    const heading = document.createElement("h2");
    heading.textContent = "My Profile";
    container.appendChild(heading);

    const info = document.createElement("div");

    info.innerHTML = `
        <p>Name: ${user.userInfo.fullName}</p>
        <p>Email: ${user.email}</p>
        <p>Phone: ${user.userInfo.phone}</p>
        <p>Role: ${user.userInfo.role}</p>
        <p>Status: ${user.isActive ? "Active" : "Inactive"}</p>
    `;

    container.appendChild(info);

    const editButton = document.createElement("button");
    editButton.textContent = "Edit Profile";

    container.appendChild(editButton);

    editButton.addEventListener("click", function () {
        showEditProfileForm(user);
    });
}


function showEditProfileForm(user) {

    const form = document.createElement("form");
    form.className = "form-box";

    form.innerHTML = `
        <label>Name</label>
        <input id="name" value="${user.userInfo.fullName}" required>

        <label>Email</label>
        <input id="email" type="email" placeholder="Enter email to change">

        <label>Phone</label>
        <input id="phone" placeholder="Enter phone to change">

        <label>Password</label>
        <input id="password" type="password">

        <button type="submit">Update Profile</button>
    `;

    container.innerHTML = "";
    container.appendChild(form);

    const backButton = document.createElement("button");
    backButton.textContent = "Back";
    container.appendChild(backButton);

    backButton.addEventListener("click", function () {
        showProfile(user);
    });


    form.addEventListener("submit", async function (event) {

        event.preventDefault();

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const password = document.getElementById("password").value;

        if (!name) {
            message.textContent = "Name cannot be empty";
            return;
        }

        if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            message.textContent = "Enter a valid email";
            return;
        }

        if (phone && !/^\d{10}$/.test(phone)) {
            message.textContent = "Phone must contain exactly 10 digits";
            return;
        }

        if (password && password.length < 8) {
            message.textContent = "Password must be at least 8 characters";
            return;
        }

        const userData = {
            user_info: {
                full_name: name
            }
        };

        if (email) userData.email = email;
        if (phone) userData.user_info.phone = phone;
        if (password) userData.password = password;

        const response = await apiRequest(`/users/${publicId}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        });

        const data = await getJson(response);

        if (!response.ok) {
            message.textContent = data.detail || "Update failed";
            return;
        }

        message.textContent = "Profile updated successfully";

        showProfile(data);
    });
}





function showAdminPage(currentUser) {
    container.innerHTML = "";

    const heading = document.createElement("h2");
    heading.textContent = "Admin Dashboard";
    container.appendChild(heading);

    const createButton = document.createElement("button");
    createButton.textContent = "Create User";
    container.appendChild(createButton);

    const formArea = document.createElement("div");
    container.appendChild(formArea);

    createButton.addEventListener("click", function () {
        showCreateForm(formArea);
    });

    loadUsers();
}

async function loadUsers() {
    const response = await apiRequest("/users");
    const data = await getJson(response);

    if (!response.ok) {
        message.textContent = data.detail || "Failed to load users";
        return;
    }

    const oldTable = document.getElementById("users-table");
    if (oldTable) oldTable.remove();

    const table = document.createElement("table");
    table.id = "users-table";

    table.innerHTML = `
        <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Role</th>
            <th>Active</th>
            <th>Actions</th>
        </tr>
    `;

    data.forEach(function (user) {
        const row = document.createElement("tr");

        row.innerHTML = `
            <td>${user.userInfo.fullName}</td>
            <td>${user.email}</td>
            <td>${user.userInfo.phone}</td>
            <td>${user.userInfo.role}</td>
            <td>${user.isActive ? "Yes" : "No"}</td>
            <td></td>
        `;

        const actions = row.lastElementChild;

        const editButton = document.createElement("button");
        editButton.textContent = "Edit";
        editButton.className = "action-button";
        editButton.addEventListener("click", function () {
            showEditForm(user);
        });

        const deleteButton = document.createElement("button");
        deleteButton.textContent = "Delete";
        deleteButton.className = "action-button";
        deleteButton.addEventListener("click", function () {
            deleteUser(user.publicId);
        });

        actions.append(editButton, deleteButton);
        table.appendChild(row);
    });

    container.appendChild(table);
}

function showCreateForm(formArea) {
    formArea.innerHTML = `
        <form id="create-form" class="form-box">
            <h3>Create User</h3>

            <label>Name</label>
            <input id="create-name" required>

            <label>Email</label>
            <input id="create-email" type="email" required>

            <label>Password</label>
            <input id="create-password" type="password" required>

            <label>Phone</label>
            <input id="create-phone" required>

            <label>Role</label>
            <select id="create-role">
                <option value="user">User</option>
                <option value="admin">Admin</option>
            </select>

            <label>
                <input id="create-active" type="checkbox" checked>
                Active
            </label>

            <button type="submit">Create</button>

            <button type="button" id="create-back-button">
                Back
            </button>

        </form>
    `;

    document.getElementById("create-back-button").addEventListener("click", function () {
        formArea.innerHTML = "";
        loadUsers();
    });

    document.getElementById("create-form").addEventListener("submit", async function (event) {
        event.preventDefault();

        const name = document.getElementById("create-name").value.trim();
        const email = document.getElementById("create-email").value.trim();
        const password = document.getElementById("create-password").value;
        const phone = document.getElementById("create-phone").value.trim();
        const role = document.getElementById("create-role").value;
        const isActive = document.getElementById("create-active").checked;

        if (!name || !email || !password || !phone) {
            message.textContent = "All fields are required";
            return;
        }

        if (password.length < 8) {
            message.textContent = "Password must be at least 8 characters";
            return;
        }

        if (!/^\d{10}$/.test(phone)) {
            message.textContent = "Phone must contain exactly 10 digits";
            return;
        }

        const userData = {
            email: email,
            password: password,
            is_active: isActive,
            user_info: {
                full_name: name,
                phone: phone,
                role: role
            }
        };

        const response = await apiRequest("/users", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        });

        const data = await getJson(response);

        if (!response.ok) {
            message.textContent = data.detail || "Create failed";
            return;
        }

        message.textContent = "User created successfully";
        formArea.innerHTML = "";
        loadUsers();
    });
}

function showEditForm(user) {
    let oldForm = document.getElementById("edit-form");
    if (oldForm) oldForm.remove();

    const form = document.createElement("form");
    form.id = "edit-form";
    form.className = "form-box";

    form.innerHTML = `
        <h3>Edit User</h3>

        <label>Name</label>
        <input id="edit-name" value="${user.userInfo.fullName}" required>

        <label>Email</label>
        <input id="edit-email" type="email" placeholder="New email">

        <label>Phone</label>
        <input id="edit-phone" placeholder="New phone">

        <label>Password</label>
        <input id="edit-password" type="password">

        <label>Role</label>
        <select id="edit-role">
            <option value="user">User</option>
            <option value="admin">Admin</option>
        </select>

        <label>
            <input id="edit-active" type="checkbox">
            Active
        </label>

        <button type="submit">Save</button>

        <button type="button" id="edit-back-button">
            Back
        </button>
    `;

    form.querySelector("#edit-role").value = user.userInfo.role;
    form.querySelector("#edit-active").checked = user.isActive;

    container.appendChild(form);

    document.getElementById("edit-back-button").addEventListener("click", function () {
        form.remove();
        loadUsers();
    });

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const name = document.getElementById("edit-name").value.trim();
        const email = document.getElementById("edit-email").value.trim();
        const phone = document.getElementById("edit-phone").value.trim();
        const password = document.getElementById("edit-password").value;
        const role = document.getElementById("edit-role").value;
        const isActive = document.getElementById("edit-active").checked;

        if (!name) {
            message.textContent = "Name cannot be empty";
            return;
        }

        if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
            message.textContent = "Enter a valid email";
            return;
        }

        if (phone && !/^\d{10}$/.test(phone)) {
            message.textContent = "Phone must contain exactly 10 digits";
            return;
        }

        if (password && password.length < 8) {
            message.textContent = "Password must be at least 8 characters";
            return;
        }

        const userData = {
            user_info: {
                full_name: name,
                role: role
            },
            is_active: isActive
        };

        if (email) userData.email = email;
        if (phone) userData.user_info.phone = phone;
        if (password) userData.password = password;

        const response = await apiRequest(`/users/${user.publicId}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(userData)
        });

        const data = await getJson(response);

        if (!response.ok) {
            message.textContent = data.detail || "Update failed";
            return;
        }

        message.textContent = "User updated successfully";
        form.remove();
        loadUsers();
    });
}

async function deleteUser(id) {
    if (!confirm("Are you sure you want to delete this user?")) {
        return;
    }

    const response = await apiRequest(`/users/${id}`, {
        method: "DELETE"
    });

    if (!response.ok) {
        const data = await getJson(response);
        message.textContent = data.detail || "Delete failed";
        return;
    }

    message.textContent = "User deleted successfully";
    loadUsers();
}

loadCurrentUser();
