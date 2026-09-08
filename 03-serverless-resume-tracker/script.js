const form = document.getElementById("applicationForm");
const message = document.getElementById("message");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const application = {
        applicationID: "app-" + Date.now(),
        company: document.getElementById("company").value,
        position: document.getElementById("position").value,
        status: document.getElementById("status").value
    };

    try {
        const response = await fetch(
            "https://f8v2ne4egk.execute-api.us-east-1.amazonaws.com/prod/applications",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(application)
            }
        );

        const result = await response.text();

        if (!response.ok) {
            throw new Error("API Error " + response.status + ": " + result);
        }

        message.textContent = "Application saved successfully!";
        form.reset();

    } catch (error) {
        message.textContent = "Error: " + error.message;
        console.error(error);
    }
});