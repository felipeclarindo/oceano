// Pegando elementos do formulario
const form = document.querySelector("#form");
const submit = document.querySelector("#submit");
const nome = document.querySelector("#nome");
const email = document.querySelector("#email");
const praia = document.querySelector("#praia");
const descricao = document.querySelector("#descricao");
// Pegando elementos do menu
const buttonMenu = document.querySelector(".btn-burguer");
const menu = document.querySelector(".menu");

buttonMenu.addEventListener("click", () => {
  menu.classList.toggle("ativo");
  buttonMenu.classList.toggle("ativo");
})

// Adicionando event listener no submit
form.addEventListener("submit", (event) => {
  // Evitando pagina de carregar
  event.preventDefault();
  // Fazendo validacoes
  let validation1 = verificarInputNome(true);
  let validation2 = verificarInputEmail(validation1);
  let validation3 = verificarInputPraia(validation2);
  let validation4 = verificarInputDescricao(validation3);
  if (validation1 && validation2 && validation3 && validation4) {
    fetch('http://127.0.0.1:5000/relatos/post', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        nome: nome.value,
        email: email.value,
        praia: praia.value,
        descricao: descricao.value
      })
    })
      .then(response => {
        if (!response.ok) {
          createAlert('Erro ao enviar os dados');
        } else {
            createAlert('Dados enviados com sucesso!', "success");
        }
      })
      .catch(error => {
        createAlert('Erro ao conectar com o servidor.');
      });
  }
})

// Verificacao do nome
const verificarInputNome = (response) => {
  const nomeValue = nome.value;
  if (nomeValue === "") {
    // Informando erro!
    errorInput(nome, "Preencha o nome...");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("O Nome não pode ficar vazio.", "warning");
    }
    return false;
  } else if (!isNaN(nomeValue)) {
    errorInput(nome, "O nome deve conter apenas caracteres.");
    // Acionando alerta
    if (response) {
      createAlert("O nome deve conter apenas caracteres.", "warning");
    }
    return false;
  } else if (nomeValue.length > 50) {
    // Informando erro!
    errorInput(nome, "O nome não deve exceder 50 caracteres.");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("O nome não deve exceder 50 caracteres.", "warning");
    }
    return false;
  } else {
    const formItem = nome.parentElement;
    formItem.classList = "form-content";
    return true;
  }
};

// Verificacao do email
const verificarInputEmail = (response) => {
  const emailValue = email.value;
  if (emailValue === "") {
    // Informando erro!
    errorInput(email, "O email é obrigatório.");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("O email é obrigatório.", "warning");
    }
    return false;
  } else if (emailValue.length > 40) {
    // Informando erro!
    errorInput(email, "O email não pode exceder 40 caracteres.");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("O email não pode exceder 40 caracteres.", "warning");
    }
    return false;
  } else {
    const formItem = email.parentElement;
    formItem.className = "form-content";
    return true;
  }
};

// Verificacao da praia
const verificarInputPraia = (response) => {
  const praiaValue = praia.value;
  if (praiaValue === "") {
    // Informando erro!
    errorInput(praia, "Preencha o nome da praia...");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("Preencha o nome da praia...", "warning");
    }
    return false;
  } else if (!isNaN(praiaValue)) {
    // Informando erro
    errorInput(praia, "O nome da praia só deve conter caracteres.");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("O nome da praia só deve conter caracteres.", "warning");
    }
    return false;
  } else if (praiaValue.length > 20) {
    // Informando erro!
    errorInput(praia, "O nome da praia não pode exceder 20 caracteres.");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("O nome da praia não pode exceder 20 caracteres.", "warning");
    }
    return false;
  } else {
    const formItem = praia.parentElement;
    formItem.className = "form-content";
    return true;
  }
};

// Verificacao da descrição
const verificarInputDescricao = (response) => {
  const descricaoValue = descricao.value;
  if (descricaoValue === "") {
    // Informando erro!
    errorInput(descricao, "Preencha a descrição...");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("A descrição não pode estar vazia.", "warning");
    }
    return false;
  } else if (descricaoValue.length > 200) {
    // Informando erro
    errorInput(descricao, "A descrição não pode exceder 200 caracteres.");
    // Verificando dado anterior...
    if (response) {
      // Acionando alerta
      createAlert("A descrição não pode exceder 200 caracteres.", "warning");
    }
    return false;
  } else {
    const formItem = descricao.parentElement;
    formItem.className = "form-content";
    return true;
  }
};

// Criando alerta
const createAlert = (message, type) => {
  var alertBox = document.getElementById("alert");
  var alertMessage = document.getElementById("alert-message");
  alertMessage.textContent = message;
  // Remover classes anteriores
  alertBox.classList.remove("success", "info", "warning");
  // Adicionar nova classe baseada no tipo de alerta
  if (type) {
    alertBox.classList.add(type);
  }
  // Definir display como block
  alertBox.style.display = "block";
  // Esconder o alerta automaticamente após 3 segundos
  setTimeout(() => {
    alertBox.style.display = "none";
  }, 3000);
};

// Criando função para mostrar o erro
const errorInput = (input, message) => {
  const formItem = input.parentElement;
  const textMessage = formItem.querySelector("a");
  textMessage.innerText = message;
  formItem.className = "form-content error";
};

// Configurando modals
const loadModal = () => {
  const myModal = document.querySelector("#modal");
  const buttonsOpenModal = document.querySelectorAll(".btn-relate");
  const buttonCloseModal = document.querySelector("#fechar");

  buttonsOpenModal.forEach((button) => {
    button.addEventListener("click", () => {
      myModal.showModal();
    });
  });

  buttonCloseModal.addEventListener("click", () => {
    buttonCloseModal.addEventListener("blur", () => {
      location.reload();
    });
    myModal.close();
  });
};

document.addEventListener("DOMContentLoaded", () => {
  var closeBtn = document.querySelector(".closebtn");
  var alertDiv = document.querySelector(".alert");

  // Definir display como none ao fechar
  closeBtn.addEventListener("click", function () {
    alertDiv.style.display = "none";
  });

  // Carregando Modal
  loadModal();
});

// Integração ChatBot
window.watsonAssistantChatOptions = {
  integrationID: "c0cf010c-e624-45d4-8618-02c958ca8395", // The ID of this integration.
  region: "us-south", // The region your integration is hosted in.
  serviceInstanceID: "8a23610e-7cde-411e-98a0-a2a5e0839572", // The ID of your service instance.
  onLoad: async (instance) => {
    await instance.render();
  },
};
setTimeout(function () {
  const t = document.createElement("script");
  t.src =
    "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" +
    (window.watsonAssistantChatOptions.clientVersion || "latest") +
    "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});
