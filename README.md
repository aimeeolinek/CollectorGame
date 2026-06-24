# Flower Collector 🌸

Flower Collector é um jogo de plataforma 2D desenvolvido em Python utilizando a biblioteca Pygame.

O objetivo do jogador é coletar flores espalhadas pelo cenário e alcançar a bandeira ao final da fase, evitando os obstáculos pelo caminho.

## Funcionalidades

* Movimentação horizontal do personagem
* Sistema de pulo com gravidade
* Coleta de flores e sistema de pontuação
* Obstáculos que causam derrota ao jogador
* Tela de vitória e tela de game over
* Sistema de melhor pontuação (score)
* Fundo com efeito de parallax
* Organização baseada em Programação Orientada a Objetos (POO)

## Estrutura do Projeto

O projeto foi desenvolvido utilizando uma arquitetura orientada a objetos, com classes responsáveis por diferentes partes do jogo:

* `Game` – controla o fluxo principal da aplicação
* `Menu` – exibe e gerencia o menu inicial
* `Level` – controla a lógica da fase
* `Player` – representa o personagem jogável
* `Entity` – classe base para as entidades do jogo
* `Collectable` – flores coletáveis
* `Obstacle` – obstáculos do cenário
* `Flag` – objetivo final da fase
* `Background` – sistema de fundo e efeito parallax
* `Score` – gerenciamento da pontuação
* `EntityFactory` – criação das entidades do jogo

## Tecnologias Utilizadas

* Python 3
* Pygame

## Status do Projeto

Projeto desenvolvido como atividade acadêmica do curso de Análise e Desenvolvimento de Sistemas, com melhorias e funcionalidades adicionadas durante o processo de aprendizagem.

---

Desenvolvido por Aimeê Isabela Olinek.
