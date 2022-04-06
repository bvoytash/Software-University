import * as api from './api/api.js';

export const login = api.login;
export const register = api.register;
export const logout = api.logout;


export async function getAllAlbums(){
    return api.get('/data/albums?sortBy=_createdOn%20desc&distinct=name')
}

export function createItem(data){
    return api.post('/data/albums', data);
}

export function getById(id){
    return api.get('/data/albums/' + id);
}

export function deleteItem(id){
    return api.del('/data/albums/' + id);
}

export function updateItem(id, data){
    return api.put('/data/albums/' + id, data);
}

export function getAlbumById(query){
    return api.get(`/data/albums?where=name%20LIKE%20%22${query}%22`)
}


// //  <---- LIKES  ----->
// export async function likeBook(bookId){
//     return api.post('/data/likes', {bookId})
// }
// export async function getLikeByBookId(bookId){
//     return api.get(`/data/likes?where=bookId%3D%22${bookId}%22&distinct=_ownerId&count`)
// }
// export async function getMyLikeByBookId(bookId, userId){
//     return api.get(`/data/likes?where=bookId%3D%22${bookId}%22%20and%20_ownerId%3D%22${userId}%22&count`)
// }
