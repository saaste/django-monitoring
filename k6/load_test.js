import { check, sleep, print } from 'k6'
import http from "k6/http"

function getRandomAnimal() {
    return Math.random() <= 0.5 ? "dogs" : "cats";
}

function getRandomMethod() {
    const rand = Math.random();
    if (rand <= 0.40) {
        return "POST";
    } else if (rand <= 0.70) {
        return "PUT";
    } else {
        return "DELETE";
    }
}

function getTestAnimal(response) {
    const body = JSON.parse(response.body)
    const testObjects = body.filter(o => o.is_test);
    if (testObjects) {
        return testObjects[0];
    }
    return undefined;
}

function makeGETRequest(animal) {
    return http.get(`http://localhost:8000/${animal}/`);
}

function makePOSTRequest(animal) {
    const payload = JSON.stringify({
        name: 'test_dog',
        breed: 'test_breed',
        likes_to_bark: Math.random() >= 0.5,
        is_test: true,
    })
    return http.post(`http://localhost:8000/${animal}/`, payload);
}

function makePUTRequest(animal, objectId) {
    const payload = JSON.stringify({
        name: 'test_dog_updated',
        breed: 'test_breed_updated',
        likes_to_bark: Math.random() >= 0.5
    })
    return http.put(`http://localhost:8000/${animal}/${objectId}/`, payload);
}

function makeDELETERequest(animal, objectId) {
    return http.del(`http://localhost:8000/${animal}/${objectId}/`);
}

export default function() {
    const isQuery = Math.random() <= 0.95;
    const animal = getRandomAnimal();
    let getResponse, animalToChange;
    if (isQuery) {
        const response = makeGETRequest(animal);
        check(response, {
            [`is GET ${animal} status 200`]: (r) => r.status === 200
        });
    } else {
        const method = getRandomMethod();
        switch (method) {
            case "POST":
                const response = makePOSTRequest(animal);
                check(response, {
                    [`is ${method} ${animal} status 201`]: (r) => r.status === 201
                });
                break;
            case "PUT":
                getResponse = makeGETRequest(animal);
                animalToChange = getTestAnimal(getResponse);
                if (animalToChange) {
                    const response = makePUTRequest(animal, animalToChange.id);
                    check(response, {
                        [`is ${method} ${animal} status 201`]: (r) => r.status === 200
                    });     
                }
                break;
            case "DELETE":
                getResponse = makeGETRequest(animal);
                animalToChange = getTestAnimal(getResponse);
                if (animalToChange) {
                    const response = makeDELETERequest(animal, animalToChange.id);
                    check(response, {
                        [`is ${method} ${animal} status 200`]: (r) => r.status === 200
                    });     
                }
                break;
                
        }
    }
    sleep(0.1);
}

export function teardown() {
    http.get("http://localhost:8000/dogs/clean/");
    http.get("http://localhost:8000/cats/clean/");
}