import { getUserData } from '../api/util.js';
import { deleteItem, getById, getLikeByBookId, getMyLikeByBookId, likeBook } from '../data.js';
import {html} from '../lib.js';

const detailsTemplate = (book, isOwner, onDelete, likes, hasLike, userData, onLike) => html`
<section id="details-page" class="details">
    <div class="book-information">
        <h3>${book.title}</h3>
        <p class="type">Type: ${book.type}</p>
        <p class="img"><img src="${book.imageUrl}"></p>
        <div class="actions">
            ${isOwner ? html`
            <a class="button" href="/edit/${book._id}">Edit</a>
            <a class="button" @click="${onDelete}" href="/">Delete</a>` : null}

            ${likeTemplate(isOwner, hasLike, userData, onLike)}
            <div class="likes">
                <img class="hearts" src="/images/heart.png">
                <span id="total-likes">Likes: ${likes }</span>
            </div>
            
        </div>
    </div>
    <div class="book-description">
        <h3>Description:</h3>
        <p>${book.description}</p>
    </div>
</section>`;

const likeTemplate = (isOwner, hasLike, userData, onLike) => {
    if(userData == undefined){
        return null
    }
    if(isOwner || hasLike){
        return null
    }else{
        return html`<a class="button" @click="${onLike}" href="javascript:void(0)">Like</a>`
    }
};

export async function detailsBook(ctx){
    const userData = getUserData();

    const book = await getById(ctx.params.id);

    // <----LIKES------>
    const likes = await getLikeByBookId(ctx.params.id);
    const hasLike = userData ? await getMyLikeByBookId(ctx.params.id, userData.id) : 0;
    // <---- LIKES------>


    const isOwner = userData && userData.id == book._ownerId;
    ctx.render(detailsTemplate(book, isOwner, onDelete, likes, hasLike, userData, onLike));

    async function onDelete(){
        const choice = confirm('Are you sure?');
        if(choice){
            await deleteItem(ctx.params.id);
            ctx.page.redirect('/');
        }
    }

    async function onLike(){
        await likeBook(ctx.params.id);
        ctx.page.redirect(`/details/${ctx.params.id}`)
    }
}