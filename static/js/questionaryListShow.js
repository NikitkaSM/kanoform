const showQuestionaryList = () => {
  return axios.get("/api/questionary-list/", {
    "Content-Type": "application/json"
  })
    .then(response => {
      const questionaries = response.data;
      const ul = document.getElementById('questionariesContainer');

      for (let x = 0; x < questionaries.length; x++) {
        const questionary = questionaries[x];
				const div = document.createElement("div");
        const child = document.createElement('div');
        const name = document.createElement('h2');
				const author = document.createElement("p");
				const deleteButton = document.createElement("button");
				
				name.innerText = `Название: ${questionary.name}`;
				author.innerText = `Автор: ${questionary.user.username}`;

				name.setAttribute("class", "questionary-name");
				author.setAttribute('class', 'questionary-author');
				
				child.setAttribute("class", "questionary");
	      child.setAttribute("id", `${questionary.id}`);
				
				div.setAttribute("style", "display: flex;");
				
				deleteButton.setAttribute("class", "delete-button");
				deleteButton.innerText = "❌";
				deleteButton.addEventListener("click", deleteQuestionary);
				deleteButton.setAttribute("type", "button");

        ul.append(child);
				child.append(name);
	      child.append(div);
				div.append(author);
				div.append(deleteButton);
				
      }
    })
}

const deleteQuestionary = event => {
	const button = event.target;
	const parent = button.parentNode.parentNode;
	const questionaryId = parent.getAttribute("id");
	const token = Cookies.get("csrftoken");
	parent.remove();
	
	axios({
		method: "delete",
		url: `/api/questionary/${questionaryId}`,
		headers: {
			"X-CSRFToken": token
		}
		
	})
}

const init = () => {
  showQuestionaryList();
}

init();