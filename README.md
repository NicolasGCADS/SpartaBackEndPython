# 🐍 API de Taxa de Administração - Python (FastAPI)

## 📖 Sobre o Projeto
Este projeto foi desenvolvido como solução para o Desafio Desenvolvedor BackEnd Júnior, que consiste em calcular o valor da taxa de administração de cada cotista em um fundo de investimento

## ▶️ Como rodar localmente

1. Clone o repositório:
   git clone https://github.com/NicolasGCADS/SpartaBackEndPython

   Rode no Visual Studio Code
   python -m venv .venv
   //Windows
   .venv\Scripts\activate
   //Linux
   source .venv/bin/activate

   Baixe as dependências
   pip install fastapi uvicorn

   Rode o servidor: (Usando Visual Studio Code, é mais facil usar a extensão FastAPI Runner)
   uvicorn app:app --reload
   c:\Users\SeuUsuario\Desktop\SpartaBackEndPython\.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload

   Rode com essa URL
   Swagger UI: http://127.0.0.1:8000/docs

   ## Exemplos em Json para testar a Aplicação
   
```bash
1.
{
  "taxa": 0.01,
  "cotas": [
    {
      "valor": 95.50,
      "quantidades": [50.0, 30.0]
    },
    {
      "valor": 96.25,
      "quantidades": [50.0, 30.0]
    }
  ]
}

2.
{
  "taxa": 0.015,
  "cotas": [
    {
      "valor": 100.00,
      "quantidades": [20.0, 40.0]
    },
    {
      "valor": 101.50,
      "quantidades": [25.0, 35.0]
    }
  ]
}


3.
{
  "taxa": 0.008,
  "cotas": [
    {
      "valor": 80.75,
      "quantidades": [10.0, 50.0]
    },
    {
      "valor": 82.00,
      "quantidades": [15.0, 45.0]
    }
  ]
}
   ```

   ## Principais Decisões
    

   



   

