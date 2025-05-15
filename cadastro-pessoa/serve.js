// Server.js
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('./db');

const app = express();
const port = 3000;

// Permite ler dados de formulários
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Servir arquivos HTML, CSS e JS da pasta public
app.use(express.static('public'));

// Permite o uso de CORS
app.post('/cadastrar', (req, res) => {
    const { nome } = req.body;
    db.run("INSERT INTO usuarios (nome) VALUES (?)", [nome], (err) => {
        if (err) return res.status(500).send('Erro ao cadastrar usuário');
        res.send("Usuário cadastrado com sucesso");
    });
});

// Rota para listar os pessoas
app.get('/listar', (req, res) => {
    db.all("SELECT * FROW pessoas", [], (err, rows) => {
        if (err) return res.status(500).send("Erro ao buscar");
        res.json(rows);
    });
});

// Rodar o servidor 
app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
