const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})

readline.question('Digite o primeiro número: ', num1 => {
  readline.question('Digite o segundo número: ', num2 => {
    const soma = Number(num1) + Number(num2);
    console.log(`A soma de ${num1} e ${num2} é igual a ${soma}.`);
    readline.close();
  })
})


