const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function askQuestion(question) {
  return new Promise((resolve) => {
    rl.question(question, resolve);
  });
}

async function lista_tolto() {
  let name = await askQuestion("Add meg a lista nevét: ");

  let num = Number(await askQuestion("Hány tagú lesz a lista?: "));

  let lista = [];
  for (let i = 0; i < num; i++) {
    let element = await askQuestion(`Add meg a(z) ${i + 1}. elemet: `);
    lista.push(element);
  }

  console.log(`A ${name} listád elemei: ${lista.join(", ")}`);
  console.log(lista);

  rl.close();
}

lista_tolto();
