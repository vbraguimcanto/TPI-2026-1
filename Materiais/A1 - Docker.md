# Docker - Principais Comandos

Neste material você aprenderá os principais comandos envolvendo o uso de Docker.

## 1. Gerenciamento de Imagens

#### Listar imagens locais
```bash
docker images
```

#### Baixar uma imagem
```bash
docker pull <nome-da-imagem>
```

#### Remover uma imagem
```bash
docker rmi <nome-da-imagem>
```

## 2. Containers

#### Containers em execução
```bash
docker ps
```

#### Todos os containers (inclusive parados)
```bash
docker ps -a
```

#### Criar e executar um container
```bash
docker run <nome-da-imagem>
```

#### Criar e executar um container com porta mapeada
```bash
docker run -p <porta-local>:<porta-container> <nome-da-imagem>
```

#### Criar e executar um container em segundo plano
```bash
docker run -d <nome-da-imagem>
```

#### Parar um container
```bash
docker stop <id-ou-nome-do-container>
```

#### Iniciar um container parado
```bash
docker start <id-ou-nome-do-container>
```

#### Remover um container
```bash
docker rm <id-ou-nome-do-container>
```

## 3. Volumes e Dados

#### Criar um volume
```bash
docker volume create <nome-do-volume>
```

#### Listar volumes
```bash
docker volume ls
```

#### Remover um volume
```bash
docker volume rm <nome-do-volume>
```

#### Executar um container com volume mapeado
```bash
docker run -v <caminho-local>:<caminho-no-container> <nome-da-imagem>
```

## 4. Docker Compose

#### Iniciando Serviços com o Docker Compose
```bash
docker compose up
```

#### Iniciando Serviços em Segundo Plano com Docker Compose
```bash
docker compose up -d
```

#### Parar serviços
```bash
docker compose down
```

## 5. Redes (Networking)

#### Listar Redes
```bash
docker network ls
```

#### Criar uma rede
```bash
docker network create <nome-da-rede>
```

#### Conectar um container a uma rede
```bash
docker network connect <nome-da-rede> <id-ou-nome-do-container>
```

#### Desconectar um container de uma rede
```bash
docker network disconnect <nome-da-rede> <id-ou-nome-do-container>
```

## 6. Dockerfile

#### Construir uma imagem a partir de um Dockerfile
```bash
docker build -t <nome-da-imagem> <caminho-do-dockerfile>
```

#### Executar um Dockerfile
```bash
docker run <nome-da-imagem>
```

## 7. Informações e Diagnósticos

#### Ver informações gerais do Docker
```bash
docker info
```

#### Ver logs de um Docker
```bash
docker logs <id-ou-nome-do-container>
```

#### Inspecionar detalhes de um container ou imagem
```bash
docker inspect <id-ou-nome-do-container-ou-imagem>
```

#### Monitorar o uso de recursos do container
```bash
docker stats
```

## 8. Limpeza de Docker

#### Remover containers parados
```bash
docker container prune
```

#### Remover imagens não utilizadas
```bash
docker image prune
```

#### Remover volumes não utilizadas
```bash
docker volume prune
```

#### Remover tudo (containers, imagens e volumes não utilizados)
```bash
docker system prune
```
