# provihack-equipe2

# Rotas

## POST - Registrando Company

Registro de uma empresa que irá receber a coleta seletiva.

### Endpoint: /company/register:

Request

```
{
	"name" : "coleta",
  "cnpj": "10.000.000/0001-14",
  "phone":"(xx)xxxxx-xxxx",
  "password":"1234",
  "email":"coleta@coleta.com.br",
	"address":{
        "cep":  "0000",
        "street": "rua d",
        "complement": "travessa h",
        "state": "BA",
				"district":"casa",
				"city":"baia",
        "number": "10"
    }
}
```

Response
-status 201 CREATED

```
{
  "id": "38c9e1f6-fe6c-497e-a2e7-767ceb270989",
  "name": "coleta",
  "cnpj": "10.000.000/0001-14",
  "phone": "(xx)xxxxx-xxxx",
  "email": "coleta@coleta.com.br",
  "quantity_collect": 0,
  "address": {
    "street": "rua d",
    "district": "casa",
    "city": "baia",
    "number": 10,
    "complement": "travessa h",
    "state": "BA",
    "cep": "0000"
  }
}
```

- status 400 BAD REQUEST

  ```
  <!-- Caso não seja passado uma chave obrigatória -->
  {
      "cnpj": [
          "Missing cnpj for required field."
      ]
  }
  ```

  ```
  <!-- Caso seja enviado uma chave com valor inválido -->
  {
   "phone": [
  "Not a valid string."
  ]
  }
  ```

## GET - Listar Empresas

Retorna uma lista com todas as empresas registradas. Esta rota aceita query params para filtrar por bairro.

### Endpoint: /company

### Endpoint com query params: /company?district=travessa

Response de todas as empresas
-status 200 OK

```
[
  {
    "id": "727f8630-c078-49a1-854c-f6a73054ba6e",
    "name": "coleta",
    "cnpj": "00.000.000/0001-14",
    "phone": "(xx)xxxxx-xxxx",
    "email": "coleta@coleta.com.br",
    "quantity_collect": 0,
    "address": {
      "street": "rua b",
      "district": "travessa",
      "city": "baia",
      "number": 0,
      "complement": "travessa",
      "state": "BA",
      "cep": "000"
    }
  },

  {
    "id": "38c9e1f6-fe6c-497e-a2e7-767ceb270989",
    "name": "coleta",
    "cnpj": "10.000.000/0001-14",
    "phone": "(xx)xxxxx-xxxx",
    "email": "coleta@coleta.com.br",
    "quantity_collect": 0,
    "address": {
      "street": "rua d",
      "district": "casa",
      "city": "baia",
      "number": 10,
      "complement": "travessa h",
      "state": "BA",
      "cep": "0000"
    }
  }
]
```

Response de uma empresa em que foi utlizado o query params
-status 200 OK

```
[
  {
    "id": "727f8630-c078-49a1-854c-f6a73054ba6e",
    "name": "coleta",
    "cnpj": "00.000.000/0001-14",
    "phone": "(xx)xxxxx-xxxx",
    "email": "coleta@coleta.com.br",
    "quantity_collect": 0,
    "address": {
      "street": "rua b",
      "district": "travessa",
      "city": "baia",
      "number": 0,
      "complement": "travessa",
      "state": "BA",
      "cep": "000"
    }
  },
  {
    "id": "99fd50c0-90ad-49ab-b533-26b3211cdd9f",
    "name": "coleta",
    "cnpj": "10.000.000/0001-14",
    "phone": "(xx)xxxxx-xxxx",
    "email": "coleta@coleta.com.br",
    "quantity_collect": 0,
    "address": {
      "street": "rua d",
      "district": "travessa",
      "city": "baia",
      "number": 10,
      "complement": "travessa h",
      "state": "BA",
      "cep": "0000"
    }
  }
]
```

## GET - Listar uma Empresas

Retorna uma empresas filtrada pelo id passado na url.

### Endpoint: /company/<id>:

Response
-status 200 OK

```
{
  "id": "727f8630-c078-49a1-854c-f6a73054ba6e",
  "name": "coleta",
  "cnpj": "00.000.000/0001-14",
  "phone": "(xx)xxxxx-xxxx",
  "email": "coleta@coleta.com.br",
  "quantity_collect": 0,
  "address": {
    "street": "rua b",
    "district": "travessa",
    "city": "baia",
    "number": 0,
    "complement": "travessa",
    "state": "BA",
    "cep": "000"
  }
}
```

## PUT - Atualizando o update da empresa

Pode atualizar o email, senha e acrescentar quantidade de residuo coletado.

### Endpoint: /company

