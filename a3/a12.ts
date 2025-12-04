async function fetchData() {
    const response = await fetch('http://api.restful-api.dev/objects')
    const data = await response.json()
    console.log(data)
}



fetchData()