
# 🌐 Agenda Django 
<div align="center">
  <img src="./frontend/public/banner.png" alt="Logo do Projeto" width="200"/>
</div>

<p align="center">
  <a href="https://github.com/Gileno29/agenda">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/guedes-jr/django_next_auth">
  </a>
  <a href="https://github.com/Gileno29/agenda/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/guedes-jr/django_next_auth">
  </a>
  <a href="https://github.com/Gileno29/agenda/network">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/guedes-jr/django_next_auth">
  </a>
  <a href="https://github.com/Gileno29/agenda/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/guedes-jr/django_next_auth">
  </a>
  <a href="https://github.com/Gileno29/agenda/blob/main/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/github/license/guedes-jr/django_next_auth">
  </a>
</p>

## 📝 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Scripts Disponíveis](#scripts-disponíveis)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Contato](#contato)

## 🛠️ Sobre o Projeto

Este é um projeto full-stack que combina Django para o back-end e Next.js para o front-end. A aplicação visa fornecer uma plataforma robusta para novos projetos.

## 🧰 Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/) - Back-end framework
- [Docker](https://www.docker.com/) - Deploy
- [SQLitle](https://www.sqlite.org/) - Banco de dados
- [Nginx](https://nginx.org/en/) - Servidor Web

## ✨ Funcionalidades

- Inserção de evendos
- Atualização
- Remoção
- Listagem

## 📋 Requisitos

- Python 3.10
- Docker
- Django

## 🚀 Instalação

### Clonando o Repositório

```bash
git clone https://github.com/Gileno29/agenda

cd agenda
```

### Configurando o Back-end (Django)

```bash
# Criar ambiente virtual
python3 -m venv agenda-venv

# Ativar ambiente virtual
source agenda-venv/bin/activate  # No Windows use `venv\Scripts\activate`

# Instalar dependências necessárias para execução do projeto
pip install -r requirements.txt

#Rodar a aplicação em modo de desenvolvimento

python manage.py runserver
```


### Executando a Aplicação em produção

**Back-end:**

```bash
cd backend
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
python manage.py runserver
```

**Front-end:**

```bash
cd frontend
npm run dev
```

## 📦 Scripts Disponíveis

Na pasta `frontend`, você pode rodar:

- `npm run dev`: Executa a aplicação em modo de desenvolvimento.
- `npm run build`: Compila a aplicação para produção.
- `npm run start`: Inicia o servidor Next.js.

Na pasta `backend`, você pode rodar:

- `python manage.py runserver`: Inicia o servidor Django.

## 📁 Estrutura de Pastas

```plaintext
├── backend
├── ApiRoot
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── LICENSE
├── README.md
├── auth
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── frontend
│   ├── README.md
│   ├── next.config.mjs
│   ├── package-lock.json
│   ├── package.json
│   ├── postcss.config.mjs
│   ├── public
│   │   ├── banner.png
│   │   ├── next.svg
│   │   └── vercel.svg
│   ├── src
│   │   ├── app
│   │   │   ├── auth
│   │   │   │   ├── password
│   │   │   │   │   ├── reset-password
│   │   │   │   │   │   └── page.tsx
│   │   │   │   │   └── reset-password-confirmation
│   │   │   │   │       └── page.tsx
│   │   │   │   ├── register
│   │   │   │   │   └── page.tsx
│   │   │   │   └── utils.ts
│   │   │   ├── components
│   │   │   │   ├── Login.module.css
│   │   │   │   ├── Login.tsx
│   │   │   │   ├── Register.tsx
│   │   │   │   ├── ResetPassword.tsx
│   │   │   │   └── ResetPasswordConfirmation.tsx
│   │   │   ├── dashboard
│   │   │   │   ├── Dashboard.module.css
│   │   │   │   └── page.tsx
│   │   │   ├── favicon.ico
│   │   │   ├── fetcher.ts
│   │   │   ├── globals.css
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   └── middleware.ts
│   ├── tailwind.config.ts
│   └── tsconfig.json
├── manage.py
└── requirements.txt
```
> Comando utilizado para mostrar a estrutura de dados `tree -I 'node_modules' -I '__pycache__' -I 'migrations' -I 'venv'`.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

1. Faça um fork do projeto
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça o push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📧 Contato

👤 **Seu Nome**

- Github: [@guedes-jr](https://github.com/guedes-jr)
- LinkedIn: [João Guedes](https://www.linkedin.com/in/jo%C3%A3o-guedes-36a440135)
- Email: joao.guedes.developer@gmail.com

---

Desenvolvido com profissionalismo por [João Guedes](https://github.com/guedes-jr) 🤖.