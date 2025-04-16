const { Builder, By } = require('selenium-webdriver');

(async function testeHanked() {
const url = 'https://www.hankeds.com.br/prova/login2.html';
let driver = await new Builder().forBrowser('chrome').build(); // Inicia o navegador

try {
await driver.get(url); // Acessa o site
await driver.sleep(2000);


// Constantes dos log in
const username = await driver.findElement(By.id('username')); // Campo usuário
const password = await driver.findElement(By.id('password')); // Campo senha
const botao = await driver.findElement(By.xpath("//button[contains(text(),'Entrar')]")); // Botão entrar

// Digitar devagar usuário
for (const letra of 'admin') {
await username.sendKeys(letra);
await driver.sleep(250);
}

await driver.sleep(1000); //esperar por 1000 segundos

// Digita devagar senha
for (const letra of 'admin123456') {
await password.sendKeys(letra);
await driver.sleep(250);
}

await driver.sleep(1000);
await botao.click(); // clicar no botão
await driver.sleep(4000); 

const urlAtual = await driver.getCurrentUrl(); // Verifica a URL atual
if (urlAtual.includes('destino.html')) {
console.log('Teste passou: redirecionado corretamente.');
} else {
console.log('Teste falhou: não houve redirecionamento.');
}

await driver.sleep(5000);

} catch (err) {
console.error('Erro durante o teste:', err);
} finally {
await driver.quit(); // Fecha o navegador
}
})();