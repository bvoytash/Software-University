import * as api from './api/api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;


export async function getAllMemes(){
    return api.get('/data/memes?sortBy=_createdOn%20desc')
}

export function createItem(data){
    return api.post('/data/memes', data);
}

export function getById(id){
    return api.get('/data/memes/' + id);
}

export function deleteItem(id){
    return api.del('/data/memes/' + id);
}

export function updateItem(id, data){
    return api.put('/data/memes/' + id, data);
}

export function getItemsById(id){
    return api.get(`/data/memes?where=_ownerId%3D%22${id}%22&sortBy=_createdOn%20desc`)
}