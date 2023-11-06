#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

async function fetchCharacters (movieId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  try {
    const filmResponse = await new Promise((resolve, reject) => {
      request(apiUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(body);
        }
      });
    });

    const film = JSON.parse(filmResponse);
    const characters = film.characters;

    for (const characterUrl of characters) {
      const charResponse = await new Promise((resolve, reject) => {
        request(characterUrl, (charError, response, charBody) => {
          if (charError) {
            reject(charError);
          } else {
            resolve(charBody);
          }
        });
      });

      const character = JSON.parse(charResponse);
      console.log(character.name);
    }
  } catch (error) {
    console.error(error);
  }
}

const movieId = process.argv[2];
fetchCharacters(movieId);