- Necessário autenticação - bearer token

Request
-body

```
{
{
  "password":"1234",
  "email":"coleta@coleta.com.br",
	"quantity_collect":1
}
}
```

Response
-status 204

```
No budy returned for response
```

-status 401 UNAUTHORIZED

```
{
  "error": "Não é permitido alterar CNPJ"
}
```

## POST - Registrando Resíduos

Registra um resíduo que o usuário pretende descartar. Deve ser passado o tipo de resíduo, a quantidade, o endereço onde este resíduo está localizado e a data em que ele estará disponível para coleta.

### Endpoint: /residues/register:

- Necessário autenticação - bearer token
- Caso não seja passado o address no body, será usado o mesmo endereço do usuário

Request

- body

```
{
	"type":"aluminio",
	"quantity": 6,
	"date": "2022-04-29 20:51",
	"address":{
                "cep":  "000",
                "street": "rua d",
                "complement": "travessa",
                "state": "BA",
                "number": "0",
                "district": "Bairro 13",
                "city": "ColetaCity"
            }
}
```

Response

- status 201 CREATED
  ```
    {
        "id": "4e7abf07-740c-4aed-ad84-553e932d9569",
        "type": "garrafas pet",
        "quantity": 6,
        "collected": false,
        "date": "2022-04-29T20:51:00",
        "address": {
            "street": "rua d",
            "district": "Bairro 13",
            "city": "ColetaCity",
            "number": 0,
            "complement": "travessa",
            "state": "BA",
            "cep": "000"
            },
        "user": {
            "name": "Miqueias",
            "email": "testandoi@mail.com",
            "address": {
            "street": "rua a",
            "district": "Bairro 13",
            "city": "Coletandia",
            "number": 0,
            "complement": "travessa",
            "state": "BA",
            "cep": "0004-00"
            }
        }
    }
  ```
- Status 400 BAD REQUEST
  ```
  <!-- Caso não seja passado uma chave obrigatória -->
  {
      "date": [
          "Missing data for required field."
      ]
  }
  ```
  ```
  <!-- Caso seja enviado uma chave com valor inválido -->
  {
      "quantity": [
          "Not a valid number."
      ]
  }
  ```

## GET - Listar Resíduos

Retorna uma lista com todos os resíduos registrados.

### Endpoint: /residues:

- status 200 OK
  ```
    [
        {
        "id": "eeb7fdd7-7d6c-4d46-9e57-37d83e90a837",
        "type": "aluminio",
        "quantity": 6,
        "collected": true,
        "date": "2022-04-29T20:51:00",
        "address": {
                "street": "rua c",
                "district": "Bairro 13",
                "city": "ColetaCity",
                "number": 0,
                "complement": "travessa",
                "state": "BA",
                "cep": "000"
                },
        "user": {
            "name": "Miqueias",
            "email": "testandoi@mail.com"
            },
        "company": {
            "name": "coleta",
            "email": "coleta@coleta.com.br"
            }
        }
    ]
  ```

## GET - pesquisa um resíduo

Busca e retorna o resíduo com uuid informado na url.

### Endpoint: /residues/< uuid >:

Response

- status 200 OK
  ```
  {
    "id": "63cc45a7-0e14-4c01-8359-33f8fbea71e7",
    "type": "aluminio",
    "quantity": 6,
    "collected": false,
    "date": "2022-04-29T20:51:00",
    "address": {
        "street": "rua a",
        "district": "Bairro 13",
        "city": "Coletandia",
        "number": 0,
        "complement": "travessa",
        "state": "BA",
        "cep": "0004-00"
        },
    "user": {
        "name": "Miqueias",
        "email": "testandoi@mail.com"
        },
    "company": null
  },
  ```
- status 400 BAD REQUEST
  ```
    {
        "message": "O id do resíduo passado por parâmetro deve ser do formato uuid v4"
    }
  ```

## PATCH - Coleta de Resíduos

Registra empresa responsável pela coleta do resíduo.

### Endpoint: /residues/< uuid >:

- Só uma empresa logada tem acesso a esta rota
- Necessário autenticação - bearer token
- Não é necessário body

Response

- status 200 OK

  ```
        No body returned for response
  ```

- status 401 UNAUTHORIZED
  ```
    {
        "message": "Somente uma empresa cadastrada pode acessar esta rota"
    }
  ```
- status 404 NOT FOUND
  ```
    {
        "message": "O residuo não foi encontrado"
    }
  ```
- status 400 BAD REQUEST
  ```
    {
        "message": "O id do resíduo passado por parâmetro deve ser do formato uuid v4"
    }
  ```
