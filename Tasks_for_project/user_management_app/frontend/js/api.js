const API_URL = "http://127.0.0.1:8000";

export async function apiRequest(path, options = {}) {
    const response = await fetch(API_URL + path, {
        ...options,
        credentials: "include"
    });

    // Access token may have expired.
    // Ask backend for a new access token and try the original request once.
    if (response.status === 401 && path !== "/users/refresh" && path !== "/logout") {
        const refreshResponse = await fetch(API_URL + "/users/refresh", {
            method: "POST",
            credentials: "include"
        });

        if (refreshResponse.ok) {
            return fetch(API_URL + path, {
                ...options,
                credentials: "include"
            });
        }
    }

    return response;
}

export async function getJson(response) {
    if (response.status === 204) {
        return null;
    }

    const data = await response.json();
    return data;
}
