"""
Dojo 067 - A Festa Junina

Exercício 4: A Distribuição de Doces

Finalmente na festa! Sua última tarefa é ajudar a distribuir os doces para as crianças.
Cada criança tem uma lista de doces que gostaria de receber, em ordem de preferência.
Você tem um estoque limitado de cada tipo de doce.

Sua missão é criar uma função `distribuir_doces(preferencias, estoque)` para
distribuir os doces.

- `preferencias` é um dicionário onde a chave é o nome da criança e o valor é uma
  lista de doces que ela gosta, em ordem de preferência.
- `estoque` é um dicionário onde a chave é o nome do doce e o valor é a quantidade
  disponível.

A função deve retornar um dicionário com o nome da criança como chave e o doce que
ela recebeu como valor.

Regra de Distribuição:
Tente dar o doce de maior preferência para cada criança. Se o doce preferido não
estiver disponível no estoque, tente o segundo, e assim por diante. Se nenhum
dos doces na lista de uma criança estiver disponível, ela não recebe nada.
Para garantir que o resultado seja consistente, processe as crianças em ordem alfabética.

Exemplos de Teste:

1.  Distribuição simples:
    - Preferências: `{"Ana": ["paçoca", "pé de moleque"], "João": ["maçã do amor", "paçoca"]}`
    - Estoque: `{"paçoca": 1, "maçã do amor": 1, "pé de moleque": 1}`
    - Saída esperada: `{"Ana": "paçoca", "João": "maçã do amor"}` (Ana é processada primeiro)

2.  Conflito de preferência:
    - Preferências: `{"Bia": ["canjica"], "Carlos": ["canjica"]}`
    - Estoque: `{"canjica": 1}`
    - Saída esperada: `{"Bia": "canjica"}` (Bia vem antes de Carlos alfabeticamente)

3.  Doce indisponível:
    - Preferências: `{"Davi": ["curau"]}`
    - Estoque: `{"pamonha": 10}`
    - Saída esperada: `{}`

4.  Alternativa por falta de estoque:
    - Preferências: `{"Eva": ["pamonha", "bolo"], "Leo": ["pamonha", "curau"]}`
    - Estoque: `{"pamonha": 1, "bolo": 1, "curau": 1}`
    - Saída esperada: `{"Eva": "pamonha", "Leo": "curau"}` (Eva pega a única pamonha, Leo pega sua segunda opção)

Crie a função `distribuir_doces` e os testes para validar essas regras.
"""
