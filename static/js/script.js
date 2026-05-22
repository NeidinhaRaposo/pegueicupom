const btnCidade = document.getElementById("btnCidade");
const listaCidades = document.getElementById("listaCidades");
const cidadeAtual = document.getElementById("cidadeAtual");
const titulosCidade = document.querySelectorAll(".cidadeTitulo");

const formularioBusca = document.querySelector(".busca");
const campoBusca = document.getElementById("campoBusca");
const cards = document.querySelectorAll(".card");
const mensagemVazia = document.getElementById("mensagemVazia");

let cidadeSelecionada = "Novo Gama";
let textoBusca = "";

btnCidade.addEventListener("click", function () {
    listaCidades.classList.toggle("ativa");
});

listaCidades.addEventListener("click", function (evento) {
    const itemClicado = evento.target;

    if (itemClicado.tagName === "P") {
        cidadeSelecionada = itemClicado.dataset.cidade;

        cidadeAtual.innerText = "Onde você está em " + cidadeSelecionada + "?";

        titulosCidade.forEach(function (titulo) {
            titulo.innerText = cidadeSelecionada;
        });

        listaCidades.classList.remove("ativa");
    }
});

formularioBusca.addEventListener("submit", function (evento) {
    evento.preventDefault();
    textoBusca = campoBusca.value.trim().toLowerCase();
    buscarCards();
});

campoBusca.addEventListener("input", function () {
    textoBusca = campoBusca.value.trim().toLowerCase();
    buscarCards();
});

function buscarCards() {
    let quantidadeVisivel = 0;

    cards.forEach(function (card) {
        const tipoDoCard = card.dataset.tipo.toLowerCase();
        const textoDoCard = card.innerText.toLowerCase();

        const combinaComBusca =
            textoBusca === "" ||
            tipoDoCard.includes(textoBusca) ||
            textoDoCard.includes(textoBusca);

        if (combinaComBusca) {
            card.style.display = "block";
            quantidadeVisivel++;
        } else {
            card.style.display = "none";
        }
    });

    if (mensagemVazia) {
        mensagemVazia.style.display = quantidadeVisivel === 0 ? "block" : "none";
    }
}

const botoesCupom = document.querySelectorAll(".card-info button");

botoesCupom.forEach(function (botao) {
    botao.addEventListener("click", function () {
        const card = botao.closest(".card");
        const empresa = card.querySelector("h4").innerText;
        const cupom = card.querySelector("h3").innerText;

        alert("Cupom resgatado!\n\nEmpresa: " + empresa + "\nOferta: " + cupom);
    });
});

const formSugestao = document.getElementById("formSugestao");
const campoSugestao = document.getElementById("campoSugestao");

if (formSugestao) {
    formSugestao.addEventListener("submit", function (evento) {
        evento.preventDefault();

        const empresaSugerida = campoSugestao.value.trim();

        if (empresaSugerida === "") {
            alert("Digite o nome da empresa que você quer sugerir.");
            return;
        }

        alert("Sugestão enviada!\n\nEmpresa: " + empresaSugerida);
        campoSugestao.value = "";
    });
}

document.addEventListener("click", function (evento) {
    const clicouDentro =
        btnCidade.contains(evento.target) ||
        listaCidades.contains(evento.target);

    if (!clicouDentro) {
        listaCidades.classList.remove("ativa");
    }
});

buscarCards();