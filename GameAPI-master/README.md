# Game API Server

## Setup instructions

You need to have `make` installed. In general, things a developer will want to
do (besides writing code!) will correspond to a `make` target.

- To create the env for a new developer, run `make dev_env`.
- To run the server locally, use `source/local.sh`
- To build production, type `make prod`.

## Requirements

The requirements for our Game API server are:

- The user can sign up.
- The user can create a new game.
- The user can edit a new game.
- The user can delete a game.
- The user can list all games.
- The user can join a game.
- One can list character types available.
- One can create a character of an available type.
- The character can be moved in the game.
- The character can interact with other characters.
- The character can "look around."
- A player can list all characters in the game? Or are some invisible?

## Design

Most of the above requirements will map directly to an API endpoint.
We will use flask restx for our API server, as we have experience with it.

We want the options available to the user stored on the server.
This way, menus etc. live in a single place.

Some design issues to be resolved.

- How do we specify a game?
- How much flexibility to users have in creating games?
- How much visual guidance resides on the server?
