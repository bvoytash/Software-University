import * as api from '../src/api/api.js';


export const login = api.login;
export const register = api.register;
export const logout = api.logout;


const endpoints = {
    all: `/data/catalog`,
    byId: `/data/catalog/`,
    myItems: (userId) => `data/catalog?where=_ownerId%3D%22${userId}%22`,
    create: `/data/catalog`,
    update: `/data/catalog/`,
}

export async function getAll(){
    return api.get(endpoints.all);
}
export function getById(id){
    return api.get(endpoints.byId + id);
}

export function getMyItems(userId){
    return api.get(endpoints.myItems(userId));
}

export function createItem(data){
    return api.post(endpoints.create, data);
}

export function updateItem(id, data){
    return api.put(endpoints.update + id, data);
}

export function deleteItem(id){
    return api.del(endpoints.getById + id);
}

