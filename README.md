# Boilerplate : Streamlit app + Persistant Database + Docker deployment

- Minimalist [Streamlit](https://streamlit.io/) application with sqlite database using [SQLAlchemy](https://www.sqlalchemy.org/)
- GitHub Actions for CI/CD :
  - Build image Using Docker
  - Push image to DockerHub repository
  - Deploy app on any server with persistant data storage using `docker-compose`
- Compatible with deployment on a Raspberry Pi or any micro server with `arm64` architecture

## Requirements

- a server (VPS or Raspbery Pi) with ssh access (key-based), and `docker-compose` installed
- a [DockerHub](https://hub.docker.com/) account with an application token
- (optional) a reverse proxy on the server configured to redirect `0.0.0.0:8501` to the domain needed

## How to use

**Setup:**
- Clone this repo locally
- Edit `.github/workflows/deploy.yml` and change `<your_dockerhub_username>` to... your DockerHub username
- Create a GitHub repo and push your code there
- Set up **GitHub secrets** :
  - Docker login : `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`.
  - Server access :
    - `HOST` : server adress
    - `USERNAME` : name of user on server
    - `KEY` : private key used to ssh the server
    - `SSH_PASSPHRASE` : password to access private key

**Deploy your app on your server :**
- In your GitHub repo online, go to *Actions* tab and manually run the workflow
- your app is now running on your server and accessible there at `0.0.0.0:8501`. You can use a reverse-proxy to make it accessible over the internet.

**Test your app locally :**
```bash
docker build -t <your_dockerhub_username>/app . #adapt with your username
docker compose up #and shutdown app with ctrl+C
```

## Customization

- You can make your DockerHub repo private, and use any other Container Registry
- Customize github actions workflow:
  - Faster build : possibility to adapt `platforms` key to your server architecture. E.g. remove `arm` if not needed, to speed up deployment
  - Possibility to trigger workflow automatically (e.g. after every push to `main` branch), see [official documentation](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)
- Possibility to add a reverse-proxy with Docker, adapting `docker-compose.yml` file. Many tutos available online (e.g. [here](https://github.com/sapped/Authenticated-Full-Stack-Streamlit)).
