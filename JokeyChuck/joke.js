async function getJoke() {
    try {
        const response = await fetch("https://api.chucknorris.io/jokes/random");
        const data = await response.json();
        document.getElementById("joke").innerText = data.value;
    } catch (error) {
        console.log("Error fetching joke:", error);
    }
}

// Get a joke when the page loads
getJoke();
