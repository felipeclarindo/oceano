// Pegando elementos do formulario
const form = document.querySelector("#form")
const submit = document.querySelector("#submit");
const nome = document.querySelector("#nome");
const email = document.querySelector("#email");
const praia = document.querySelector("#praia");
const descricao = document.querySelector("#descricao");
let PERMITIDO = false

// Adicionando event listener no submit
form.addEventListener("submit", (event) => {
  event.preventDefault()
  let validation1 = verificarInputNome();
  let validation2 = verificarInputEmail();
  let validation3 = verificarInputPraia();
  let validation4 = verificarInputDescricao();
  if (validation1 && validation2 && validation3 && validation4) {
    PERMITIDO = true;
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
        throw new Error('Erro ao enviar os dados');
      }
      console.log('Dados enviados com sucesso!');
    })
    .then(data => {
      alert(data.message);
    })
    .catch(error => {
      console.error('Erro ao enviar os dados:', error);
    });
  }
})

// Verificacao do nome
const verificarInputNome = () => {
  const nomeValue = nome.value;
  if (nomeValue === "") {
    // Informando erro!
    errorInput(nome, "Preencha o nome...")
    return false
  } else if (!isNaN(nomeValue)) {
    errorInput(nome, "O nome deve conter apenas caracteres.")
    return false
  } else if (nomeValue.length > 50) {
    // Informando erro!
    errorInput(nome, "O nome não deve exceder 50 caracteres.")
    return false
  }else {
    const formItem = nome.parentElement;
    formItem.classList = "form-content";
    return true
  }
}

// Verificacao do email
const verificarInputEmail = () => {
  const emailValue = email.value;
  if (emailValue === "") {
    // Informando erro!
    errorInput(email, "O email é obrigatório.");
    return false;
  } else if (emailValue.length > 40) {
    // Informando erro!
    errorInput(email, "O email não pode exceder 40 caracteres.");
    return false;
  } else {
    const formItem = email.parentElement;
    formItem.className = "form-content";
    return true;
  }
}

// Verificacao da praia
const verificarInputPraia = () => {
  const praiaValue = praia.value;
  if (praiaValue === "") {
    // Informando erro!
    errorInput(praia, "Preencha o nome da praia...");
    return false;
  } else if (!isNaN(praiaValue)){
    // Informando erro
    errorInput(praia, "O nome da praia só deve conter caracteres.")
    return false
  }else if (praiaValue.length > 20) {
    // Informando erro!
    errorInput(praia, "O nome da praia não pode exceder 20 caracteres.");
    return false;
  } else {
    const formItem = praia.parentElement;
    formItem.className = "form-content";
    return true;
  }
}

// Verificacao da descrição
const verificarInputDescricao = () => {
  const descricaoValue = descricao.value;
  if (descricaoValue === "") {
    // Informando erro!
    errorInput(descricao, "Preencha a descrição...");
    return false;
  } else if (descricaoValue.length > 200) {
    // Informando erro
    errorInput(descricao, "A descrição não pode exceder 200 caracteres.");
    return false;
  } else {
    const formItem = descricao.parentElement;
    formItem.className = "form-content";
    return true;
  }
}

// Criando função para mostrar o erro
const errorInput = (input, message) => {
  const formItem = input.parentElement;
  const textMessage = formItem.querySelector("a");
  textMessage.innerText = message;
  formItem.className = "form-content error";
}


// Configurando modals
const loadModal = () => {
  const myModal = document.querySelector("#modal");
  const buttonsOpenModal = document.querySelectorAll("#btn-relate");
  const buttonCloseModal = document.querySelector("#fechar")
  const buttonSubmitModal = document.querySelector("#submit")

  buttonsOpenModal.forEach(button => {
    button.addEventListener("click", () => {
      myModal.showModal();
    });
  });

  buttonCloseModal.addEventListener("click", () => {
    buttonCloseModal.addEventListener("blur", () => {
      location.reload()
    })
    myModal.close()
  })


  buttonSubmitModal.addEventListener("click", () => {
    if (PERMITIDO === true) {
      alert("Enviado com suceso!")
      myModal.close()
    }
  })
};

// Carregando Modal
document.addEventListener("DOMContentLoaded", loadModal());

// Integração ChatBot
window.watsonAssistantChatOptions = {
  integrationID: "c0cf010c-e624-45d4-8618-02c958ca8395", // The ID of this integration.
  region: "us-south", // The region your integration is hosted in.
  serviceInstanceID: "8a23610e-7cde-411e-98a0-a2a5e0839572", // The ID of your service instance.
  onLoad: async (instance) => { await instance.render(); }
};
setTimeout(function () {
  const t = document.createElement('script');
  t.src = "https://web-chat.global.assistant.watson.appdomain.cloud/versions/" + (window.watsonAssistantChatOptions.clientVersion || 'latest') + "/WatsonAssistantChatEntry.js";
  document.head.appendChild(t);
});

