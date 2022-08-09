const csrftoken = document.body.querySelector("input").getAttribute("value")
const submitBtn = document.getElementById("submit-btn")

const sendRequest = () => {
  const firstName = document.getElementById("first_name").value
  const userName = document.getElementById("username").value
  const password = document.getElementById("password").value

  const user = {
    first_name: firstName,
    username: userName,
    password: password
  }

  console.log(user)

  axios.post('/api/users/register/', user, {
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken
    }
  }).then(response => console.log(response.data))
     .catch(error => console.log(error))
}

submitBtn.addEventListener("click", sendRequest)