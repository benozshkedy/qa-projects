function showAlert() {
    console.log("Done!")
    //alert("Thank You")
    // console.log(document.getElementById("fname").value);
    let lname1 = document.getElementById("lname").value
    let fname =  document.getElementById("fname").value
    alert(lname1 + " " + fname + " Thank You");
    getWeather()

}
async function getWeather() {
    const city = document.getElementById("city").value;

    if (!city) {
        alert("Enter a city name");
        return;
    }

    try {
        // 1) Geocode city → lat/lon
        const geoRes = await fetch(
            `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}`
        );
        const geo = await geoRes.json();

        if (!geo.results || geo.results.length === 0) {
            document.getElementById("result").textContent = "City not found.";
            return;
        }

        const { latitude, longitude, name, country } = geo.results[0];

        // 2) Get weather from Open-Meteo
        const weatherRes = await fetch(
            `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current=temperature_2m,weather_code`
        );
        const weather = await weatherRes.json();

        const temp = weather.current.temperature_2m;
        const code = weather.current.weather_code;
        const time = weather.current.time

        alert(`
          ${name}, ${country}
          Temperature: ${temp}°C
          Weather Code: ${code}
          Time: ${time}
        `);
    } catch (err) {
        console.error(err);
        document.getElementById("result").textContent = "Error fetching weather.";
    }
}